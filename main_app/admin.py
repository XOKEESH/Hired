from django.contrib import admin
from .models import App, Interview, Note, Task, FollowUp, Contact, Feedback, Offer

# Register your models here.
admin.site.register(App)
admin.site.register(Interview)
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(FollowUp)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Offer)