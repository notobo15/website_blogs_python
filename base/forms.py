from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Article, Comment
from tinymce.widgets import TinyMCE
from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


from django import forms
from mptt.forms import TreeNodeChoiceField
# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'desc', 'content', 'category_id']


class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password1'].help_text = None
    #     self.fields['password2'].help_text = None
    # username = forms.CharField(label='username', min_length=5, max_length=150)
    # email = forms.EmailField(label='email')
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 = forms.CharField(
    #     label='Confirm password', widget=forms.PasswordInput)

    # def username_clean(self):
    #     username = self.cleaned_data['username'].lower()
    #     new = User.objects.filter(username=username)
    #     if new.count():
    #         raise ValidationError("User Already Exist")
    #     return username

    # def email_clean(self):
    #     email = self.cleaned_data['email'].lower()
    #     new = User.objects.filter(email=email)
    #     if new.count():
    #         raise ValidationError(" Email Already Exist")
    #     return email

    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']

    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Password don't match")
    #     return password2

    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password1']
    #     )
    #     return user


class CreateCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    class Meta:
        model = Comment
        fields = ['content', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['content'].label = ''
        self.fields['parent'].label = ''
        self.fields['parent'].required = False
