# Django Puppet Master

![alt text](https://raw.githubusercontent.com/overnite-software/django-puppetmaster/master/docs/assets/puppetmaster.png "How it works")

Django Puppet Master is a Django application for instantiating and routing to micro front ends such as React.
You can leverage the power of Django's out of the box templating, session authentication, and permissions to manage requests
from your micro frameworks.

For now, there is only support for React based apps.

### 1. Installation

`pip install git+https://github.com/overnite-software/django-puppetmaster`

Add the package to your installed apps:
```
INSTALLED_APPS = [
    ...django apps,
    'puppet_master.puppets',
]
```

Run `python manage.py migrate`.

### 2. Create a puppet

A puppet is an object that represents your frontend application. It holds the data necessary to retrieve information about the app.

In the Django admin, add a new puppet and provide the required data.

```
Name: # Name you want to give your microfrontend. This is just for you

Domain URL: # The domain where your microfrontend is hosted.

HTML file: # The URL location of the main html file of your frontend application. Ex. 'https://domain.com/index.html'

Route: # The route your app will be accessible on.

Requires Login: # Check if you want the route to be authenticated users only.

```

### 3. Using CSRF protection

For CSRF protection: make sure you send request with the header `X-CSRFToken` assinged with the value of the `csrftoken` cookie.



