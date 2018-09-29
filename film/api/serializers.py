from rest_framework import serializers
from film.models import Movies, Comments


class MoviesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='moviesItem', read_only=True)

    class Meta:
        model = Movies
        fields = ['pk', 'title', 'year', 'rated', 'relased', 'runtime', 'genre', 'plot', 'language', 'url', ]
        read_only_fields = ['pk', 'year', 'rated', 'relased', 'runtime', 'genre', 'plot', 'language', ]

    def validate_title(self, value):
        qs = Movies.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The title must be unique")
        return value


class CommentsSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='commentsItem', read_only=True)

    class Meta:
        model = Comments
        fields = ['pk', 'movies', 'text', 'url', ]
        read_only_fields = ['pk']

