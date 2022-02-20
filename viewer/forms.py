from django.core.exceptions import ValidationError
from django.forms import (
    Form,
    CharField,
    ModelChoiceField,
    IntegerField,
    DateField,
    Textarea,
    SelectDateWidget,
    NumberInput, ModelForm,
)
from datetime import date
from viewer.models import Genre, Movie


def capitalize_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


def dupa_validator(value: str) -> None:
    if 'dupa' in value.lower():
        raise ValidationError("Dupa is not allowed in this field.")


def unique_validator(value: str) -> None:
    splitted_val = value.strip('.').strip(',').strip('!').strip('?').lower().split(" ")
    if len(splitted_val) != len(set(splitted_val)):
        raise ValidationError("Only unique words allowed.")


class PastDate(DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Future dates are not allowed.")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    title = CharField(max_length=128, validators=[capitalize_validator])
    released = PastDate(widget=NumberInput(attrs={"type": "date"}))
    description = CharField(widget=Textarea, required=False, validators=[])

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Comedy' and result['rating'] > 6:
            self.add_error("genre", f"Can't be Comedy if {result['rating']}.")
            self.add_error("rating", f"Cant't be {result['rating']} if genre is Comedy.")
            # self.add_error("rating", f"Cant't be {result['rating']} if genre is {result['genre'].name}.") !!!Czemu nie dziala??????
            raise ValidationError("Comedies are not so good to be rated above 6.")
        return result


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
    name = CharField(max_length=128)
