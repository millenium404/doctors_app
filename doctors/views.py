from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DoctorEditForm
from .models import Doctor
from .filters import DoctorFilter
from django.http import Http404
from datetime import datetime, timedelta
from appointments.models import Appointment
from .utils import hours_list, week_list, date_time_object, populate_appointments


def datetime_view(request): # Test view. To be removed!
    appointment = Appointment.objects.first()
    time = appointment.hour
    formated_time = time.strftime("Имате записан час за %H:%M на %x")
    context = {'time': formated_time}
    return render(request, 'doctors/datetime.html', context)

def schedule_view(request, id=None):
    doctor = get_object_or_404(Doctor, user_id=id)
    appointments = Appointment.objects.filter(doctor_id=id)
    if request.method == 'POST':
        query = request.POST
        # print(query)
        for key, value in query.items():
            if key not in ['csrfmiddlewaretoken', 'button']:
                value = date_time_object(value)
                print(value)
        return redirect('schedule-view', id=request.user.id)
    if request.user.id == id and request.user.profile.is_doctor:
        populate_appointments(id)
        hours = hours_list
        dates = week_list()
        context = {'doctor': doctor, 'appointments': appointments, 'hours': hours, 'dates': dates}
        return render(request, 'doctors/schedule.html', context)
    else:
        raise Http404

def doctor_search_view(request):
    query_dict = request.GET # This is a dictionary
    query = query_dict.get('q') # <input type="text" name="q">
    qs = Doctor.objects.search(query=query)
    context = {'doctors': qs}
    return render(request, 'doctors/search.html', context)

@login_required
def doctor_edit_view(request, id=None):
    obj = get_object_or_404(Doctor, user_id=id)
    form = DoctorEditForm(request.POST or None, instance=obj)
    context = {'object': obj, 'form': form}
    if form.is_valid():
        try:
            form.save()
            obj = Doctor.objects.get(user_id=id)
            obj.map_url = f"https://www.google.com/maps?q={obj.city}+{obj.address}&output=embed"
            obj.save()
            messages.success(request, f'Лекарската практика е обновена успешно.')
        except:
            messages.warning(request, f'Възникна грешка. Моля, опитайте отново.')
        return redirect('doctor-edit-view', id=id)
    if id == request.user.id and request.user.profile.is_doctor:
        return render(request, 'doctors/edit-doctor.html', context)
    else:
        raise Http404


def doctor_list_view(request):
    obj = Doctor.objects.all()
    filter = DoctorFilter(request.GET, queryset=obj)
    context = {'object': obj, 'filter': filter}
    return render(request, 'doctors/list-view.html', context)

def doctor_detail_view(request, id=None):
    obj = get_object_or_404(Doctor, id=id)
    range = [1, 2, 3, 4, 5, 6, 7, 8]
    context = {'doctor': obj, 'range': range}
    return render(request, 'doctors/detail-view.html', context)
