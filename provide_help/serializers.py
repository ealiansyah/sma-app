from create_help.models import HelpTicket
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = HelpTicket
    fields = ['response']