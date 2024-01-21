from django import forms


class RoomAvailabilityForm(forms.Form):
    entrance_date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'id': 'datepicker-entrance'}))
    exit_date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'id': 'datepicker-exit'}))
