from django.db import models
from django.utils import timezone
import os
from datetime import datetime


def make_dir():
    directory = '/docker-mount-' + str(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f"))
    os.mkdir(directory)
    return directory


# Create your models here.
class Container(models.Model):
    """ Describe a container """

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    timestamp = models.DateTimeField(default=timezone.now)

    DOCKER_VNC = 'docker-vnc'
    DOCKER_MESSAGER = 'docker-messager'
    CONTAINER_CHOICES = (
        (DOCKER_VNC, 'docker-vnc'),
        (DOCKER_MESSAGER, 'docker-messager'),
        )

    container = models.CharField(
        max_length=20,
        choices=CONTAINER_CHOICES,
        default=DOCKER_VNC,
    )

    def __str__(self):
        return '%s_%s' % (self.user, self.container)

    directory = models.CharField(
        max_length=50,
        default=make_dir
    ) 
