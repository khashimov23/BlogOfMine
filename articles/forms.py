from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
    
    # overriding default form setting and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs = {'placeholder': 'Enter name','class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder': 'Leave comment..', 'class':'form-control', 'rows':'5'}