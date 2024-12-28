from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class App:
    def __init__(app, company, title, date, description):
        app.company = company
        app.title = title
        app.date = date
        app.description = description

apps = [
    App('Shopify', 'Software Engineer', '12/27/24', 'A job that pays very well.'),
    App('Playstation', 'UX Designer', '12/23/24', 'A job that pays very well.')
]   

def app_index(request):
    return render(request, 'apps/index.html', {'apps': apps})
