from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:post_slug>/', views.detail, name='detail'),
    path('<slug:post_slug>/results/', views.results, name='results'),
    path('<slug:post_slug>/submit/', views.submit, name='submit'),
]