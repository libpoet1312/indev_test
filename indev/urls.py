"""indev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings.base as settings
from categories.views import CategoryListView
from questions.views import QuestionViewSet, QuestionDetailView, checkAnswerForQuestion

urlpatterns = [
    path('admin/', admin.site.urls),

    path('questions/', TemplateView.as_view(template_name='crud.html')),

    path('questions/<int:question_id>/', QuestionDetailView.as_view()),



    path('api/v1/categories/', CategoryListView.as_view()),
    path('api/v1/questions/<int:question_id>/<str:answer_text>/', checkAnswerForQuestion),
]

router = DefaultRouter()
router.register('api/v1/questions', QuestionViewSet, basename='question')
urlpatterns += router.urls

# hack to serve static files under docker without modifying nginx in docker
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
# urlpatterns = format_suffix_patterns(urlpatterns)
