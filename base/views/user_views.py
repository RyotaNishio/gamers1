from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.urls import reverse_lazy
from base.models import User, Post, Profile


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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'bio')
        widgets = {'birthday': forms.SelectDateWidget(years=[x for x in range(1980, 2022)])}

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs[
            'class'] = "px-3 py-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full border border-gray-300 sm:text-sm rounded-md"
        self.fields['bio'].widget.attrs['placeholder'] = "bio"
        self.fields['birthday'].widget.attrs[
            'class'] = "mr-1 px-3 py-2 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block border border-gray-300 sm:text-sm rounded-md"


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
        context['birthday'] = context['user'].profile.birthday
        context['bio'] = context['user'].profile.bio
        return context


class UserLikes(DetailView):
    model = User
    template_name = "pages/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['object']
        context['post_set'] = user.favorited.all().order_by('-created_at')
        context['birthday'] = context['user'].profile.birthday
        context['bio'] = context['user'].profile.bio
        return context


class UserList(ListView):
    model = User
    template_name = 'pages/user_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserList, self).get_context_data()
        context['list_title'] = 'Users'
        return context


class ProfileUpdate(UpdateView):
    template_name = 'pages/profile.html'
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.kwargs['pk']})

