from django.forms import Textarea
from django.db import models
from django.contrib import admin
from .models import Section, Page, SubPage, Question, Response


def get_form_overrides():
    return {
        models.CharField: {'widget': Textarea(attrs={'rows': 1, 'cols': 255})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 200})},
    }


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


admin.site.register(Section)
admin.site.register(Page)
admin.site.register(SubPage, SubPageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
