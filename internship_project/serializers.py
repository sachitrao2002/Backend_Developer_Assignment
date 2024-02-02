from rest_framework import serializers
from .models import user_data
from django.contrib.auth import get_user_model
class user_dataSerilizater(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields="__all__"
        


    