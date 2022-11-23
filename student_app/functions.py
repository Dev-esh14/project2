from django.conf import settings
from django.core.mail import BadHeaderError,EmailMessage
import os
import sys
sys.path.append("student_app")
from .models import Bonafide, Staff, Student, Department
from pdfMaker.makePdf import htmlGenerator,from_template

from background_task import background

"""
 i haven't configured thanks.html properly so don't worry if u
 get pageNotFountError. <program works>
-----------------------------------------------------------------------------------------------------------
"""
@background(schedule=60)
def send_email(student_id,staff_id,bonafide_id):
    student= Student.objects.get(rollno=student_id)
    bonafide=Bonafide.objects.get(pk=int(bonafide_id))
    staff=Staff.objects.get(staffid=staff_id)
    department=Department.objects.get(department_name=student.department)


    OUTPUT_FILENAME = student.rollno+ '_' + bonafide_id + '.pdf'
    TEMPLATE_FILE = "E:\\projects\\django_projects\\bongen\\student_app\\bonfide_template\\template.html"

    # subject mail body to mail
    subject = bonafide.reason_for_request
    message = "this is a test , so don't worry..."
    # user mail ID -> From
    from_email = settings.EMAIL_HOST_USER

    try:
        if subject and message and from_email:
            #send_mail(subject, message, from_email,receiver mail id => ['@gmail.com','@gmail.com'])
            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [student.email, staff.email])

            # generate html Template from making PDF
            htmlGenerator(student=student,bonafide=bonafide,staff=staff,department=department)
            # Generate PDF from Template
            from_template(TEMPLATE_FILE, OUTPUT_FILENAME)

            #attachs Pdf generated
            email.attach_file(OUTPUT_FILENAME)
            email.send()
            os.remove(OUTPUT_FILENAME)
            return 'success'
        else:
            return 'Make sure all fields are entered and valid'

    except BadHeaderError :
        return 'Invalid header found'
#

#print(send_email('2019PECCS302', 'karthikeyansvkm2311@gmail.com'))