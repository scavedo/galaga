from django.shortcuts import render, get_object_or_404
from rsi_app.models import Founders

# Create your views here.
def index(request):
    return render(request, 'rsi_app/index.html')\

def founders_list(request):
    founders = Founders.objects.all()
    return render(request, 'rsi_app/founders_list.html', {'founders': founders})

def founder_detail(request, slug):
    founder = get_object_or_404(Founders, slug=slug)
    return render(request, 'rsi_app/founder_detail.html', {'founder': founder})

