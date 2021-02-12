from django.http import HttpResponse
from django.template import loader
import os


def index(request):
    template = loader.get_template("landing/index.html")
    return HttpResponse(template.render({}, request))
