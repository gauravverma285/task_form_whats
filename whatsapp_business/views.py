from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from app.models import Job
from .serializers import JobSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all().values('first_name')
    first_name = queryset.values('first_name')
    serializer_class = JobSerializer


class WhatsAppWrapper(APIView):
    
    def post(self, request):
        
        to = request.data.get('to', '')
        template = request.data.get('template', {}).get('name', '')
        Authorization = request.headers.get('Authorization')
        phone_id = request.headers.get('phone-Id')
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json'
        }

        if not to and not template:
            message = "Recipients number and template not provided."
            return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)

        if not Authorization:
            message = "Access-token not provided or not valid."
            return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not phone_id:
            message = "Phone-number id not provided or not valid."
            return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)
        
        url = f'https://graph.facebook.com/v15.0/{phone_id}/messages'
        data = {
            'messaging_product': 'whatsapp',
            'to': to,
            'type': 'template',
            'template': {
                'name': template,
                'language': {'code': 'en_US'}
            }
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == status.HTTP_200_OK:
            message="Whatsapp message is send succefully."
            return Response({'message':message}, status=status.HTTP_200_OK)
        else:
            message = "Failed to send whatsapp message."
            return Response({'message':message}, status=status.HTTP_400_BAD_REQUEST)

