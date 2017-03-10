""" Forms for adding a Container """

from django import forms
from .models import Container

class ImageForm(forms.ModelForm):
    """ Select a supported image """

    class Meta:
        model = Container
        fields = (
            'image',
        )


class VNCForm(forms.ModelForm):
    """ Add VNC items to Image """

    class Meta:
        model = Container
        fields = (
            'vnc_pass',
        )


class JabberForm(forms.ModelForm):
    """ Add Jabber items to Image """

    class Meta:
        model = Container
        fields = (
            'user1',
            'pass1',
            'user2',
            'pass2',
        )
