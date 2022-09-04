from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.db.models import F
from django.views.generic import ListView,FormView,DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from .forms import *






class MyPasswordChangeView(PasswordChangeView):
    template_name ='password-change.html'
    success_url = reverse_lazy('password-change-done-view')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name ='password-reset-done.html'



class WorkExperienceListView(ListView):
    model = WorkExperience
    template_name = 'index.html'
    context_object_name = 'works'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['langs'] = Lang.objects.all()
        context['kens'] = Ken.objects.all()
        context['percents'] = Percents.objects.all()
        context['socials'] = Social.objects.all()
        return context



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')



class Add_WorkExperienceView(CreateView):
    form_class = UserAdd_WorkExperienceForm
    template_name = 'Add Work Experience.html'
    success_url = reverse_lazy('home')
    raise_exception = True

def add_workExperience(request):
    if request.method == 'POST':
        form = UserAdd_WorkExperienceForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserAdd_WorkExperienceForm()
    return render(request, 'Add Work Experience.html', {'form': form})

