from django.forms import ModelForm
from .models import Article
from tinymce.widgets import TinyMCE


# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'desc', 'content', 'category_id']
