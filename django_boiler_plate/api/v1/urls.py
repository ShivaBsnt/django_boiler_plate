from django.urls import include, path

urlpatterns = [
    path('user/', include('django_boiler_plate.user.api.v1.urls')),
]
