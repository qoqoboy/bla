from django.conf.urls import url
from . import views


app_name = 'upapp'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
]
