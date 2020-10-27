from django.db import models
from django.contrib.auth.models import User


class level(models.Model):

    level = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.level


class subject(models.Model):
    select_level = models.ForeignKey(level, on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    class Meta:
        ordering = ['select_level']

    def __str__(self):
        return f'{self.level}/{self.subject}'


class topic(models.Model):
    select_level = models.ForeignKey(level, on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    select_subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)

    class Meta:
        ordering = ['select_level']

    def __str__(self):
        return f'{self.level}/{self.subject}/{self.topic}'


class sheet_name(models.Model):
    sheet_type_choice = (
        ("main", "main"),
        ("practice", "practice")
    )
    sheet_name = models.CharField(max_length=50, unique=True)
    select_level = models.ForeignKey(level, on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    select_subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    select_topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    sheet_type = models.CharField(max_length=20,
                                  choices=sheet_type_choice)
    no_of_questions = models.PositiveSmallIntegerField()
    concept = models.TextField(blank=True)
    concept_image = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    concept_video = models.URLField(blank=True)
    description = models.CharField(max_length=70, blank=True)
    allow_calc = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id}/{self.sheet_name}'


class questions(models.Model):

    select_sheet_name = models.ForeignKey(
        sheet_name, on_delete=models.CASCADE)
    sheet_name = models.CharField(max_length=50)
    question_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=False)
    question_image = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    blank_type = models.BooleanField(default=False)
    option_a = models.CharField(blank=True, max_length=100, null=False)
    option_b = models.CharField(blank=True, max_length=100, null=False)
    option_c = models.CharField(blank=True, max_length=100, null=False)
    option_d = models.CharField(blank=True, max_length=100, null=False)
    correct_answer = models.CharField(
        blank=True, max_length=100, null=False)
    option_blank = models.CharField(blank=True, max_length=100, null=True)
    hint = models.CharField(blank=True, max_length=500, null=False)
    hint_image = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    hint_video = models.URLField(blank=True, max_length=200)

    class Meta:
        ordering = ['question_no']

    def __str__(self):
        return f'{self.sheet_name}/{self.question_no}'


class index(models.Model):
    user_name = models.CharField(max_length=100)
    sheet_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user_name}/{self.sheet_name}'


class UserAnswers(models.Model):
    user_name = models.CharField(max_length=50)
    sheet_name = models.CharField(max_length=50)
    question_no = models.PositiveSmallIntegerField()
    user_answer = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)

    class Meta:
        ordering = ['question_no']

    def __str__(self):
        return f'{self.id}/{self.user_name}/{self.sheet_name}/{self.question_no}/{self.user_answer}/{self.correct_answer}'


class flag(models.Model):
    user_name = models.CharField(max_length=50)
    sheet_name = models.CharField(max_length=50)
    question_no = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['question_no']

    def __str__(self):
        return f'{self.id}/{self.user_name}/{self.sheet_name}/{self.question_no}'
