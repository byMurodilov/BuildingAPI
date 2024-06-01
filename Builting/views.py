from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny


from .models import Hudud, Qurilishtashkiloti, Qurilishbinosi
from .serializers import HududSerializer, QurilishtashkilotiSerializer, QurilishbinosiSerializer


class HududViewSet(viewsets.ModelViewSet):
    
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class QurilishtashkilotiViewSet(viewsets.ModelViewSet):

    queryset = Qurilishtashkiloti.objects.all()
    serializer_class = QurilishtashkilotiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class QurilishbinosiViewSet(viewsets.ModelViewSet):
    queryset = Qurilishbinosi.objects.all()
    serializer_class = QurilishbinosiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




def index(request):
    return render(request, 'index.html')