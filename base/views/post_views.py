from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, View
from django.db.models import Q
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'img')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs[
            'class'] = "px-3 py-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full border border-gray-300 sm:text-sm rounded-md"
        self.fields['body'].widget.attrs['placeholder'] = "What's up?"


class PostCreate(CreateView):
    model = Post
    template_name = 'pages/new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class PostDetail(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'


class PostList(ListView):
    model = Post
    template_name = 'pages/post_list.html'

    def get_queryset(self):
        users = self.request.user.following.all()
        return super().get_queryset().filter(Q(user__in=users) | Q(user=self.request.user)).order_by('-created_at')


class PostDelete(DeleteView):
    model = Post
    template_name = 'pages/confirm_delete.html'
    success_url = reverse_lazy('post_list')


class PostUpdate(UpdateView):
    model = Post
    template_name = 'pages/post_update.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class Like(View):
    def get(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs['pk'])
        except:
            post = Comment.objects.get(pk=kwargs['pk'])
        user = request.user
        is_liked = post.liked.filter(pk=user.pk).exists()

        if is_liked:
            post.liked.remove(user)
        else:
            post.liked.add(user)
        return redirect(request.GET.get('next'))

