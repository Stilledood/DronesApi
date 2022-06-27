from django.shortcuts import render
from .serializers import DroneCategorySerializer,DroneSerializer,PilotSerializer,CompetitionSerializer,PilotCompetitionsSerializer
from rest_framework import generics
from .models import *


class DroneCategoryList(generics.ListCreateAPIView):

    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer



class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer



class DroneList(generics.ListCreateAPIView):

    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class PilotList(generics.ListCreateAPIView):

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer


class CompetitionList(generics.ListCreateAPIView):

    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionsSerializer


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionsSerializer

    
