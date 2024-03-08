from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from django.contrib.auth import authenticate

from authentication.serializers import RegisterSerializer


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return response.Response(serializer.data, status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_200_OK)
    
