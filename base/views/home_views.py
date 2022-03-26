from django.views.generic import ListView
from ..models import Post


class Top(ListView):
    model = Post
    template_name = 'pages/post_list.html'

    def get_queryset(self):
        return super(Top, self).get_queryset().order_by('-created_at')
