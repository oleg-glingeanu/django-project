from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.views import generic
from .forms import CustomUserCreationForm , CustomUserChangeForm, EditProfileForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
