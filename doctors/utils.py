from datetime import datetime, timedelta
from doctors_app.settings import LANGUAGE_CODE

hours_list = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

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
    string = string[-14:]
    string = string.replace('-', ' ')
    string = string.replace('/', '-')
    string += ':00'
    return string
