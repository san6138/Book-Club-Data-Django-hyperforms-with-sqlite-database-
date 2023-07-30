import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant, FormField, FormModel, FormData, FormRecord
from .forms import Registrationform
from django.views import View

# Create your views here.
class Indexview(View):
    def get(self, request, *args, **kwargs):
        record_list = []
        all_participants = FormRecord.objects.all()
        for participant in all_participants:
            form = FormData.objects.filter(record_id=participant.id)
            record_list.append(form)
        model = FormModel.objects.filter(name="participants").first()
        headings = model.form_fields.all()
        return render(request, "forms/index.html", {"all_participants": record_list, "headings": headings})



class RegisterView(View):
    def post(self, request):
        new_data_dic = dict(request.POST)
        new_record = FormRecord.objects.create()
        form_field = FormField.objects.filter(form=FormModel.objects.filter(name="participants").first())
        del new_data_dic["csrfmiddlewaretoken"]
        for data, formfield in zip(new_data_dic, form_field):
            print(data)
            FormData.objects.create(record_id=new_record.id, form_field_id=formfield.id, value=new_data_dic[data][0])
        return HttpResponse(f"success{new_data_dic}")

    def get(self, request):
        forms = FormField.objects.all()
        return render(request, "forms/registration.html", {'form': forms})