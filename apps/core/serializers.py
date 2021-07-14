from rest_framework import serializers

from apps.core.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'performance': {'required': False}}


class StudentUpdateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    performance = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = ('full_name', 'birth_date', 'performance')
