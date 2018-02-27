from rest_framework import serializers
from .models import OstrichBreeders


class OstrichBreedersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OstrichBreeders
        fields = ("name", "birth_year", "sex", "description")
