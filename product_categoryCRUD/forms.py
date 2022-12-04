from django import forms


class ProductCategoryUpdateForm(forms.Form):

    desc_attrs = {
        'type': 'text',
        'name': 'description',
        'id': 'description',
        'placeholder': 'Change your description here..'
    }

    desc = forms.CharField(label="", widget=forms.Textarea(attrs=desc_attrs))
