from django import forms
from .models import Interview, Note, Task, FollowUp, Contact, Feedback, Offer

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['date', 'type', 'notes']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['date', 'content']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['due_date', 'task_description']
        widgets = {
            'due_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ['date', 'description']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_date', 'contact_method', 'contact_notes']
        widgets = {
            'contact_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',  # Add the bootstrap form control class for styling
                    'placeholder': 'Select a date',
                    'type': 'date',
                    'style': 'max-width: 250px;'  # You can adjust this width as needed
                }
            ),
            'contact_method': forms.Select(
                attrs={
                    'class': 'form-control',  # Add the bootstrap form control class for styling
                    'style': 'max-width: 250px;'  # Similar to the date input field
                }
            ),
            'contact_notes': forms.Textarea(
                attrs={
                    'class': 'form-control',  # Add the bootstrap form control class for styling
                    'placeholder': 'Enter contact notes',
                    'rows': 4,  # Adjust the number of rows for the textarea
                    'style': 'max-width: 500px;'  # Adjust width for textarea
                }
            ),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments']

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['offer_details', 'offer_date', 'salary', 'benefits', 'start_date', 'accepted']
        widgets = {
            'offer_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
