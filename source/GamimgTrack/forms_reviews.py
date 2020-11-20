from django import forms


class CriarReviewForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255, required=True)
    content = forms.CharField(label="Conteudo", widget=forms.Textarea, required=True)
