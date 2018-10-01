from rest_framework.test import APITestCase
from film.models import Movies, Comments
from rest_framework import status
import json, requests
from rest_framework.reverse import reverse as api_reverse

# automated
# new / blank db

class MovieCommentAPITestCase(APITestCase):
    def setUp(self):
        movieTest = Movies.objects.create(title='Title Test',
                                      year='2000',
                                      rated='No',
                                      relased='31 December 1972',
                                      runtime='25 min',
                                      genre='Drama',
                                      plot='Test movie about test.',
                                      language='Polish'
                                      )
        commentTest = Comments.objects.create(text='Test komentarz testowy.',
                                          movies=movieTest, )

    def test_single_movie(self):
        movie_count = Movies.objects.count()
        self.assertEqual(movie_count, 1)

    def test_single_comment(self):
        comment_count = Comments.objects.count()
        self.assertEqual(comment_count, 1)

    def test_get_list_movies(self):
        data = {}
        url = api_reverse("moviesList")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    def test_get_list_comments(self):
        data = {}
        url = api_reverse("commentsList")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    def test_post_item_movies(self):
        response = requests.get("http://www.omdbapi.com/?apikey=e914fe0d&t=" + 'Test')
        python_dictionary_values = json.loads(response.text)
        data = {"title": 'Test',
                "year": python_dictionary_values['Year'],
                "rated": python_dictionary_values['Rated'],
                "relased": python_dictionary_values['Released'],
                "runtime": python_dictionary_values['Runtime'],
                "genre": python_dictionary_values['Genre'],
                "plot": python_dictionary_values['Plot'],
                "language": python_dictionary_values['Language']}
        url = api_reverse("moviesList")
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print(response.data)

    def test_get_item_movies(self):
        data = {}
        movie = Movies.objects.first()
        url = api_reverse("moviesItem", args=[movie.pk])
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item_movies(self):
        data = {}
        movie = Movies.objects.first()
        url = api_reverse("moviesItem", args=[movie.pk])
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_post_list_comments(self):
        movie = Movies.objects.first()
        data = {"text": "Tekst testowy kometarz", "movies": movie.pk}
        url = api_reverse("commentsList")
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print(response.data)

    def test_get_item_comments(self):
        data = {}
        comment = Comments.objects.first()
        url = api_reverse("commentsItem", args=[comment.pk])
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item_comments(self):
        movie = Movies.objects.first()
        data = {"text": "elo", "movies": movie.pk}
        comment = Comments.objects.first()
        url = api_reverse("commentsItem", args=[comment.pk])
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item_comments(self):
        data = {}
        comment = Comments.objects.first()
        url = api_reverse("commentsItem", args=[comment.pk])
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)