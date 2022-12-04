from rest_framework import serializers
from .models import HelpTicket

class HelpFormSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelpTicket
        fields = ['url', 'username', 'email', 'is_staff']