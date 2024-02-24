# from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class Hello(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        return Response(
            data={
                "successMessage": "123",
                "errorMessage": None,
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
