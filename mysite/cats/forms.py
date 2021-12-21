from .models import Cat, Breed
from django.forms import ModelForm

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'

class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'
