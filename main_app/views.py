from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import App, Interview, Note, Task, FollowUp, Contact, Feedback, Offer
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InterviewForm, NoteForm, TaskForm, FollowUpForm, ContactForm, FeedbackForm, OfferForm


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
    app = get_object_or_404(App, id=app_id)
    
    interview_form = InterviewForm()
    note_form = NoteForm()
    task_form = TaskForm()
    followup_form = FollowUpForm()
    contact_form = ContactForm()
    feedback_form = FeedbackForm()
    offer_form = OfferForm()
    
    return render(request, 'apps/detail.html', {
        'app': app,
        'interview_form': interview_form,
        'note_form': note_form,
        'task_form': task_form,
        'followup_form': followup_form,
        'contact_form': contact_form,
        'feedback_form': feedback_form,
        'offer_form': offer_form
    })

def add_interview(request, app_id):
    form = InterviewForm(request.POST)
    if form.is_valid():
        new_interview = form.save(commit=False)
        new_interview.app_id = app_id
        new_interview.save()
    return redirect('app-detail', app_id=app_id)

def add_note(request, app_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.app_id = app_id
        new_note.save()
    return redirect('app-detail', app_id=app_id)

def add_task(request, app_id):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.app_id = app_id
        new_task.save()
    return redirect('app-detail', app_id=app_id)

def add_followUp(request, app_id):
    form = FollowUpForm(request.POST)
    if form.is_valid():
        new_followup = form.save(commit=False)
        new_followup.app_id = app_id
        new_followup.save()
    return redirect('app-detail', app_id=app_id)

def add_contact(request, app_id):
    form = ContactForm(request.POST)
    if form.is_valid():
        new_contact = form.save(commit=False)
        new_contact.app_id = app_id
        new_contact.save()
    return redirect('app-detail', app_id=app_id)

def add_feedback(request, app_id):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        new_feedback = form.save(commit=False)
        new_feedback.app_id = app_id
        new_feedback.save()
    return redirect('app-detail', app_id=app_id)

def add_offer(request, app_id):
    form = OfferForm(request.POST)
    if form.is_valid():
        new_offer = form.save(commit=False)
        new_offer.app_id = app_id
        new_offer.save()
    return redirect('app-detail', app_id=app_id)

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