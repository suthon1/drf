from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.forms import model_to_dict

from .serializers import WomenSerializer, CarSerializer
from .models import Women, Car


class WomenList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPiView(APIView):
    def get(self, request):
        womens = Women.objects.all()
        return Response({'posts': WomenSerializer(womens, many=True).data})

    def post(self, request):
        serializers = WomenSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        # new_post = Women.objects.create(
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )
        return Response({'post': serializers.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Method Put not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class CarApiView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        return Response({'car list': CarSerializer(cars, many=True).data})

    def post(self, request):
        serializers = CarSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        new_cars = Car.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'car post': CarSerializer(new_cars).data})























"""


here also we just test our example

class WomenApiView(APIView):

    def get(self, request):
        women_list = Women.objects.all().values()
        return Response({'get_women_list': list(women_list)})

    def post(self, request):
        post_ = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_)})
"""