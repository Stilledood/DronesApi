from django.shortcuts import render
from .serializers import DroneCategorySerializer,DroneSerializer,PilotSerializer,CompetitionSerializer,PilotCompetitionsSerializer
from rest_framework import generics
from .models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import rest_framework as filters
from rest_framework import permissions
from .custompermissions import IsCurrentUserOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle


class DroneCategoryList(generics.ListCreateAPIView):

    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    filter_fields=('name',)
    search_fields=('^name',)
    ordering_fields=('name',)




class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer



class DroneList(generics.ListCreateAPIView):

    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)

    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name='drone-list'

    search_fields=('^name',)
    ordering_fields=('name','category',)
    filter_fields=('name','category',)

    permissions_classes=(permissions.IsAuthenticated,IsCurrentUserOrReadOnly)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):

    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)

    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name='drone-detail'

    permission_classes = (permissions.IsAuthenticated,IsCurrentUserOrReadOnly)


class PilotList(generics.ListCreateAPIView):

    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name='pilot-list'

    search_fields=('^name','^gender',)
    ordering_fields=('name',)
    filter_fields=('name',)

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):

    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name='pilot-detail'

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)



class CompetitionFilters(filters.FilterSet):
    '''Class to create a custom filter for competitions list'''

    min_distance_competition=filters.NumberFilter(field_name='max_distance',lookup_expr='gte')
    max_distance_competition=filters.NumberFilter(field_name='max_distance',lookup_expr='lte')
    drone_name=filters.AllValuesFilter(field_name='drone__name')
    pilot_name=filters.AllValuesFilter(field_name='pilot__name')

    class Meta:
        model=Competition
        fields=('max_distance','min_distance_competition','max_distance_competition','drone_name','pilot_name')







class CompetitionList(generics.ListCreateAPIView):

    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionsSerializer
    name='competition-list'

    filterset_class=CompetitionFilters
    ordering_fields=(
        'max_distance','name'
    )



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


