#from twilio.rest import Client

import json
import requests
import random

from django.core.mail import send_mail

def verifyEmail(request,user):
		activation_code=random.randrange(111111111111,999999999999)
		request.session['activation_code'] = activation_code
		#send_mail(<subject>,<message>,[<email1>,<emai2>],fail_silently=False)
			
		subject='Welcome to ToDoApp!!'
		message='''We are happy to see you on our platform. <br /><br />
				   Please click over the <a href='http://localhost:8000/todoapp/actact/?id={}&act_code={}'>link</a> to activate your account. 	
				'''.format(user.id,activation_code,user.first_name+' '+user.last_name)
		send_mail(subject,'','ToDoApp Welcomes you',[request.POST.get('email')],fail_silently=False,html_message=message)

def reCaptcha(request):
		responsekey=request.POST.get('g-recaptcha-response')
		secretkey='6Lct2PIUAAAAADJaCrr1d6FpMPaWXaHbxfBgp68y'
		captchadata={'secret':secretkey,'response':responsekey}
		resp=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
		respdict=json.loads(resp.text)
		return respdict['success']