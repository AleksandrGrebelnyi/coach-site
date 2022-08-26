from django import forms
from .models import UserReservation
from django.core.validators import RegexValidator

# create form for customer to collect customer data


class CustomerContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Ваше имя',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
        })
    )

    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Ваш Email',
        'data-rule': 'email',
        'pattern': '(^[A-Za-z0-9]+[\w_]+.[\w_]+@[0-9A-Za-z]+\.[a-z]{2,7}$)',
        'data-msg': 'Please enter a valid email',

    }))

    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'phone',
        'id': 'phone',
        'placeholder': 'Ваш телефон (+ код страны): +XXXXXXXXXXXX',
        'data-rule': 'minlen:4',
        'pattern': '^((\+?\d{3}[- .]?)\d{7,13}$)',
        'data-msg': 'Please enter in format +XXXXXXXXXXXX',
    }))

    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'type': 'number',
        'class': 'form-control',
        'name': 'message',
        'rows': '5',
        'placeholder': 'Напишите какой тариф вы выбрали (марафон похудения или индивидуальное ведение), а так же '
                       'можете задать интересующие вас вопросы и оставить ваши контакты из социальных сетей '
                       '(instagram или facebook или телеграм)',
        'required': 'required',
    }))

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'message')