from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["text"]
        labels = {"text": "Note"}
        widgets = {"text": forms.TextInput(attrs={"placeholder": "Write a short note", "autocomplete": "off"})}

    def clean_text(self):
        text = self.cleaned_data["text"].strip()
        if not text:
            raise forms.ValidationError("Write something first.")
        return text
