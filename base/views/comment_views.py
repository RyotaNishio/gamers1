from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from ..models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs[
            'class'] = "px-3 py-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full border border-gray-300 sm:text-sm rounded-md"
        self.fields['body'].widget.attrs['placeholder'] = "Reply to {{ self.post.user.username }}"


class CommentCreate(CreateView):
    model = Comment
    template_name = 'pages/comment_form.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdate(UpdateView):
    model = Comment
    template_name = 'pages/comment_form.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'pages/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})