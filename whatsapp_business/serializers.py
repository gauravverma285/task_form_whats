from rest_framework import serializers
from app.models import Job

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'first_name', 'second_name', 'city']