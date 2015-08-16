from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response



# The following dictionary represents the state dictionary

state_dic = {'act':['Australia Capital Territory',
'It\'s a nice place','australia capital territory is a beautiful place','/image/act.jpg','/image/actview.jpg'],
'vic':['Victoria','it has the most beautiful night','many description','/image/vic.jpg','/image/vicview.jpg'],
'sa':['South Australia','the great ocean','many description','/image/sa.jpg','/image/saview.jpg'],
'tas':['Tasmania','it has the most beautiful night','many description','/image/tas.jpg','/image/tasview.jpg'],
'nt':['Northern Territory','it has the most beautiful night','many description','/image/nt.jpg','/image/ntview.jpg'],
'qld':['Queensland','it has the most beautiful night','many description','/image/qld.jpg','/image/qldview.jpg'],
'nsw':['New South Wales','it has the most beautiful night','many description','/image/nsw.jpg','/image/nswview.jpg'],
'wa':['Western Australia','it has the most beautiful night','many description','/image/wa.jpg','/image/waview.jpg']}





def homepage(request):
	# html="<html><body>It is now.</body></html>" 

	t = get_template('homepage.html')
	html = t.render(Context({'homepage_des_title':'What We Provide',
		'homepage_des_content':'We are aim to provide you a better trip, in Australia or even in the whole world.',
		'state_dic':state_dic,}))
	return HttpResponse(html)




def service(request):
	# html="<html><body>It is now.</body></html>" 
	t = get_template('service.html')
	html = t.render(Context())

	return HttpResponse(html)	


def about(request):
	# html="<html><body>It is now.</body></html>" 
	t = get_template('about.html')
	html = t.render(Context({'imagepath':'/image/about.jpg',
		'about_des_title':'Who are we behind the website',
		'about_des_content':'Anything description'}))

	return HttpResponse(html)


def contact(request):
	# html="<html><body>It is now.</body></html>" 
	t = get_template('contact.html')
	html = t.render(Context())

	return HttpResponse(html)	


def playtem(request):
	t=get_template('play.html')
	html = t.render(Context())
	return HttpResponse(html)



def act(request):
	key = 'act'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)



def vic(request):
	key = 'vic'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)	

def sa(request):
	key = 'sa'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)	

def tas(request):
	key = 'tas'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)	


def nt(request):
	key = 'nt'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)	

def qld(request):
	key = 'qld'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)	

def nsw(request):
	key = 'nsw'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)	


def wa(request):
	key = 'wa'
	t = get_template('state.html')
	html = t.render(Context({'statename':state_dic[key][0],
		'state_des_title':state_dic[key][1],
		'state_des_content':state_dic[key][2],
		'imagepath':state_dic[key][4]}))
	return HttpResponse(html)				
