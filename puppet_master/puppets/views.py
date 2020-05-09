from django.conf import settings
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from bs4 import BeautifulSoup
from django.core.cache import cache

import requests

from puppet_master.puppets.models import Puppet

LOGIN_URL = getattr(settings, "LOGIN_URL", "/admin/login/")


def build_link(url, tag, type):
    """
        Prepends a micro frontend domain url to the original
        absolute path

    :param url:
    :param tag:
    :param type:
    :return:
    """

    if tag[type].startswith('/'):
        tag[type] = f"{url}{tag[type]}"


def parse_descendants(url, descendants):
    """

        Checks the descendants of a tag from beautiful soup
        for and child with an href attribute or src attr and
        builds a link with the micro frontend domain

    :param url:
    :param descendants:
    :return:
    """
    for child in descendants:
        try:
            if child.has_attr('href'):
                build_link(url, child, 'href')
            if child.has_attr('src'):
                build_link(url, child, 'src')
        except AttributeError:
            pass


def puppet_view(request, route):
    """

    Based on the route, this view fetches the generated html
    file of a microfrontend such as React.js

    :param request:
    :param route:
    :return:
    """

    # Get list of available puppet routes and find the one that
    # is being requested.

    current_route = None
    puppet_routes = Puppet.objects.all().values('route')
    for puppet_route in puppet_routes:
        puppet_route_str = puppet_route['route']
        if route.find(puppet_route_str, 0, len(puppet_route_str)) >= 0:
            current_route = puppet_route_str

    if not current_route:
        raise Http404("Unable to locate route for application.")

    mf = get_object_or_404(Puppet, route=current_route)

    if mf.requires_login and not request.user.is_authenticated:
        return redirect(f"{LOGIN_URL}?next={request.get_full_path()}")

    context = cache.get(f'puppet-{mf.id}')
    if not context:
        req = requests.get(f"{mf.html_file}")
        soup = BeautifulSoup(req.text, 'html.parser')
        parse_descendants(mf.domain_url, soup.head.contents)
        parse_descendants(mf.domain_url, soup.body.contents)

        context = {
            "body": soup.body.prettify(),
            "head": soup.head.prettify()
        }

        cache.set(f'puppet-{mf.id}', context, 500)

    return render(
        request,
        "puppets/puppet.html",
        {"react_index": context}
    )


def index(request):
    """
    Homepage of the django-microfrontend-suite
    :param request:
    :return:
    """

    return render(request, "puppets/index.html", {"micro_frontends": Puppet.objects.all()})
