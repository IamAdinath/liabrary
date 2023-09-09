from django.urls import include, path
from rest_framework import routers
from web.views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()
# router.register(r'users', views.UserView)
# router.register('swagger', schema_view)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', UserView.as_view()),
    path('books/', Books.as_view())
]
