from block_app.models import User, Post
from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp_class'}),
            'email': forms.EmailInput(attrs={'class': 'inp_class'}),
            'password': forms.PasswordInput(attrs={'class': 'inp_class'})
        }
        labels = {
            'username': 'Введите имя',
            'email': 'Введите эл. почта',
            'password': 'Введите пароль'
        }
        error_messages = {
            'username': {
                'unique': 'Это имя уже занято'
            }
        }


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('date_posted',)
        widgets = {
            'author': forms.Select(attrs={'class': 'author'}),
            'title': forms.TextInput(attrs={'class': 'title'}),
            'content': forms.Textarea(attrs={'class': 'content'})
        }
        labels = {
            'author': 'Автор',
            'title': 'Заголовок',
            'content': 'Текст'
        }
