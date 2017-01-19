from django.db import models


class Section(models.Model):
    initial_seq = 0
    section_text = models.CharField(max_length=255)
    section_seq = models.IntegerField(default=100)

    def __str__(self):
        return str(self.id) + ': ' + self.section_text


class Page(models.Model):
    initial_seq = 0
    page_header = models.TextField(null=True, blank=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    page_seq = models.IntegerField(default=100)

    def __str__(self):
        return str(self.page_seq) + ': ' + self.page_header[:100]


class SubPage(models.Model):
    initial_seq = 0
    sub_page_header = models.TextField(null=True, blank=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)
    sub_page_seq = models.IntegerField(default=100)

    def __str__(self):
        return str(self.sub_page_seq) + ': ' + self.sub_page_header[:100]


class Question(models.Model):
    initial_seq = 0
    # initialise constants for Question types
    SINGLE_QUESTION = 'SingleQuestion'
    MULTI_CHOICE_QUESTION = 'MultiChoiceQuestion'
    TEXT_QUESTION = 'TextQuestion'

    question_seq = models.IntegerField(default=100)
    question_text = models.CharField(max_length=255)

    # tuple of question choices, will make a drop down box.
    QUESTION_TYPE_CHOICES = (
        (SINGLE_QUESTION, 'Single Question'),
        (MULTI_CHOICE_QUESTION, 'Multi-Choice Question'),
        (TEXT_QUESTION, 'Text Question'),
    )
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPE_CHOICES, default=SINGLE_QUESTION)
    sub_page = models.ForeignKey('SubPage', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    initial_seq = 0
    response_text = models.CharField(max_length=255)
    response_value = models.IntegerField()
    response_seq = models.IntegerField(default=100)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.response_text


def default_seq_value(quiz_model):
    """
    Sets a default question seq number
    :return: integer
    """
    quiz_model_title = quiz_model.title()
    quiz_model += "_seq"

    if quiz_model_title.initial_seq == 0:
        quiz_model_title.initial_seq += 100
        return quiz_model_title.initial_seq
    else:
        return quiz_model_title.objects.all().aggregate(models.Max(quiz_model_title.quiz_model)) + 100

