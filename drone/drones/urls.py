from django.urls import path
from .views import *


app_name='v1'

urlpatterns = [
    path('',ApiRoot.as_view(),name=ApiRoot.name),
    path('categories',DroneCategoryList.as_view(),name='category_list'),
    path('categories/<int:pk>/',DroneCategoryDetail.as_view(),name='dronecategory-detail'),
    path('drones',DroneList.as_view(),name=DroneList.name),
    path('drones/<int:pk>/',DroneDetail.as_view(),name=DroneDetail.name),
    path('pilots',PilotList.as_view(),name=PilotList.name),
    path('pilots/<int:pk>/',PilotDetail.as_view(),name=PilotDetail.name),
    path('competitions',CompetitionList.as_view(),name=CompetitionList.name),
    path('competitions/<int:pk>/',CompetitionDetail.as_view(),name=CompetitionDetail.name)
]