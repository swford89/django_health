from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:post_slug>/', views.detail, name='detail'),
    path('<slug:post_slug>/results/', views.results, name='results'),
    path('<slug:post_slug>/submit/', views.submit, name='submit')
]
