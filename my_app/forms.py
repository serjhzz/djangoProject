from django import forms

from my_app.models import Post


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PostForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'preview',]
