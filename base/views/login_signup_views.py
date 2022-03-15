from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy

User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs[
                'class'] = "appearance-none rounded-none relative block w-full px-3 py-2 border " \
                           "border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none " \
                           "focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            field.widget.attrs['type'] = field.label
            field.widget.attrs['name'] = field.label


class Signup(CreateView):
    form_class = SignupForm
    template_name = 'pages/login_signup.html'
    success_url = reverse_lazy('top')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs[
                'class'] = "appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300" \
                           " placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500" \
                           " focus:border-indigo-500 focus:z-10 sm:text-sm"
            field.widget.attrs['type'] = field.label
            field.widget.attrs['name'] = field.label


class Login(LoginView):
    form_class = LoginForm
    template_name = 'pages/login_signup.html'

    def form_valid(self, form):
        messages.success(self.request, 'You are successfully login.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'You are missed login.')
        return super().form_invalid(form)


class Logout(LogoutView):
    template_name = 'pages/login_signup.html'


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'img',
            'username',
            'email'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs[
            'class'] = "mb-4 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
        # self.fields['img'].widget.attrs['class'] =
        self.fields['email'].widget.attrs[
            'class'] = "mb-5 appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"


class UserUpdate(UpdateView):
    model = User
    template_name = 'pages/user_update.html'
    success_url = reverse_lazy('user_detail')
    form_class = UserUpdateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)
