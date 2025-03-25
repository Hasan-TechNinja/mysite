from rest_framework import serializers
from todo.models import Database

class DatabaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = "__all__"
        