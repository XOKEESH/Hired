from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import App
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')   

@login_required
def app_index(request):
    apps = App.objects.filter(user=request.user)
    return render(request, 'apps/index.html', {'apps': apps})

@login_required
def app_detail(request, app_id):
    app = App.objects.get(id=app_id)
    return render(request, 'apps/detail.html', {'app': app})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class AppCreate(LoginRequiredMixin, CreateView):
    model = App
    fields = [
        'job_title', 
        'company_name', 
        'status', 
        'job_link', 
        'job_description', 
        'notes', 
        'attachments'
    ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    success_url = '/applications/'
 
class AppUpdate(LoginRequiredMixin, UpdateView):
    model = App
    fields = ['job_link', 'job_description', 'notes', 'attachments']

class AppDelete(LoginRequiredMixin, DeleteView):
    model = App
    success_url = '/apps/'