from rest_framework import serializers
from .models import HelpTicket

class HelpFormSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelpTicket
        fields = ['title', 'description']