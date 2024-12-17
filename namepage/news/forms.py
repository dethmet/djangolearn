from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'main_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назови наброс'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заинтригуй'
            }),
            'main_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Набрасывай во всю!!!'
            }),            
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата наброса',
                'type': 'datetime-local'                
            })
        }
