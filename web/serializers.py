from rest_framework import serializers
from django.contrib.auth.models import User
from web.models import Bookshelf, Author

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BookshelfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['name', 'assigned_status', ]
