from django.shortcuts import render

# Create your views here.
def baking(request):
    return render(request, "baking.html")