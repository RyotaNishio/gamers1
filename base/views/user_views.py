from django.views.generic import DetailView, ListView, UpdateView, View
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from base.models import User, Post


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'img',
            'username',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs[
            'class'] = "mb-4 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"


class UserUpdate(UpdateView):
    model = User
    template_name = 'pages/user_update.html'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)


class UserDetail(DetailView):
    model = User
    template_name = "pages/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['post_set'] = Post.objects.filter(user=context['object']).order_by('-created_at')
        return context


class UserList(ListView):
    model = User
    template_name = 'pages/user_list.html'


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
