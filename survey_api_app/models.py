from django.db import models


class Respondent(models.Model):
    pass


class Survey(models.Model):
    name = models.CharField(max_length=255)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    description = models.CharField(max_length=510)
    type = models.SmallIntegerField()
    respondents = models.ManyToManyField(Respondent)

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=510)

    def __str__(self):
        return self.text


class Choice(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
