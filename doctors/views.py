from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DoctorEditForm, DateForm, AppointmentForm
from .models import Doctor
from .filters import DoctorFilter
from django.http import Http404
from datetime import datetime, timedelta
from appointments.models import Appointment
from .utils import populate_appointments, appointments_dict, save_appointment_hours

week = 0
days = 0

@login_required
def schedule_view(request, id=None):
    global week
    if request.user.id == id and request.user.profile.is_doctor:
        week = 0
        doctor = get_object_or_404(Doctor, user_id=id)
        context = {'doctor': doctor}
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
    global days
    days = 0
    obj = get_object_or_404(Doctor, id=id)
    context = {'doctor': obj}
    return render(request, 'doctors/detail-view.html', context)

def htmx_calendar_view(request, id):
    global days
    if request.method == 'GET':
        query = request.GET
        if query:
            days += int(query['date'])
            if days < 0:
                days = 0
    obj = get_object_or_404(Doctor, id=id)
    apps = Appointment.objects.filter(doctor_id=id, user_id=0).order_by('hour')
    date = datetime.now()
    for app in apps:
        if app.hour.timestamp() > date.timestamp():
            date = app.hour + timedelta(hours=3)
            break
    date = date + timedelta(days=days)
    next_date = date + timedelta(days=1)
    hours = Appointment.objects.filter(doctor_id=id, hour__range=[date.date(), next_date.date()], user_id=0, status='available')
    context = {'doctor': obj, 'hours': hours, 'days': days, 'date': date}
    return render(request, 'doctors/htmx-calendar.html', context)

def get_appointment_htmx(request, id):
    appointment = Appointment.objects.get(id=id)
    form = AppointmentForm()
    user_appointments = Appointment.objects.filter(user_id=request.user.id, doctor_id = appointment.doctor_id)
    context = {'appointment': appointment, 'form': form, 'id': id}
    if request.method == 'POST':
        if len(user_appointments) < 3:
            query = request.POST
            appointment.reason = query['reason']
            appointment.user_id = request.user.id
            appointment.save()
            context['success'] = 'Успешно запазихте избрания от Вас час.'
        else:
            context['error'] = '*Не може да запазите повече часове при този лекар!'
            return render(request, 'doctors/get-appointment.html', context)
    return render(request, 'doctors/get-appointment.html', context)

def schedule_calendar_htmx(request, id=None):
    global week
    doctor = get_object_or_404(Doctor, user_id=id)
    appointments = Appointment.objects.filter(doctor_id=id)
    if request.method == 'POST':
        try:
            save_appointment_hours(request.POST, id, week)
            messages.success(request, f'Графикът е обновен успешно.')
        except:
            messages.warning(request, f'Възникна грешка... Моля, опреснете страницата и опитайте отново.')
        return redirect('schedule-calendar-view', id=request.user.id)
    populate_appointments(id)
    hours = appointments_dict(id, week)
    if request.method == 'GET':
        query = request.GET
        if query:
            week += int(query['week'])
            if week < 0:
                week = 0
        hours = appointments_dict(id, week)
    context = {'doctor': doctor, 'hours': hours, 'week': week}
    return render(request, 'doctors/htmx-schedule-calendar.html', context)
