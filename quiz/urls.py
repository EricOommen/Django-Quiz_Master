from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("topics/", views.topic_selection, name="topic_selection"),
    path(
        "experience-level/<str:topic>/", views.experience_level, name="experience_level"
    ),
    path("quiz/<str:topic>/<str:level>/", views.quiz_page, name="quiz_page"),
    path("result/", views.result_page, name="result_page"),
    path("history/", views.history_page, name="history_page"),
]
