"""Forms for blog comments and custom signup form for user registration."""

from django import forms
from .models import Comment
from allauth.account.forms import SignupForm


class CommentForm(forms.ModelForm):
    """
    Form for users to submit a comment.

    This form is linked to the Comment model and allows users
    to input their comment body.
    """

    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    """
    Custom signup form to override default labels and help texts.

    - Changes field labels for username, email, and passwords.
    - Provides simpler, more user-friendly password help text.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the form and customize field labels and help texts."""
        super().__init__(*args, **kwargs)

        # Customize field labels
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email (optional)"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password (again)"

        # Customize password help texts
        self.fields['password1'].help_text = (
            "Your password must be at least 8 characters long "
            "and not be entirely numeric."
        )
        self.fields['password2'].help_text = (
            "Enter the same password again to verify."
        )
