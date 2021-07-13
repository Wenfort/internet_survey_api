from rest_framework import serializers

from .models import Survey, Question, Choice, Respondent, RespondentAnswer


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=510)
    type = serializers.IntegerField()
    choice = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    start_day = serializers.DateTimeField()
    end_day = serializers.DateTimeField()
    description = serializers.CharField(max_length=510)
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'


class SurveySerializerWithBlockedStartDay(SurveySerializer):
    start_day = serializers.DateTimeField(read_only=True)

здесь не конкретный, будем использовать для отправки данных
class Re(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    survey = serializers.SlugRelatedField(queryset=Survey.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)

    class Meta:
        model = Respondent
        fields = ['__all__']

здесь данные по конкретному
class RespondentAnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    respondent = Re(many=True)

    class Meta:
        model = Respondent
        fields = ['__all__']

