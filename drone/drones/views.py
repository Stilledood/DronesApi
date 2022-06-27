from django.shortcuts import render
from .serializers import DroneCategorySerializer,DroneSerializer,PilotSerializer,CompetitionSerializer,PilotCompetitionsSerializer
from rest_framework import generics
from .models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse


class DroneCategoryList(generics.ListCreateAPIView):

    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer




class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer



class DroneList(generics.ListCreateAPIView):

    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name='drone-list'


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name='drone-detail'


class PilotList(generics.ListCreateAPIView):

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name='pilot-list'


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name='pilot-detail'


class CompetitionList(generics.ListCreateAPIView):

    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionsSerializer
    name='competition-list'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionsSerializer
    name='competition-detail'


class ApiRoot(generics.GenericAPIView):
    name='api-root'

    def get(self,request,*args,**kwargs):
        return Response(
            {
                'drone-categories':reverse('category_list',request=request),
                'drones':reverse(DroneList.name,request=request),
                'pilots':reverse(PilotList.name,request=request),
                'competitions':reverse(CompetitionList.name,request=request)

            }
        )


