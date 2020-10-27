from django.db import models
from django.contrib.auth.models import User
from sheet.models import level, subject, topic


class exam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TestPaper(models.Model):
    test_type_choice = (
        ("weekly", "weekly"),
        ("mock", "mock"),
        ("subject", "subject"),
        ("topic", "topic"),
        ("previous_year_paper", "previous_year_paper"),
    )
    test_number = models.PositiveSmallIntegerField(unique=True)
    test_name = models.CharField(max_length=50, unique=True)
    select_exam = models.ForeignKey(exam, on_delete=models.CASCADE, blank=True)
    exam = models.CharField(max_length=50)
    test_type = models.CharField(max_length=20,
                                 choices=test_type_choice)
    select_level = models.ForeignKey(
        level, on_delete=models.CASCADE, blank=True)
    level = models.CharField(max_length=50)
    select_subject = models.ForeignKey(
        subject, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True)
    select_topic = models.ForeignKey(
        topic, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.CharField(max_length=50, blank=True)
    time_limit_in_minutes = models.PositiveSmallIntegerField()
    no_of_questions = models.PositiveSmallIntegerField()
    positive_marks = models.IntegerField(blank=True)
    negative_marks = models.IntegerField(blank=True)
    description = models.CharField(max_length=70, blank=True)
    allow_calc = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['test_number', ]
        verbose_name_plural = "TestPapers"

    def __str__(self):
        return f'{self.id}/{self.test_name}'


class questions(models.Model):
    select_test_name = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=50)
    question_no = models.PositiveSmallIntegerField()
    question = models.CharField(max_length=500, null=False)
    questionimage = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    blank_type = models.BooleanField(default=False)
    option_a = models.CharField(blank=True, max_length=100, null=False)
    option_b = models.CharField(blank=True, max_length=100, null=False)
    option_c = models.CharField(blank=True, max_length=100, null=False)
    option_d = models.CharField(blank=True, max_length=100, null=False)
    correct_answer = models.CharField(max_length=50)
    answer_blank = models.CharField(blank=True, max_length=100, null=True)
    solution = models.CharField(blank=True, max_length=500, null=False)
    solution_image = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    solution_video = models.URLField(blank=True, max_length=200)

    class Meta:
        ordering = ['question_no']

    def __str__(self):
        return f'{self.test_name}/{self.question_no}'


class TestIndex(models.Model):
    user = models.CharField(max_length=100)
    select_test_name = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}/{self.test_name}/{self.completed}'


class UserAnswers(models.Model):
    user_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    question_no = models.PositiveSmallIntegerField()
    user_answer = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)
    marks = models.IntegerField(blank=True)

    class Meta:
        ordering = ['question_no']

    def __str__(self):
        return f'{self.id}/{self.user_name}/{self.test_name}/{self.question_no}/{self.user_answer}/{self.correct_answer}/{self.marks}'


class UserResult(models.Model):
    user_name = models.CharField(max_length=100)
    test_name = models.CharField(max_length=100)
    submitted = models.BooleanField(default=False)
    score = models.IntegerField()

    class Meta:
        ordering = ['score']

    def __str__(self):
        return f'{self.user_name}/{self.test_name}/{self.score}'


class flag(models.Model):
    user_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    question_no = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['question_no']

    def __str__(self):
        return f'{self.id}/{self.user_name}/{self.test_name}/{self.question_no}'


class timer(models.Model):
    user_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    time_left = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.id}/{self.user_name}/{self.test_name}/{self.time_left}'
