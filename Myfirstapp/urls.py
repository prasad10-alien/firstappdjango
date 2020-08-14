from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="prasad123"),
    path('send_details/',views.send_details,name="prasad12")

]
