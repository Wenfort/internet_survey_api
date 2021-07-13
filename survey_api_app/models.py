from django.db import models


class Respondent(models.Model):
    pass


class Survey(models.Model):
    name = models.CharField(max_length=255)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    description = models.CharField(max_length=510)
    respondents = models.ManyToManyField(Respondent, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='question', on_delete=models.CASCADE)
    text = models.CharField(max_length=510)
    type = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choice', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class RespondentAnswer(models.Model):
    respondent = models.ForeignKey(Respondent, related_name='respondent', on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE)