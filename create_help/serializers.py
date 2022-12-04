from rest_framework import serializers
from .models import HelpForm

class HelpFormSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelpForm
        fields = ['url', 'username', 'email', 'is_staff']