from django.urls import path
from .views import SignUpView , UserEditView
from.forms import UserChangeForm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]