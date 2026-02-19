from django import forms
from .models import Service
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ["serviceName", "serviceDescription", "servicePrice", "categoryId"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✅ Custom required error messages
        self.fields["serviceName"].error_messages["required"] = "Service Name is required!"
        self.fields["serviceDescription"].error_messages["required"] = "Service Description is required!"
        self.fields["servicePrice"].error_messages["required"] = "Service Price is required!"
        self.fields["categoryId"].error_messages["required"] = "Category is required!"

        # Crispy helper
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field("serviceName", css_class="form-control"),
            Field("serviceDescription", css_class="form-control"),
            Field("servicePrice", css_class="form-control"),
            Field("categoryId", css_class="form-control"),
        )
