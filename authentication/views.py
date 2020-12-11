from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, render, reverse
from django.views.generic import TemplateView, View

from .forms import LoginForm

# Create your views here.


# def login_view(request):
#     html = 'login.html'
#     form = LoginForm()
#     context = {'form': form}
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request, username=data['username'], password=data['password'])
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(request.GET.get('next',
#                                             reverse('homepage')))
#     return render(request, html, context)


class LoginView(View):

    form_class = LoginForm

    def get(self, request):
        html = 'login.html'
        form = self.form_class
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next',
                                            reverse('homepage')))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('loginpage')))
