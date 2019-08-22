from rest_framework import generics, viewsets
from .models import Clients,Accounts,Mov
from .serializers import ClientSerializer, AccountSerializer, MovSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
