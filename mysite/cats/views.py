from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from cats.models import Cat, Breed
from .forms import CatForm, BreedForm
# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cat_list = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        ctx = {"cat_list":cat_list, "breed_count":breed_count}
        template_name = "cats/cat_list.html"
        return render(request, template_name, ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        ctx = {"breed_list":breed_list}
        template_name = 'cats/breed_list.html'
        return render(request, template_name, ctx)

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, View):
    template_name = 'cats/cat_form.html'

    def get(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        form = CatForm(instance=cat)
        ctx = {'form':form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('cats:all'))
        else:
            ctx = {'form':form}
            return render(request, self.template_name, ctx)



class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, View):
    template_name = 'cats/cat_confirm_delete.html'
    def get(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        ctx = {'cat':cat}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        cat.delete()
        return redirect(reverse_lazy('cats:all'))

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
