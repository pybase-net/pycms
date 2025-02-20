
from django.urls import path
from .views import PageView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('pages/', PageView.as_view(), name='pages'),
]
