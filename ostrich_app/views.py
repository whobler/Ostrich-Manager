from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from ostrich_app.models import OstrichBreeders, EggsBabies
from .serializers import OstrichBreedersSerializer, OstrichEggsBabiesSerializer
from .forms import AddBreederForm


class HomePage(View):
    def get(self, request):
        return render(request, "index.html")


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return render(request, "logout.html")


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
            return redirect(reverse('home'))
        return HttpResponse("Username %s not found." % username)


class GetBreeder(LoginRequiredMixin, APIView):
    login_url = '/login/'

    def get_breeder(self, pk):
        try:
            return OstrichBreeders.objects.get(pk=pk)
        except OstrichBreeders.DoesNotExist:
            raise Http404

    def get(self, request, id):
        breeder = self.get_breeder(id)
        serializer = OstrichBreedersSerializer(breeder, context={'request': request})
        return Response(serializer.data)


class GetBreeders(LoginRequiredMixin, APIView):
    login_url = '/login/'

    def get(self, request):
        breeders = OstrichBreeders.objects.all()
        serializer = OstrichBreedersSerializer(breeders, many=True, context={'request': request})
        return Response(serializer.data)


class Breeders(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        ctx = {
        }
        return render(request, 'breeders.html', ctx)


class ShowBreeders(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        breeders = OstrichBreeders.objects.all()
        ctx = {
            'breeders': breeders,
        }
        return render(request, 'show_breeders.html', ctx)


class AddBreeder(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = AddBreederForm()
        ctx = {
            'form': form,
            'pre_name': 'Add ',
        }
        return render(request, "add_breeder.html", ctx)

    def post(self, request):
        form = AddBreederForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        return HttpResponse('not valid')


class ModifyBreeder(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        breeder_to_mod = OstrichBreeders.objects.get(pk=id)
        form = AddBreederForm(instance=breeder_to_mod)
        ctx = {
            'form': form,
            'id': id,
            'pre_name': 'Modify ',
        }
        return render(request, "add_breeder.html", ctx)

    def post(self, request, id):
        breeder_to_mod = OstrichBreeders.objects.get(pk=id)
        form = AddBreederForm(request.POST, instance=breeder_to_mod)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        return HttpResponse('not valid')


class GetEggsBaby(LoginRequiredMixin, APIView):
    login_url = '/login/'

    def get_baby(self, pk):
        try:
            return EggsBabies.objects.get(pk=pk)
        except EggsBabies.DoesNotExist:
            raise Http404

    def get(self, request, id):
        baby = self.get_baby(id)
        serializer = OstrichEggsBabiesSerializer(baby, context={'request': request})
        return Response(serializer.data)


class GetEggsBabies(LoginRequiredMixin, APIView):
    login_url = '/login/'

    def get(self, request):
        babies = EggsBabies.objects.all()
        ctx = {
            'babies': babies,
        }
        return render(request, 'show_babies.html', ctx)


class ShowEggsBabies(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        eggs_babies = EggsBabies.objects.all()
        ctx = {
            'eggs_babies': eggs_babies,
        }
        return render(request, 'eggs_babies.html', ctx)


class ShowWarehouse(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        eggs_babies = EggsBabies.objects.all()
        ctx = {
            'eggs_babies': eggs_babies,
        }
        return render(request, 'warehouse.html', ctx)


class ShowSoldBirds(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        eggs_babies = EggsBabies.objects.all()
        ctx = {
            'eggs_babies': eggs_babies,
        }
        return render(request, 'sold_birds.html', ctx)


class ShowBudget(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        eggs_babies = EggsBabies.objects.all()
        ctx = {
            'eggs_babies': eggs_babies,
        }
        return render(request, 'budget.html', ctx)


class ShowSeasonsStatistics(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        eggs_babies = EggsBabies.objects.all()
        ctx = {
            'eggs_babies': eggs_babies,
        }
        return render(request, 'seasons_statistics.html', ctx)
