from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password',)

    def create(self, validated_data):
        user = User.objects.create_user(username = validated_data['username'], password = validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class DataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'

    def validate(self, data):
        name = data['name']
        email = data['email']
        role = data['role']
        phone_number = data['phone_number']

        if name:
            for n in name:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'Name must contain only characters.'})


        if len(name) < 5:
            raise serializers.ValidationError({'error':'Name must be greater than 5'})

        return data





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'


        