
from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'^home/',views.HomeView.as_view(),name="home"),
     url(r'^$',views.IndexView.as_view(),name="index"),
     url(r'^register/$',views.RegisterView.as_view(), name='register'),
    url(r'^login/',views.loginview.as_view(),name='login'),
    url(r'^logout/',views.logoutview,name="logout")
]