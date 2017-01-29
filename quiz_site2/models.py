from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    # initial_seq = 0
    section_text = models.CharField(max_length=255)
    section_seq = models.IntegerField(default=100)

    def __str__(self):
        return str(self.id) + ': ' + self.section_text


class Page(models.Model):
    # initial_seq = 0
    page_header = models.TextField(blank=True)
    page_seq = models.IntegerField(default=100)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.page_seq) + ': ' + self.page_header[:100]


class SubPage(models.Model):
    # initial_seq = 0
    sub_page_header = models.TextField(blank=True)
    sub_page_seq = models.IntegerField(default=100)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sub_page_seq) + ': ' + self.sub_page_header[:100]


class Question(models.Model):
    # initial_seq = 0
    # initialise constants for Question types
    SINGLE_QUESTION_TABLE = 'SingleQuestionTable'
    SINGLE_QUESTION_LIST = 'SingleQuestionList'
    MULTI_CHOICE_QUESTION = 'MultiChoiceQuestion'
    TEXT_QUESTION = 'TextQuestion'

    # initialise yes no constants
    YES = 'Y'
    NO = 'N'

    # tuple of question choices, will make a drop down box.
    QUESTION_TYPE_CHOICES = (
        (SINGLE_QUESTION_TABLE, 'Single Question Table'),
        (SINGLE_QUESTION_LIST, 'Single Question List'),
        (MULTI_CHOICE_QUESTION, 'Multi Choice Question'),
        (TEXT_QUESTION, 'Text Question'),
    )

    SUB_QUESTION_CHOICES = (
        (YES, 'Y'),
        (NO, 'N'),
    )

    question_seq = models.IntegerField(default=100)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPE_CHOICES, default=SINGLE_QUESTION_TABLE)
    sub_question = models.CharField(max_length=1, choices=SUB_QUESTION_CHOICES, default=NO)
    sub_page = models.ForeignKey('SubPage', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    # initial_seq = 0

    # initialise yes no constants
    YES = 'Y'
    NO = 'N'

    RESPONSE_OPS_CHOICES = (
        (YES, 'Y'),
        (NO, 'N'),
    )

    response_text = models.CharField(max_length=255)
    response_value = models.IntegerField()
    response_seq = models.IntegerField(default=100)
    response_ops = models.CharField(max_length=1, choices=RESPONSE_OPS_CHOICES, default=NO)
    response_columns = models.IntegerField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.response_text


class Participant(models.Model):
    ONLINE = 'Online'
    PAPER = 'Paper'
    NO_PART = 'Not_Participated'

    SURVEY_TYPE_CHOICES = (
        (ONLINE, 'Online'),
        (PAPER, 'Paper'),
        (NO_PART, 'Not Participated')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=255, choices=SURVEY_TYPE_CHOICES, default=ONLINE)
    survey_type = models.CharField(max_length=20)

    def __str__(self):
        return self.organisation


def default_seq_value(quiz_model):
    """
    Sets a default question seq number, not in use.

    :return: integer
    """
    quiz_model_title = quiz_model.title()
    quiz_model += "_seq"

    if quiz_model_title.initial_seq == 0:
        quiz_model_title.initial_seq += 100
        return quiz_model_title.initial_seq
    else:
        return quiz_model_title.objects.all().aggregate(models.Max(quiz_model_title.quiz_model)) + 100

