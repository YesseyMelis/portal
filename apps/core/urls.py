from django.urls import path

from apps.core import views

urlpatterns = [
    path('student/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('student/<int:pk>', views.StudentUpdateView.as_view(), name='student-update'),
]

app_name = 'core'
