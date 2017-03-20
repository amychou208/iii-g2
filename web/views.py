# coding: utf-8
from django.shortcuts import render 
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
import random, os
from web import forms
from PIL import Image, ImageDraw, ImageFont
#from django.contrib.auth.decorators import login_required
from uuid_upload_path import uuid
from .models import Matchlist, Registration, Starlist

# Create your views here.

def Photo_upload(request):
    messages.get_messages(request)
    custom_backfile = None
    if 'custom_backfile' in request.session:
        if len(request.session.get('custom_backfile')) > 0:
            custom_backfile = request.session.get('custom_backfile')

    if request.method=='POST':
        if 'change_backfile' in request.POST:
            upload_form = forms.UploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                custom_backfile = save_backfile(request.FILES['file'])
                request.session['custom_backfile'] = custom_backfile
                #messages.add_message(request, messages.SUCCESS, "檔案上傳成功！")
                return redirect('/web/photoloading/')
            else:
                messages.add_message(request, messages.WARNING, "檔案上傳失敗！")
                return redirect('/web/')
        else:
            if custom_backfile is None:
                back_file = os.path.join(settings.BASE_DIR, 'static/photo/eu.png')
            else:
                back_file = os.path.join(settings.BASE_DIR, 'web/media', custom_backfile)
    	        saved_filename = back_file
    else:
        upload_form = forms.UploadForm()


    template = get_template('2.Photo_upload.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def save_backfile(f):
    target = os.path.join(settings.BASE_DIR,"web/media", uuid()+'.jpg')
    with open(target, 'wb') as des:
        for chunk in f.chunks():
            des.write(chunk)
    return os.path.basename(target)

def Photoloading(request):
		
	return render (request, '3.Photo_loading.html',{})

def Mystarface(request):

        star_list = Starlist.objects.all()
        return render (request, '4.mystarface.html',locals())

def Registration_post(request):
    if request.method == 'POST':
        r_form = forms.RegistrationForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            return HttpResponseRedirect('/web/photoloading/')
        else:
            messages.add_message(request, messages.WARNING, "請確認填入資料是否正確！")
            return HttpResponseRedirect('/web/registration/')
    else:
        r_form = forms.RegistrationForm()

    template = get_template('registration.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

def post2db(request):
    messages.get_messages(request)
    if request.method == 'POST':
        r_form = forms.RegistrationForm(request.POST)
	if r_form.is_valid():
            r_form.save()
#  	    print request.POST.get('matchgender')
#           print type(request.POST.get('matchgender'))
#	    gender = request.POST.get('matchgender')
#	    str(gender)
#	    if gender == "女性":
#		   return HttpResponseRedirect('/web/choosegirl/')
#	    else:
	    return HttpResponseRedirect('/web/chooseboy/')
        else:
            messages.add_message(request, messages.WARNING, "請確認填入資料是否正確！")
    	    return HttpResponseRedirect('/web/registration/')
    else:
        r_form = forms.RegistrationForm()

    template = get_template('post2db.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

def Loading(request):

	return render (request, '6.Form_loading.html',{})


def Choosegirl(request):

        return render (request, '6.choosegirl.html',{})

def Chooseboy(request):

        return render (request, '6.chooseboy.html',{})

def matchlist(request):
	match_list = Matchlist.objects.all()
	return render (request, '7.Matching_list.html',locals())

def AccountInfo(request,id):
		
	account = Registration.objects.get(id=id)
    	
	return render(request, "8.Account_Info.html", locals())


from django.shortcuts import render
from textflow.models import FlowObject

def your_view(request):
  return render(request, 'template.html', {
    'texts': FlowObject.serialize(),
  })
