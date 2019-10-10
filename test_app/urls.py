from django.urls import path
from test_app import views

urlpatterns = [
    
    path('ha/',views.hi),
    path('date/',views.date_t),
    path('one/',views.o),
    path('a/',views.n)

]