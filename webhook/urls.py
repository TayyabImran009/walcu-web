from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    path('create-task/<str:plate>/<str:make>/<str:model>/',views.create_taask,name='create_taask'),

    path('reserved/<str:plate>/',views.reserved,name='reserved'),

    path('available/<str:plate>/',views.available,name="available"),

    path('delivered/<str:plate>/',views.delivered,name="delivered"),

]


# http://localhost:8000/create-task/E789LEP/Audi/RS9/

# http://localhost:8000/reserved/E789LEP/

# http://localhost:8000/available/E789LEP/

# http://localhost:8000/delivered/E789LEP/