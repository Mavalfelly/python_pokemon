from .models import Pokemon
from rest_framework import viewsets, status
from .serializers import PokemonSerializers, UserSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class PokeViewSet(viewsets.ModelViewSet):
    queryset=Pokemon.objects.all()
    serializer_class=PokemonSerializers
    permission_classes=[IsAuthenticated]
    # auto associates the input w the authed user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # only owned pokemon returned
    def get_queryset(self):
        return Pokemon.objects.filter(user=self.request.user)
    


class UserRegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User was created succesfuly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)