from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:meeting_count>/', views.meetings, name='meetings')
]
