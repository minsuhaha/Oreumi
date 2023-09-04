from rest_framework import serializers
from .models import *

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'