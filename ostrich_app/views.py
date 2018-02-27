from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response

from ostrich_app.models import OstrichBreeders
from .serializers import OstrichBreedersSerializer


def logout_user(request):
    logout(request)
    return HttpResponse("Succesfully logged out.")


class ShowBreeders(APIView, LoginRequiredMixin):
    login_url = '/login/'

    def get(self, request):
        breeders = OstrichBreeders.objects.all()
        serializer = OstrichBreedersSerializer(breeders, many=True, context={'request': request})
        return Response(serializer.data)


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            url = request.GET.get("next")
            if url:
                return redirect(url)
            return HttpResponse("Logged in.")
        return HttpResponse("ERROR %s %s" % (username, password))


