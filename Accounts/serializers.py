from rest_framework import serializers
from .models import Accounts,Clients,Mov


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = ('id','name', 'mail', 'phone')

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = ('id','client','account','date')

class MovSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mov
        fields = ('__all__')