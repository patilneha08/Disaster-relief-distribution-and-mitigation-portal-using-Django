from django.urls import path
from . import views

urlpatterns=[
    path('index',views.index,name="index"),
    path('about',views.about,name="about"),
    path('floods',views.floods,name="floods"),
    path('droughts',views.droughts,name="droughts"),
    path('cyclones',views.cyclones,name="cyclones"),
    path('earthquakes',views.earthquakes,name="earthquakes"),
    path('landslides',views.landslides,name="landslides"),
    path('pandemic',views.pandemic,name="pandemic"),
    path('donate',views.donate,name="donate"),
    path('volunteer',views.volunteer,name="volunteer"),
    path('help',views.help,name="help"),
    path('contact',views.contact,name="contact"),
    path('success',views.success,name="success"),
    path("<int:ngo_id>/selectngo",views.selectngo,name="selectngo"),
    path('sos',views.sos,name="sos"),
]
