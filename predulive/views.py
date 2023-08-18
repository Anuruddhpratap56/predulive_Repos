from django.shortcuts import render
from campaigns.models import campaigns
from innovations.models import innovation
from media_coverage.models import news
from media_coverage.models import achievements
from contact.models import contact
def homePage(request):
    cam_data=campaigns.objects.all()
    inn_data=innovation.objects.all()
    news_data=news.objects.all()
    ach_data=achievements.objects.all()
    
    if request.method=='POST':  
        fullName=request.POST.get('fullName')
        emailAddress=request.POST.get('emailAddress')
        mobileNumber=request.POST.get('mobileNumber')
        emailSub=request.POST.get('emailSubject')
        message=request.POST.get('message')
    
        contactInfo=contact(name=fullName,email=emailAddress,mobile=mobileNumber,email_sub=emailSub,description=message)
    
        contactInfo.save()
    
    data={'data1':cam_data,'inn1':inn_data,'news_data1':news_data,'ach_data1':ach_data}
    return render(request,'index.html',data)
    