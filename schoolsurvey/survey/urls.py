
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('surveys', views.SurveyView)
router.register('categories', views.CategoryView)
router.register('question', views.QuestionView)
router.register('answers', views.AnswersView)

urlpatterns = [

    path('', include(router.urls))

]
