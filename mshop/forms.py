from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('text',)
        def __init__(self, *args,**kwargs) :
            super().__init__(self, *args,**kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class']= 'form-control'