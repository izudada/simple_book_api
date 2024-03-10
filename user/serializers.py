from rest_framework import serializers

from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',) 
