from django import forms
from BookingManagement.models import Room


class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            "number",
            "type",
            "price",
            "capacity",
            "image",
        )

    def __init__(self, *args, **kwargs):
        super(RoomCreationForm, self).__init__(*args, **kwargs)
        for fieldname in [
            "number",
            "type",
            "price",
            "capacity",
        ]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {"class": "form-control"})
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "type": "file"})


class RoomEditForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            "number",
            "type",
            "price",
            "capacity",
            "image",
        )

    def __init__(self, *args, **kwargs):
        super(RoomEditForm, self).__init__(*args, **kwargs)
        for fieldname in [
            "number",
            "type",
            "price",
            "capacity",
        ]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {"class": "form-control"})
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "type": "file"})

    def clean(self):
        cleaned_data = super().clean()
        for key in list(cleaned_data.keys()):
            if cleaned_data[key] == '':
                del cleaned_data[key]
        return cleaned_data
