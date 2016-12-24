from django.conf.urls import url
from .views import AutoDocsView

urlpatterns = [
    url(r'^docs/', AutoDocsView.as_view()),
]
