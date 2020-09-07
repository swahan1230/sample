from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path(r'transfer/(?P<value>\d+)/$',views.modelview,name='modelview'),
    path('download/',views.download,name='download'),
    path('home/',views.returnhome,name='returnhome'),
    path('about/',views.about,name='about'),
    path('feedback/',views.feedback,name='feedback'),
    path('submit/',views.submit,name='submit'),
]
