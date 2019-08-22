from rest_framework import serializers
from .models import Accounts,Clients,Mov


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = '__all__'

class MovSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mov
        fields = '__all__'