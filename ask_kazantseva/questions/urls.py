"""ask_kazantseva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from questions.views import index, ask, user_settings, logout, signup, tags, hot, login, question

urlpatterns = [
    path(r'', index, name="index"),
    path(r'ask', ask, name="ask"),
    path(r'settings', user_settings, name="settings"),
    path(r'logout', logout, name="logout"),
    path(r'signup',signup, name="signup"),
    path(r'login',login, name="login"),
    path(r'tag/<str:tag>', tags, name="tag"),
    path(r'hot', hot, name="hot"),
    path(r'question/<int:id_question>', question, name="question"),
]
