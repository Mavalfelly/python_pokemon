from .models import Pokemon
from rest_framework import viewsets,permissions
from .serializers import PokemonSerializers

class PokeViewSet(viewsets.ModelViewSet):
    queryset=Pokemon.objects.all()
    serializer_class=PokemonSerializers
    permission_classes=[permissions.AllowAny]