from rest_framework import serializers
from Main.models import Flowers

class FlowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flowers
        fields = '__all__'