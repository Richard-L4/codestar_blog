from django import forms
from allauth.account.forms import SignupForm
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Password 1 help text (manual bullet list with <p>)
        self.fields['password1'].help_text = (
            '<p>&bull; Your password must be at least 8 characters long.</p>'
            '<p>&bull; It must not be entirely numeric.</p>'
            '<p>&bull; It must not be a commonly used password.</p>'
            '<p>&bull; It must not be too similar to your personal information.</p>'
        )

        # Password 2 help text
        self.fields['password2'].help_text = (
            '<p>Please enter the same password again for verification.</p>'
        )
