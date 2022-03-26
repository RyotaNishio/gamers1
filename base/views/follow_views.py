from django.views.generic import View, ListView
from ..models import User
from django.shortcuts import redirect


class FollowUnFollow(View):

    def get(self, request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        user = request.user
        is_follow = user.following.filter(pk=target_user.pk).exists()
        if is_follow:
            user.following.remove(target_user)
        else:
            user.following.add(target_user)
        return redirect(request.GET.get('next'))


class FollowingList(ListView):
    template_name = 'pages/user_list.html'

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user.following.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['list_title'] = 'Followings'
        return context


class FollowersList(ListView):
    template_name = 'pages/user_list.html'

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user.followed_by.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['list_title'] = 'Followers'
        return context
