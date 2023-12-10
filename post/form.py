from django import forms
from .models import * 

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CreatePostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Post
        fields = ['category', 'title', 'description', 'is_published']

class UpdatePostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Post
        fields = ['category', 'title', 'description', 'is_published']