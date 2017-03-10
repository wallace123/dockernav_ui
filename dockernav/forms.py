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
    """ Input VNC info """

    class Meta:
        model = Container
        fields = (
            'vnc_pass',
        )


class JabberForm(forms.ModelForm):
    """ Input Jabber info """

    class Meta:
        model = Container
        fields = (
            'user1',
            'pass1',
            'user2',
            'pass2',
        )
