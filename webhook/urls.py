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


#E5853GKS



# plate:1113BBB
# Make=MERCEDES BENZ
# MODEL=CLASS A

#1111AAA-REMOVE CAR

#1112ABC -REMOVE CAR TWO

#{"todo-item": {"content": "0000TST-TEST TEST", "responsible-party-id": "466639", "tags": "Video"}, "sub-task3-response": {"STATUS": "OK", "id": "22029122", "affectedTaskIds": "22029122"}}


#{'STATUS': 'OK', 'id': '22029124', 'affectedTaskIds': '22029124'} *******************************
#{'STATUS': 'OK', 'id': '22029118', 'affectedTaskIds': '22029118'} *******************************
#{'STATUS': 'OK', 'id': '22029111', 'affectedTaskIds': '22029111'} *******************************