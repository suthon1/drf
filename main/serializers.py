from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Women, Car


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"



class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    description = serializers.CharField()

"""
here we created serializers

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    time_created = serializers.DateTimeField(read_only=True)
    time_updated = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_created = validated_data.get('time_created', instance.time_created)
        instance.time_updated = validated_data.get('time_updated', instance.time_updated)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance
"""
"""
class WomenModel:  #  here i used this model class just for education and for examples
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()


def encode():
    model = WomenModel('anjelina ,', 'Anjelina')
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep="\n")
    json = JSONRenderer().render(model_sr.data)
    print(json)"""
