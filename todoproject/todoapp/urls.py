from django.urls import path
from .views import HomePageView, TaskCreateView, TaskDetailView, TaskDeleteView,TaskSearchView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', TaskCreateView.as_view(), name='newtask'),
    path('<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('search/', TaskSearchView.as_view(), name='search'),



]
