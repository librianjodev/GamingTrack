from django import forms


class CriarPostagemForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True, label="Conteudo")
