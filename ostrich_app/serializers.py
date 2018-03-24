from rest_framework import serializers
from .models import OstrichBreeders, EggsBabies


class OstrichBreedersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OstrichBreeders
        fields = ("name", "birth_year", "sex", "description")


class OstrichEggsBabiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EggsBabies
        fields = ("number", "sex", "description", "father", "mother")
