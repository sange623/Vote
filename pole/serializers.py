from rest_framework import serializers
from .models import User,PoleHaveOptions,PoleTable,Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class PoleHaveOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoleHaveOptions
        fields = '__all__'

class PoleTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoleTable
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
