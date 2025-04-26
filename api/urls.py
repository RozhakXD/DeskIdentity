from django.urls import path
from api.views import UserAgentGeneratorView

urlpatterns = [
    path('generate/', UserAgentGeneratorView.as_view(), name='generate_user_agent')
]