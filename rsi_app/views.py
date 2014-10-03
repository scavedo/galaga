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
            founders = {}
        return render(request, 'rsi_app/founders_list.html', {'founders': founders})

class FounderDetail(View):
    def get(self, request, slug):
        founder = get_object_or_404(Founders, slug=slug)
        return render(request, 'rsi_app/founder_detail.html', {'founder': founder})