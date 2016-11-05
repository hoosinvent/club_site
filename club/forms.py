from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    email_subject = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Field('contact_name', css_class='form-control'),
            Field('contact_email', css_class='form-control'),
            Field('email_subject', css_class='form-control'),
            Field('content', css_class='form-control'),
            FormActions(Submit('submit', 'Submit', css_class='btn btn-primary'))
        )