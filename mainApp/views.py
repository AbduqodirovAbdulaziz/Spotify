from django.shortcuts import render
from datetime import date
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class DavlatModelViewSet(ModelViewSet):
    queryset = Davlat.objects.all()
    serializer_class = DavlatSerializer


class ClubsModelViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    @action(detail=True, methods=['get'])
    def players(self, request, pk):
        club = self.get_object()
        oyinchilar = Player.objects.filter(club=club)
        serializer = PlayerSerializer(oyinchilar, many=True)
        return Response(serializer.data)


class PlayersModelViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class U_20_PlayersModelViewSet(ModelViewSet):
    hozirgi_sana = str(date.today())
    yil = int(hozirgi_sana[:4]) - 20
    yangi_sana = hozirgi_sana.replace(hozirgi_sana[:4], str(yil))
    queryset = Player.objects.filter(t_yil__gt=yangi_sana)
    serializer_class = PlayerSerializer


class TransfersModelViewSet(ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializers

    # @action(detail=True, methods=['get'])
    # def records(self, request):
    #     narx=self.get_object()
    #     transfers = Transfer.objects.all().order_by(narx)
    #     serializer = TransferSerializers(transfers, many=True)
    #     return Response(serializer.data)


# =============================================================================

class DavlatlarApiView(APIView):
    def get(self, request):
        davlatlar = Davlat.objects.all()
        serializer = DavlatSerializer(davlatlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        davlat = request.data
        serializer = DavlatSerializer(data=davlat)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'create_data': serializer.data})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ClublarApiView(APIView):
    def get(self, request):
        clublar = Club.objects.all()
        serializer = ClubSerializer(clublar, many=True)
        return Response(serializer.data)

    def post(self, request):
        club = request.data
        serializer = ClubSerializer(data=club)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayersApiView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        player = request.data
        serializer = PlayerSerializer(data=player)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransfersApiView(APIView):
    def get(self, request):
        transfers = Transfer.objects.all()
        serializer = TransferSerializers(transfers, many=True)
        return Response(serializer.data)

    def post(self, request):
        transfer = request.data
        serializer = TransferSerializers(data=transfer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
