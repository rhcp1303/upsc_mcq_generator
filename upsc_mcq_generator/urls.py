from django.contrib import admin
from django.urls import path
import questions.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test1/', views.test1, name='test1'),
    path('api/test1_view/', views.test1_view, name='test1_view')
]
