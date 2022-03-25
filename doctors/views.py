from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DoctorEditForm
from .models import Doctor
from django.http import Http404

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
