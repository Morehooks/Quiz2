from django.contrib import admin
from import_export import resources, fields
from .models import Section, Page, SubPage, Question, Response, Participant, User
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget


"""
Below resources for importing/exporting data into models
"""


class SectionResource(resources.ModelResource):

    class Meta:
        model = Section


class PageResource(resources.ModelResource):
    section = fields.Field(
        column_name='section',
        attribute='section',
        widget=ForeignKeyWidget(Section, 'id'))

    class Meta:
        model = Page


class SubPageResource(resources.ModelResource):
    page = fields.Field(
        column_name='page',
        attribute='page',
        widget=ForeignKeyWidget(Page, 'id'))

    class Meta:
        model = SubPage


class QuestionResource(resources.ModelResource):
    sub_page = fields.Field(
        column_name='sub_page',
        attribute='sub_page',
        widget=ForeignKeyWidget(SubPage, 'id'))

    class Meta:
        model = Question


class ResponseResource(resources.ModelResource):
    question = fields.Field(
        column_name='question',
        attribute='question',
        widget=ForeignKeyWidget(Question, 'id'))

    class Meta:
        model = Response


class ParticipantResource(resources.ModelResource):
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, 'id'))

    class Meta:
        model = Participant


"""
Below admin classes for import/export to use the Admin GUI.
"""


class SectionIOAdmin(ImportExportActionModelAdmin):
    pass


class PageIOAdmin(ImportExportActionModelAdmin):
    pass


class SubPageIOAdmin(ImportExportActionModelAdmin):
    pass


class QuestionIOAdmin(ImportExportActionModelAdmin):
    pass


class ResponseIOAdmin(ImportExportActionModelAdmin):
    pass


class ParticipantIOAdmin(ImportExportActionModelAdmin):
    pass


"""
Registering classes for admin page
"""
admin.site.register(Page, PageIOAdmin)
admin.site.register(Section, SectionIOAdmin)
admin.site.register(SubPage, SubPageIOAdmin)
admin.site.register(Question,  QuestionIOAdmin)
admin.site.register(Response, ResponseIOAdmin)
admin.site.register(Participant, ParticipantIOAdmin)
