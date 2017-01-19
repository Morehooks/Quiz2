from django.shortcuts import render
from django.http import Http404
from .models import Section


def index(request):
    try:
        sections = Section.objects.all()
    except Section.DoesNotExist:
        raise Http404("Section does not exist")
    return render(request, 'section_test.html', {'section': sections})