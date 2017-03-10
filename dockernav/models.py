""" Models.py sets tables for database """

from django.db import models
from django.utils import timezone


# Create your models here.
class NavServer(models.Model):
    """ Holds the IP and Port of the available Nav Servers """
    name = models.CharField(max_length=20)

    host = models.CharField(max_length=20)
    port = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Container(models.Model):
    """ Holds the supported docker containers """
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    navserver = models.ForeignKey(
        'dockernav.NavServer',
        on_delete=models.CASCADE,
    )

    created_date = models.DateTimeField(default=timezone.now)

    rand_int = models.IntegerField(default=0, unique=True)

    DOCKER_IMAGES = (
        ('vnc', 'wallace123/docker-vnc'),
        ('jabber', 'wallace123/docker-jabber'),
    )

    image = models.CharField(max_length=10, choices=DOCKER_IMAGES)

    vnc_pass = models.CharField(max_length=20, blank=True)

    jabber_ip = models.CharField(max_length=20, blank=True)
    user1 = models.CharField(max_length=20, blank=True)
    pass1 = models.CharField(max_length=20, blank=True)

    user2 = models.CharField(max_length=20, blank=True)
    pass2 = models.CharField(max_length=20, blank=True)

    # Cleanup items
    category = models.CharField(max_length=30, blank=True)
    loop_file = models.CharField(max_length=30, blank=True)
    dservice = models.CharField(max_length=30, blank=True)
    dockerd = models.CharField(max_length=30, blank=True)
    device = models.CharField(max_length=30, blank=True)
    port = models.CharField(max_length=6, blank=True)
    docker_run = models.CharField(max_length=30, blank=True)
    docker_lib = models.CharField(max_length=30, blank=True)
    docker_bridge = models.CharField(max_length=16, blank=True)
    mount_point = models.CharField(max_length=30, blank=True)
    container = models.CharField(max_length=30, blank=True)
    dservice_path = models.CharField(max_length=40, blank=True)
    docker = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return '%s-%d' % (self.image, self.rand_int)
