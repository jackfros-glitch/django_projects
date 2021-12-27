from django.shortcuts import render, redirect, get_object_or_404
from .owner import OwnerCreateView, OwnerListView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView
from .models import Ads, Comment, Fav
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateForm, CommentForm
from django.views import View
from django.http import HttpResponse

# Create your views here.

class AdsCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateForm()
        ctx = {"form":form}
        template_name = "ads/ads_form.html"
        return render(request, template_name, ctx)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)
        if form.is_valid():
            object = form.save(commit=False)
            object.owner = request.user
            object.save()
            return redirect(reverse_lazy("ads:all"))
        else:
            template_name = "ads/ads_form.html"
            ctx = {"form":form}
            return render(request, template_name, ctx)

class AdsListView(OwnerListView):
    model = Ads
    template_name ="ads/ads_list.html"

    def get(self, request):
        ads_list = Ads.objects.all()
        favorites = list()
        if request.user.is_authenticated :
            rows = request.user.favorite_ads.values('id')
            favorites = [row['id'] for row in rows]
        ctx =  {'ads_list':ads_list, 'favorites':favorites }
        return render(request, self.template_name, ctx)

class AdsDetailView(OwnerDetailView):
    model = Ads
    def get(self, request, pk):
        ad = Ads.objects.get(pk=pk)
        comment = Comment.objects.filter(ad=ad).order_by("-updated_at")
        comment_form = CommentForm()
        ctx = {"comments":comment, "comment_form":comment_form, "ads":ad }
        template_name = 'ads/ads_detail.html'
        return render(request, template_name, ctx)

class AdsUpdateView(OwnerUpdateView):
    def get(self, request, pk):
        ad = get_object_or_404(Ads, pk=pk, owner=request.user)
        form = CreateForm(instance= ad)
        ctx = {"form":form}
        template_name = "ads/ads_form.html"
        return render(request, template_name, ctx)

    def post(self, request, pk):
        ad = get_object_or_404(Ads, pk=pk, owner=request.user)
        form = CreateForm(request.POST, request.FILES or None, instance= ad)
        if not form.is_valid():
            ctx = {"form":form}
            template_name = "ads/ads_form.html"
            return render(request, template_name, ctx)
        ad = form.save(commit=False)
        ad.save()
        return redirect(reverse_lazy("ads:all"))

class AdsDeleteView(OwnerDeleteView):
    model = Ads
    success_url = reverse_lazy("ads:all")

def stream_file(request, pk):
    ad = get_object_or_404(Ads, pk = pk)
    response = HttpResponse()
    response["content-type"] = ad.content_type
    response["content-length"] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ads, pk=pk)
        comment = Comment(text=request.POST["comment"], owner=request.user, ad=ad)
        comment.save()
        return redirect(reverse("ads:ads_detail", args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model=Comment

    def get_success_url(self):
        ad = self.object.ad
        return reverse("ads:ads_detail", args=[ad.id])

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ads, pk=pk)
        fav = Fav(user=request.user, ad=ad)
        try:
            fav.save()
        except IntegrityError:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad =  get_object_or_404(Ads, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=ad).delete()
        except Fav.DoesNotExist as e:
            pass
        return HttpResponse()

