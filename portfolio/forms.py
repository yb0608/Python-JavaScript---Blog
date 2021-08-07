from django import forms
from .models import Project, Category, Comment

categories = Category.objects.all().values_list('category', 'category')
categories_list = []

for category in categories:
    categories_list.append(category)


class ShareForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'author', 'category', 'content', 'summary', 'image')

        widgets = {
            'title':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'New Title'
            }),
            'author':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'currentUser',
                    'type': 'hidden'
                }),
            'category':
            forms.Select(choices=categories_list,
                         attrs={'class': 'form-control'}),
            'content':
            forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "New Content"
            }),
            'summary':
            forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Summary"
            }),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'category', 'content', 'summary', 'image')

        widgets = {
            'title':
            forms.TextInput(attrs={'class': 'form-control'}),
            'category':
            forms.Select(choices=categories_list,
                         attrs={'class': 'form-control'}),
            'content':
            forms.Textarea(attrs={'class': 'form-control'}),
            'summary':
            forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter', 'content')

        widgets = {
            'commenter':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'currentUser',
                    'type': 'hidden'
                }),
            'content':
            forms.Textarea(attrs={'class': 'form-control'}),
        }
