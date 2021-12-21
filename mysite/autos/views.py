from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Auto, Make
from .forms import AutoForm, MakeForm
# Create your views here.

class MainView(LoginRequiredMixin, View):

    def get(self, request):
        auto_list = Auto.objects.all()
        make = Make.objects.all().count()

        ctx = {'auto_list' : auto_list, 'make_count' : make}
        template_name = 'autos/auto_list.html'
        return render(request, template_name, ctx)

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeView(LoginRequiredMixin, View):

    def get(self, request):
        make_list = Make.objects.all()
        ctx = {'make_list':make_list}
        template_name = 'autos/make_list.html'
        return render(request, template_name, ctx)

class MakeCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = MakeForm()
        ctx = {'form':form}
        template_name = 'autos/make_form.html'
        return render(request, template_name, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/autos')
        else:
            error_message = "You did not fill in a valid make.please fill in a valid make"
            ctx = {'form':form, 'error_message':error_message}
            template_name = 'autos/make_form.html'
            return render(request, template_name, ctx)

class AutoUpdate(LoginRequiredMixin, View):
    template_name = 'autos/auto_form.html'
    update = True

    def get(self, request, pk):
        auto = get_object_or_404(Auto, pk=pk)
        form = AutoForm(instance=auto)
        ctx = {'form':form , 'update':self.update}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        auto = get_object_or_404(Auto, pk=pk)
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('autos:all'))
        else:
            ctx = {'form':form, 'update': self.update}
            return render(request, self.template, ctx)

class MakeUpdate(LoginRequiredMixin, View):
    template_name = 'autos/make_form.html'
    def get(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        form = MakeForm(instance=make)
        ctx = { 'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        make = get_object_or_404(Make, pk = pk)
        form = MakeForm(request.POST, instance=make)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('autos:all'))
        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy('autos:all')
    fields = '__all__'


class MakeDelete(LoginRequiredMixin, View):
    template_name = 'autos/make_confirm_delete.html'
    def get(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        ctx = { 'make': make}
        return render(request, self.template_name, ctx)

    def post(self, request,pk):
        make = get_object_or_404(Make, pk=pk)
        make.delete()
        return redirect(reverse_lazy('autos:all'))






