from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('transfer/',views.modelview,name='modelview'),
    path('download/',views.download,name='download')
]
