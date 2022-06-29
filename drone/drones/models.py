from django.db import models



class DroneCategory(models.Model):

    name=models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Drone(models.Model):

    name=models.CharField(max_length=256)
    description=models.TextField()
    has_it_competed=models.BooleanField(default=False)
    category=models.ForeignKey(DroneCategory,on_delete=models.CASCADE,related_name='drones')
    user=models.ForeignKey('auth.User',related_name='drones',on_delete=models.CASCADE)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name


class Pilot(models.Model):

    MALE='M'
    FEMALE='F'

    GENDER_CHOICES=(
        (MALE,'male'),
        (FEMALE,'female')
    )

    name=models.CharField(max_length=256)
    gender=models.CharField(max_length=2,choices=GENDER_CHOICES,default=MALE)
    races_count=models.IntegerField()

    def __str__(self):
        return self.name


class Competition(models.Model):

    name=models.CharField(max_length=256)
    max_distance=models.IntegerField()

    pilot=models.ForeignKey(Pilot,on_delete=models.CASCADE,related_name='competition')
    drone=models.ForeignKey(Drone,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
