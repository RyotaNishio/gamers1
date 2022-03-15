from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from base.models import User


class UserDetail(DetailView):
    model = User
    template_name = "pages/user_detail.html"


class UserList(ListView):
    model = User
    template_name = 'pages/user_list.html'



