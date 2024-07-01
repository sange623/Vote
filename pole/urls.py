from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewset import UserViewset,PoleHaveOptionsViewset,PoleTableViewset,VoteViewset


router = DefaultRouter()
router.register(r'user',UserViewset,basename='UserViewset')
router.register(r'polehaveoptions',PoleHaveOptionsViewset,basename='PoleHaveOptionsViewset')
router.register(r'poletable',PoleTableViewset,basename='PoleTableViewset')
router.register(r'vote',VoteViewset,basename='VoteViewset')


urlpatterns = [
    path('',include(router.urls)),
]
