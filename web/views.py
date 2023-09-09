import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import UserSerializer, BookshelfSerializer
from django.contrib.auth.models import User
from web.models import Bookshelf, Rent, Author
import json


class UserView(APIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format="json"):
        try:
            serialized_data = serialize(format, self.queryset.all())
            serialized_data = json.loads(serialized_data)
            return Response(serialized_data)
        except Exception as e:
            return Response({"message": f"Error is here is the {e}"})


class Books(APIView):
    queryset = Bookshelf.objects.all().order_by('name')
    serializer_class = BookshelfSerializer

    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format="json"):
        try:
            serialized_data = serialize(format, self.queryset.all())
            serialized_data = json.loads(serialized_data)
            return Response(serialized_data)
        except Exception as e:
            return Response({"message": f"Error is here is the {e}"})

    def post(self, request, format="json"):
        try:
            serialized_data = serialize(format, self.queryset.all())
            serialized_data = json.loads(serialized_data)
            data = request.POST
            Bookshelf.objects.create(
                name=request.POST.get('name'),
                assigned_status=bool(request.POST.get('assigned_status')))
            return Response(data)
        except Exception as e:
            return Response({"message": f"Error is here is the {e}"})