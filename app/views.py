from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, course, Contact
# from .forms import JobForm, courseForm
from django.contrib import messages

# Create your views here.

def course_edit(request):
    # mycourse = get_object_or_404(course)
    if request.method == "POST":
        title = request.POST['title']
        # print(request, title)
        company_name = request.POST.get('company_name')
        certification = request.POST.get('certification')
        instructor = request.POST['instructor']
        duration = request.POST['duration']
        description = request.POST.get('description')

        blog = course.objects.create(title=title, instructor=instructor, duration=duration, company_name=company_name, certification=certification, description=description)
        # blog = course.objects.all()
    
        messages.success(request, f'Profile Updated Succefully!!!!ttttttttttt')
        return redirect('course_edit')

    else:
        blog = course.objects.all()
        return render(request, 'app/aplicant_edit.html', {'blogs': blog})



def aplicant_edit(request):

    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        print(first_name, '888888888888888888888888888')
        second_name = request.POST.get("second_name")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        state = request.POST.get("state")
        countary = request.POST.get("countary")
        university = request.POST.get("university")
        school = request.POST.get("school")
        education = request.POST.get("education")
        address = request.POST.get("address")
        current_address = request.POST.get("current_address")
        project = request.POST.get("project")
        email = request.POST.get("email")
        number = request.POST.get("number")

        title = request.POST['title']
        # print(request, title)ew Aplican
        company_name = request.POST.get('company_name')
        certification = request.POST.get('certification')
        instructor = request.POST['instructor']
        duration = request.POST['duration']
        description = request.POST.get('description')

        blog = course.objects.create(title=title, instructor=instructor, duration=duration, company_name=company_name, certification=certification, description=description)


        person = Job.objects.create(first_name = first_name, second_name=second_name, gender=gender, city=city, state=state,
        countary=countary, university=university, school=school, education=education, address=address,
        project=project, email=email, number=number)

        messages.success(request, f'Profile Updated Succesfully!!!!ttttttttttt')
        return redirect('aplicant_edit')
    else:
        person = Job.objects.all()
        blog = course.objects.all()
        return render(request, 'app/aplicant_edit.html', {'person': person, 'blogs': blog})
