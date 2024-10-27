from django.http import HttpResponse
from core.models import Profile
from django.shortcuts import render


def publish(request):
    return render(request,"publish.html")
def rankings(request):
    return render(request,"Rankings.html")
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request,"Profile.html",{'profile': user_profile})                        