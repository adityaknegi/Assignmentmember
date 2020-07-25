from rest_framework import serializers
from usertracker.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ActivityPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['start_time', 'end_time']

