from django.db import models
from django.urls import reverse


class Puppet(models.Model):
    """

        MicroFrontend settings for your React apps to be delivered
        through a django template.

    """
    name = models.CharField(
        max_length=100,
        help_text="Name of your micro frontend."
    )
    domain_url = models.URLField(
        help_text="The public domain in which the files are hosted."
    )
    internal_url = models.URLField(
        help_text="The internal domain"
    )
    html_file = models.CharField(
        max_length=200,
        help_text="The URL location of the html file of the built SPA app."
    )
    route = models.CharField(
        max_length=255,
        help_text="The django route where the app will be served",
        unique=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("puppet", args=[self.route])


