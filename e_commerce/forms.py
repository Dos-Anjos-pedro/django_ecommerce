from django import forms

class ContactForm(forms.Form):
    Nome_Completo = forms.CharField(
        error_messages={'required': 'Obrigatorio o Preenchimento do Nome!'},
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email= forms.EmailField(
        error_messages={'invalid': 'Digite um Email valido'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    Mensagem= forms.CharField(
        error_messages={'required': 'Obrigatorio o Preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
)
def clean_email(self):
        email= self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError ('O Email deve ser do gmail.com')
        return email