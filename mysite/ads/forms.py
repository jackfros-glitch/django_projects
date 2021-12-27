from django import forms
from .models import Ads, Comment
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import naturalsize

class CreateForm(forms.ModelForm):
    max_upload_limit = 2*1024*1024
    max_upload_limit_text = naturalsize(max_upload_limit)


    picture = forms.FileField(required=False, label="File to Upload <= "+ max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Ads
        fields = ['title','text', 'price', 'picture']

    #validate the size of the uploaded picture file
    def clean(self):
        #get the cleaned data
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None: return
        if len(pic) > self.max_upload_limit:
            self.adderror('picture', 'File must be < ' + self.max_upload_limit_text +'bytes')

    #Convert upload file object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        f = instance.picture
        if isinstance(f, InMemoryUploadedFile):
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr

        if commit:
            instance.save()

        return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)


