from django.contrib import admin
from django.urls import path, include
from mainApp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('davlats', DavlatModelViewSet)
router.register('clubs', ClubsModelViewSet)
router.register('players', PlayersModelViewSet)
router.register('transfers', TransfersModelViewSet)
router.register(r'yoshlar',U_20_PlayersModelViewSet,basename='u20_players')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('davlatlar/', DavlatlarApiView.as_view()),
    path('clublar/', ClublarApiView.as_view()),
    path('playerlar/', ClublarApiView.as_view()),
    path('transferlar/', ClublarApiView.as_view()),

]
