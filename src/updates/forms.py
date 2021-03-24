from django import forms

from .models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data
        content = data.get("content", None)
        image = data.get("image", None)

        if (content is None or content == "") and (image is None or image == ""):
            raise forms.ValidationError('Content or image is required.')

        return super().clean()

    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image'
        ]
