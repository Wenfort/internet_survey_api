from django.db import models


class Respondent(models.Model):
    pass


class Survey(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=510)

    def __str__(self):
        return self.name


class Question(models.Model):

    QUESTION_TYPE_CHOICES = (
        (1, 'Вопрос с одним возможным ответом'),
        (2, 'Вопрос с несколькими возможными ответами'),
        (3, 'Вопрос с вводом собственного ответа')
    )

    survey = models.ForeignKey(Survey, related_name='question', on_delete=models.CASCADE)
    text = models.CharField(max_length=510)
    type = models.CharField(max_length=100, choices=QUESTION_TYPE_CHOICES, default=1)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choice', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class RespondentAnswer(models.Model):
    respondent = models.ForeignKey(Respondent, related_name='respondent', on_delete=models.CASCADE, blank=True, null=True)
    survey = models.ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE)
