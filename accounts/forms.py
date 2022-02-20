from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ChoiceField, Textarea, CharField

from accounts.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True):
        result = super(SignUpForm, self).save(commit)
        profile = Profile(id=result.id, biography='', gender='', user=result)
        if commit:
            profile.save()
        return result

class UserProfileUpdateForm(ModelForm):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    class Meta:
        model = Profile
        fields = '__all__'

    gender = ChoiceField(choices=GENDER_CHOICES, required=False)
    biography = CharField(label="Tell us your story with movies", widget=Textarea, required=False)
