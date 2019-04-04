from django.shortcuts import render

# Create your views here.
def specialoccasion(request):
    return render(request, "specialoccasion.html")