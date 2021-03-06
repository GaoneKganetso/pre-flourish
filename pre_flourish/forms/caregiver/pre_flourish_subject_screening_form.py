from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ...models import PreFlourishSubjectScreening


class PreFlourishSubjectScreeningForm(SiteModelFormMixin, FormValidatorMixin,
                           forms.ModelForm):
    screening_identifier = forms.CharField(
        required=False,
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = PreFlourishSubjectScreening
        fields = '__all__'
