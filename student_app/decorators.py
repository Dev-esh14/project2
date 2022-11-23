from .models import Staff, Student
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

def staff_status(fn):
    def wrapper(request):
        try:
            username = request.user.get_username()
            # if request.user.is_superuser:
            #     return fn(request)
            try:
                obj= Staff.objects.get(staffid=username)
            except:
                obj= Student.objects.get(rollno=username)
            if obj.is_staff:
                return fn(request)
            else:
                # return JsonResponse({
                #     'status':'error',
                #     'msg':'Login as a staff to view this page'
                # })
                return redirect('staff_login')
        except:
            # return JsonResponse({
            #     'status':'error',
            #     'msg':'Login as a staff to view this page'
            # })
            return redirect('staff_login')
    return wrapper

def student_status(fn):
    def wrapper(request):
        try:
            username = request.user.get_username()
            # if request.user.is_superuser:
            #     return fn(request)
            try:
                obj= Student.objects.get(rollno=username)
            except:
                obj= Staff.objects.get(staffid=username)
            if obj.is_student:
                return fn(request)
            else:
                # return JsonResponse({
                #     'status':'error',
                #     'msg':'Login as a student to view this page'
                # })
                return redirect('student_login')
        except:
            # return JsonResponse({
            #     'status':'error',
            #     'msg':'Login as a student to view this page'
            # })
            return redirect('student_login')
    return wrapper

def admin_status(fn):
    def wrapper(request):
        try:
            if request.user.is_superuser:
                return fn(request)
            else:
                # return JsonResponse({
                #     'status':'error',
                #     'msg':'Only admins can view this page'
                # })
                return redirect('staff_login')
        except:
            # return JsonResponse({
            #     'status':'error',
            #     'msg':'Only admins can view this page'
            # })
            return redirect('staff_login')
    return wrapper