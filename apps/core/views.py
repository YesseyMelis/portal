from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.core.models import Student
from apps.core.serializers import StudentSerializer, StudentUpdateSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    permission_classes = (AllowAny,)
    http_method_names = ('put',)
