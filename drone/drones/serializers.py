from rest_framework import serializers
from .models import *


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):

    drones=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='drone_detail')

    class Meta:
        model=DroneCategory
        fields=('url','pk','name','drones')



class DroneSerializer(serializers.HyperlinkedModelSerializer):

    drone_category=serializers.SlugRelatedField(queryset=DroneCategory.objects.all(),slug_field='name')

    class Meta:
        model=Drone
        fields=('url','name','description','drone_category')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):

    drones=DroneSerializer()

    class Meta:
        model=Competition
        fields=('url','pk','name','drone')

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competititons=CompetitionSerializer(many=True,read_only=True)

    class Meta:
        model=Pilot
        fields=('url','pk','gender','name','competitions')


class PilotCompetitionsSerializer(serializers.HyperlinkedModelSerializer):
    pilot=serializers.SlugRelatedField(queryset=Pilot.objects.all(),slug_field='name')
    drone=serializers.SlugRelatedField(queryset=Drone.objects.all(),slug_field='name')

    class Meta:
        model=Competition
        fields=('url','pk','max_distance','pilot','drone')

        
