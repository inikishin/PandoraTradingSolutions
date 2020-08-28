from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(
        label="Имя",
        widget=forms.TextInput
    )

    email = forms.EmailField(
        widget=forms.EmailInput
    )

    subject = forms.CharField(
        label="Тема",
        widget=forms.TextInput
    )

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea
    )