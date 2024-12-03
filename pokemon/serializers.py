from .models import Pokemon
from rest_framework import serializers

class PokemonSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Pokemon
        fields='__all__'