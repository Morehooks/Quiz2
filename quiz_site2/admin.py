from django.forms import Textarea
from django.db import models
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Section, Page, SubPage, Question, Response


def get_form_overrides():
    """
    I felt the widgets for text fields were too small, so this class makes them bigger.
    :return: Model fields
    """
    return {
        models.CharField: {'widget': Textarea(attrs={'rows': 1, 'cols': 255})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 200})},
    }


"""
Below are classes to alter the admin GUI for models.
"""


class ResponseInline(admin.StackedInline):
    formfield_overrides = get_form_overrides()
    model = Response
    extra = 1


class QuestionInline(admin.StackedInline):
    formfield_overrides = get_form_overrides()
    model = Question
    extra = 1


class SubPageAdmin(admin.ModelAdmin):
    formfield_overrides = get_form_overrides()
    fieldsets = [
        (None, {'fields': ['sub_page_header', 'sub_page_seq', 'section', 'page']}),
    ]
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    formfield_overrides = get_form_overrides()
    fieldsets = [
        (None,               {'fields': ['question_text', 'question_seq', 'question_type', 'sub_page']}),
    ]
    inlines = [ResponseInline]


"""
Below resources for importing/exporting data into models
"""


class SectionResource(resources.ModelResource):

    class Meta:
        model = Section


class PageResource(resources.ModelResource):

    class Meta:
        model = Page


class SubPageResource(resources.ModelResource):

    class Meta:
        model = SubPage


class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question


class ResponseResource(resources.ModelResource):

    class Meta:
        model = Response


"""
Below admin classes for import/export to use the Admin GUI.
"""


class SectionIOAdmin(ImportExportModelAdmin):
    resource_class = SectionResource


"""
Registering classes for admin page
"""
admin.site.register(Section, SectionIOAdmin)
admin.site.register(Page)
admin.site.register(SubPage, SubPageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
