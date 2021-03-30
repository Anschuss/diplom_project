from django import forms
from crispy_forms.helper import FormHelper

from .models import TenderDoc


class AddedDocForm(forms.ModelForm):
    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].label = 'Дата добавления'

    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = TenderDoc
        fields = (
            "number_contract", "customer", "document", "organizer", "clinic",
            "type_tender", "status", "price", "guarantee", "type_product",
            "product", "date", "description"
        )
