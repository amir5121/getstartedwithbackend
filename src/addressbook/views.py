from django.views.generic.edit import CreateView
from django.forms import ModelForm

from addressbook.models import Addressbook


class PhonebookForm(ModelForm):
    class Meta:
        model = Addressbook
        exclude = ['id']


class AddressbookView(CreateView):
    form_class = PhonebookForm
    success_url = "/"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        kwargs["object_list"] = Addressbook.objects.order_by("id")
        return super(AddressbookView, self).get_context_data(**kwargs)
