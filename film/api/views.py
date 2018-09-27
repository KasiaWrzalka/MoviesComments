from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.reverse import reverse
import json, requests
from .serializers import MoviesSerializer, CommentsSerializers
from film.models import Movies, Comments

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movies': reverse('moviesList', request=request, format=format)
        # 'user': reverse('userList', request=request, format=format)
    })

class MoviesList(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = MoviesSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Movies.objects.all()

    def perform_create(self, serializer):
        response = requests.get("http://www.omdbapi.com/?apikey=e914fe0d&t=" + str(serializer.validated_data['title']))
        python_dictionary_values = json.loads(response.text)
        if python_dictionary_values['Response'] == "True":
            serializer.save(
                year=python_dictionary_values['Year'],
                rated=python_dictionary_values['Rated'],
                relased=python_dictionary_values['Released'],
                runtime=python_dictionary_values['Runtime'],
                genre=python_dictionary_values['Genre'],
                plot=python_dictionary_values['Plot'],
                language=python_dictionary_values['Language'])
        else:
            raise serializers.ValidationError(str(python_dictionary_values['Error']))


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)