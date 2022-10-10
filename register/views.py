from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewUser
 
from django.core.mail import EmailMessage



def index(request):
    
  if request.method == 'POST':




    surname = request.POST['surname']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    phone = request.POST['phone']
    company = request.POST['company']
    firstname = request.POST['firstname']
    gender = request.POST['gender']
    education = request.POST['education']
    religion = request.POST['religion']
    location = request.POST['location']



    if password == password2:

        
      if NewUser.objects.filter(surname=surname).exists():

        messages.error(request, ' Surname has already been taken ')
        return redirect('index')

      elif NewUser.objects.filter(email=email).exists():

        messages.error(request, ' Email has already been taken ')
        return redirect('index')

      
           

      else:

        new_user = NewUser.objects.create_user(username=surname,first_name=firstname, phone=phone, password=password, email=email, location=location, education=education, religion=religion, company=company, gender=gender)
        new_user.is_active = False

        email_subject = 'Activate your acount '
        email_body = ' Click this link to activate your account'
        email = EmailMessage(
          settings.EMAIL_HOST_USER,
          email_subject,
          email_body,          
          'noreply@jobber.com',
          [email],
                  )
        email.send(fail_silently=False)
        new_user.save()
        
        messages.info(request, 'Successful !! Activation link has been sent to your mail', )
        return redirect('index')

    else:
      messages.error(request, 'Invalid Credentials')
      return redirect('index')

  else:
    return render(request, 'index.html')