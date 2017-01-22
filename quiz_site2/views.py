from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Page, SubPage, Question, Response


def index(request):
    """
    Adapted from: https://docs.djangoproject.com/en/1.10/topics/pagination/
    :param request:
    :return: render(request, template, dictionary of page objects)
    """
    pages = Page.objects.all()
    paginator = Paginator(pages, 1)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages = paginator.page(paginator.num_pages)
    page_dict = {'pages': pages, 'sub_pages': SubPage.objects.all(),
                 'questions': Question.objects.all(), 'responses': Response.objects.all()}
    return render(request, 'page.html', page_dict)



