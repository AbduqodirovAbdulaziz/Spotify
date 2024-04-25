from rest_framework import serializers
from .models import *


class DavlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davlat
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class TransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"
