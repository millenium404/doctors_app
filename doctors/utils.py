from datetime import datetime, timedelta
from doctors_app.settings import LANGUAGE_CODE
from .models import Doctor
from appointments.models import Appointment

hours_list = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

def week_days():
    today = datetime.now()
    days_list = []
    for n in range(7):
        day = today + timedelta(days=1)
        day = day.strftime('%A')
        days_list.append(day)
    return days_list


def week_range():
    today = datetime.now() - timedelta(hours=13)
    week_ahead = today + timedelta(days=7)
    range = [today.date(), week_ahead.date()]
    return range


def appointments_dict(id):
    today = datetime.now() - timedelta(hours=13)
    week_ahead = today + timedelta(days=7)
    appointments = Appointment.objects.filter(doctor_id=id, hour__range=[today.date(), week_ahead.date()])
    dictionary = {}
    for app in appointments:
        time_object = app.hour.strftime('%d/%m/%y %H:%M').split()
        date = time_object[0]
        hour = time_object[1]
        status = app.status
        patient = app.user_id
        if date not in dictionary:
            dictionary[date] = [[hour, status, patient]]
        else:
            dictionary[date] += [[hour, status, patient]]
    return dictionary

def week_list():
    current_time = datetime.now()
    week_list = []
    for n in range(7):
        time = current_time + timedelta(days=n)
        # time_string += str(time.date())
        formated_time = time.strftime('%A, %x')
        if LANGUAGE_CODE == 'bg':
            formated_time = formated_time.replace('Monday', 'Понеделник')
            formated_time = formated_time.replace('Tuesday', 'Вторник')
            formated_time = formated_time.replace('Wednesday', 'Сряда')
            formated_time = formated_time.replace('Thursday', 'Четвъртък')
            formated_time = formated_time.replace('Friday', 'Петък')
            formated_time = formated_time.replace('Saturday', 'Събота')
            formated_time = formated_time.replace('Sunday', 'Неделя')
        week_list.append(formated_time)
    return week_list

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
    start_time = datetime.now()
    if len(appointments) < 2640:
        for n in range(120): #Its still broken, to be fixed!
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
                    appointment = Appointment.objects.create(doctor_id=id)
                    appointment.user_id = 0
                    appointment.status = 'not_available'
                    appointment.hour = f"{date.date()} {hour}:00"
                    appointment.save()
