from django.urls import path
from . import views


urlpatterns = [

    path('create-task/',views.create_taask,name='create_taask'),

    path('reserved/',views.reserved,name='reserved'),

    path('available/',views.available,name="available"),

    path('delivered/',views.delivered,name="delivered"),

    path('', views.action, name="action")

]

# http://localhost:8000/?action=create&plate=E2323FRW&make=AUDI&model=RS4

# http://localhost:8000/?action=reserved&plate=E2323FRW&make=AUDI&model=RS4

# http://localhost:8000/?action=available&plate=E2323FRW&make=AUDI&model=RS4

# http://localhost:8000/?action=delivered&plate=E2323FRW


#################

#http://164.92.144.88:8004/?action=create&plate=E2323FRW&make=AUDI&model=RS4

#http://164.92.144.88:8004/?action=reserved&plate=E2323FRW&make=AUDI&model=RS4

#http://164.92.144.88:8004/?action=available&plate=E2323FRW&make=AUDI&model=RS4

#http://164.92.144.88:8004/?action=delivered&plate=E2323FRW
