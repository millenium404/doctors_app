from datetime import datetime, timedelta
from .models import Doctor
from appointments.models import Appointment

hours_list = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

def week_range():
    today = datetime.now() - timedelta(hours=13)
    week_ahead = today + timedelta(days=7)
    range = [today.date(), week_ahead.date()]
    return range

def appointments_dict(id, week):
    today = datetime.now() - timedelta(hours=3)
    today += timedelta(weeks=int(week))
    week_ahead = today + timedelta(days=7)
    appointments = Appointment.objects.filter(doctor_id=id, hour__range=[today.date(), week_ahead.date()])
    dictionary = {}
    for app in appointments:
        time_object = app.hour.strftime('%d/%m/%y %H:%M').split()
        date = time_object[0]
        hour = time_object[1]
        status = app.status
        patient = app.user_id
        app_id = app.id
        if date not in dictionary:
            dictionary[date] = [[hour, status, patient, app_id]]
        else:
            dictionary[date] += [[hour, status, patient, app_id]]
    return dictionary

def date_time_object(string):
    #2022-04-04 13:00:00
    #'Събота, 04/09/22-11:30'
    string = string[:16]
    string = string.replace('-', ' ')
    string = string.replace('/', '-')
    string = string.replace('[', '')
    string = string.replace("'", '')
    string = string.replace('-', ' ')
    string = string.replace(':', ' ')
    string = string.split()
    new_string = f"20{string[2]}-{string[1]}-{string[0]} {string[3]}:{string[4]}"
    return new_string

def populate_appointments(id):
    appointments = Appointment.objects.filter(doctor_id=id)
    time_now = datetime.now() - timedelta(days=7)
    time_before = time_now - timedelta(days=7)
    old_appointments = Appointment.objects.filter(doctor_id=id, hour__range=[time_before, time_now])
    old_appointments.delete()
    if len(appointments) < 1980:
        for n in range(90):
            for hour in hours_list:
                time = datetime.now()
                date = time + timedelta(days=n)
                new_hour = f"{date.date()} {hour}:00"
                appointments_query = appointments.filter(hour=new_hour).first()
                try:
                    check_hour = str(appointments_query.hour)
                except:
                    check_hour = ''
                if new_hour not in check_hour:
                    appointment = Appointment.objects.create(doctor_id=id, user_id=0, status='not_available', hour=f"{date.date()} {hour}:00")

def save_appointment_hours(post_request, id, week):
    query = post_request
    today = datetime.now() - timedelta(hours=13)
    today += timedelta(weeks=int(week))
    week_ahead = today + timedelta(days=7)
    app_object = Appointment.objects.filter(doctor_id=id, hour__range=[today.date(), week_ahead.date()])
    for app in app_object:
        app.status = 'not_available'
        app.save()
    for key, value in query.items():
        if key not in ['csrfmiddlewaretoken', 'button']:
            hour = date_time_object(value)
            app_object = Appointment.objects.filter(doctor_id=id, hour=hour).first()
            app_object.status = 'available'
            app_object.save()
