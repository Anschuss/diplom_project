from django import forms
from .models import Presentation


class AddedPresentationForm(forms.ModelForm):
    document = forms.FileField(required=False)

    class Meta:
        model = Presentation
        fields = (
            "number_tender", "status", "description"
        )
