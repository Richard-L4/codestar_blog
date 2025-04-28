from django import forms
from .models import Comment
from allauth.account.forms import SignupForm

# Form for blog comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Custom signup form for allauth (outside of CommentForm)
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Replace the help texts so there are no <ul> or <li> in them
        self.fields['password1'].help_text = "Password must be at least 8 characters."
        self.fields['password2'].help_text = "Enter the same password again to verify."
