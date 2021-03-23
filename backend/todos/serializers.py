from .models import *
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    """
    todos.Task erializer
    """
    class Meta:
        model = Task
        exclude = ()
        read_only_fields = ('id','created_at', 'updated_at')


