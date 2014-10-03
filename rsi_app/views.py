from django.shortcuts import render, get_object_or_404
from rsi_app.models import Founders
from django.views.generic import View

# Create your views here.
def index(request):
    return render(request, 'rsi_app/index.html')\

class FoundersList(View):
    def get(self, request):
        try:
            founders = Founders.objects.all()
        except:
            return render(request, 'rsi_app/founders_list.html', {'error': 'No founders found.'})
        return render(request, 'rsi_app/founders_list.html', {'founders': founders})

class FounderDetail(View):
    def get(self, request, slug):
        founder = get_object_or_404(Founders, slug=slug)
        try:
            founders = Founders.objects.all()
        except:
            return render(request, 'rsi_app/founders_list.html', {'error': 'No founders found.'})

        return render(request, 'rsi_app/founders_detail.html', {'founder': founder, 'founders': founders})

def ghost_stories(request):
    return render(request, 'rsi_app/ghost_stories.html')

class Event(View):
    def get(self, request):
        return render(request, 'rsi_app/event.html')

def history(request):
    return render(request, 'rsi_app/history.html')
