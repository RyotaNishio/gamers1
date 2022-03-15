from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Top(LoginRequiredMixin, TemplateView):
    template_name = 'pages/top.html'
    login_url = '/login/'
