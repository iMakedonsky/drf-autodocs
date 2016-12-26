from django.conf.urls import url
from .views import TreeView

urlpatterns = [
    url(r'^docs/', TreeView.as_view(), name='api-tree'),
]
