from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Type your question or message...'}),
        label="Your Message"
    )
    image = forms.ImageField(label="Attach Image (optional)", required=False)
