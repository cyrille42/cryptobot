from django.shortcuts               import render
from django.contrib.auth.models     import User

from rest_framework.generics        import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions     import IsAuthenticatedOrReadOnly

from .models                        import Alert, Rule

from .serializers                   import AlertSerializer, UserSerializer, RuleSerializer

from django.http import HttpResponse

class AlertList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'pk'

class UserList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class RuleList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class RuleDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    lookup_field = 'pk'
