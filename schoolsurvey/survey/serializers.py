from rest_framework import serializers
from .models import Survey
from .models import Category
<<<<<<< HEAD
from .models import Answers, Questionaire
=======
from .models import Question, Answers
>>>>>>> cf263849322247aab8b3cd232ec75db274f5cd70


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'url', 'name', 'description')

<<<<<<< HEAD
# class QuestionSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Question
#         fields = ('id', 'url', 'title', 'help', 'category')


class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'url', 'school', 'answer', 'questionId')

class QuestionaireSerializer(serializers.ModelSerializer):
    pages = serializers.JSONField() # change is here

    class Meta:
        model = Questionaire
        fields = ('id','pages',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    questionaire =  QuestionaireSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'description','questionaire')
=======

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'survey', 'visibility', 'allows_edit',
                  'identifier', 'description', 'form_builder_json', 'custom_submit_url')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'url', 'title', 'help', 'category')


class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'url', 'answer', 'question')
>>>>>>> cf263849322247aab8b3cd232ec75db274f5cd70
