from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class HomePageView(View):
    def get(self, request):
        context = {}
        return render(request, 'index-4.html', context)