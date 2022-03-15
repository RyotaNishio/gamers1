from django.views.generic import DetailView, ListView
from base.models import User


class UserView(DetailView):
    model = User
    template_name = "pages/user.html"


class UserListView(ListView):
    model = User
    template_name = 'pages/user_list.html'
