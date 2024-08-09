from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_details.models import User, Address, AuthTokens
from django.contrib.auth import authenticate, login,logout
from doctors.models import Blogs,Categories,Appointments



# # Write this code in calendar_app/views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from oauth2_provider.views.generic import ProtectedResourceView
# from .models import Event
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# import datetime
# import pytz

# class CalendarView(ProtectedResourceView):
#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("This is your calendar view")


# def fetch_events(request):
#     try:
#         # Authenticate with Google Calendar API
#         creds = Credentials.from_authorized_user_file(
#             'token.json')  # Path to your token file
#         if creds.expired and creds.refresh_token:
#             creds.refresh(Request())

#         # Build Google Calendar API service
#         service = build('calendar', 'v3', credentials=creds)

#         # Retrieve events from Google Calendar
#         now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         events_result = service.events().list(
#             calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
#             orderBy='startTime').execute()
#         events_data = events_result.get('items', [])

#         # Save events to the database
#         for event_data in events_data:
#             start_time = event_data['start'].get(
#                 'dateTime', event_data['start'].get('date'))
#             end_time = event_data['end'].get(
#                 'dateTime', event_data['end'].get('date'))
#             start_time = datetime.datetime.fromisoformat(start_time)
#             end_time = datetime.datetime.fromisoformat(end_time)
#             # Convert to UTC timezone
#             start_time = pytz.utc.localize(start_time)
#             end_time = pytz.utc.localize(end_time)
#             # Save event to the database
#             Event.objects.create(
#                 summary=event_data.get('summary', ''),
#                 start_time=start_time,
#                 end_time=end_time
#             )

#         # Retrieve events from the database and display
#         events = Event.objects.all()
#         context = {'events': events}
#         return render(request, 'calendar_integration/calendar_events.html', context)

#     except Exception as e:
#         return HttpResponse(f"An error occurred: {e}")


def Patient_dashboard(request,id):
    context={}
    user=User.objects.get(id=id)
    add=Address.objects.filter(user=user).last()
    print('------addd',add)
    context['user']=user
    context['add']=add
    return render(request,'patient/patient_dashboard.html',context)

def logout_view(request):
    logout(request)
    return redirect('login_page')


def Blogs_list(request):
    context={}
    if request.GET.get('cat'):
        cat = request.GET.get('cat')
        context['blogs']=Blogs.objects.filter(is_draft=False,categories_id=cat).order_by('-id')    
    else:
        context['blogs']=Blogs.objects.filter(is_draft=False).order_by('-id')    
    context['cat']=Categories.objects.filter()
    
    return render(request,'patient/patient_blogs.html',context)



import requests
import json
from django.db.models import F
from doctors.generate_token import get_new_token
        
def book_appointment(request):
    context={}
    doctors=User.objects.filter(user_type='doctor').order_by('-id')
    cat=Categories.objects.all()
    context['doc']=doctors
    context['cat']=cat


    if request.method=='POST':
        token=AuthTokens.objects.get(id=1).token1
        spec=request.POST.get('spec')
        doc_id=request.POST.get('doc_id')
        # pat_id=request.POST.get('pat_id')
        dateandtime=request.POST.get('dateandtime')
        print('1111',spec)
        print('22222',dateandtime)
        print('tokkk',token)
        from datetime import datetime,timedelta
        # now = datetime.now()  
        # dateandtime=str(dateandtime).replace('T',' ')
        new_now = datetime.strptime(dateandtime, '%Y-%m-%dT%H:%M')  
        new_now1=new_now+timedelta(minutes = 45)
        print('------',new_now)
        
        end_date=new_now1.strftime('%Y-%m-%dT%H:%M:%S+05:30')
        print('------',end_date)
        
        str_date=new_now.strftime('%Y-%m-%dT%H:%M:00+05:30')


        import requests
        import json

        url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"

        payload = json.dumps({
        "start": {
            "dateTime": str_date,
            "timeZone": "Asia/Kolkata"
        },
        "end": {
            "dateTime": end_date,
            "timeZone": "Asia/Kolkata"
        },
        "summary": "Appointment Booked",
        "description": F"Appointment Booked by {request.user.email}"
        })
        headers = {
        'Authorization': F'Bearer {token}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        # except :
        if response.status_code==401:
            res=get_new_token()
            token="Bearer "+res['access_token']
            print('-------tokrn22',token)
            payload1 = json.dumps({
            "start": {
                "dateTime": str_date,
                "timeZone": "Asia/Kolkata"
            },
            "end": {
                "dateTime": end_date,
                "timeZone": "Asia/Kolkata"
            },
            "summary": "Appointment Booked",
            "description": F"Appointment booked by {request.user.email}"
            })
            headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload1)

            print('====response22',response.text)
            # except :
            if response.status_code==200:

                apps=Appointments.objects.create(doc_id=doc_id,pat_id=request.user.id,start_date_time=str_date,end_date_time=end_date)
                return redirect('booked_appoints',id=apps.id)
            else:
                context["message"]="some technical issue"
        elif response.status_code==200:

            apps=Appointments.objects.create(doc_id=doc_id,pat_id=request.user.id,start_date_time=str_date,end_date_time=end_date)
            return redirect('booked_appoints',id=apps.id)
        else:
            context["message"]="some technical issue"
        
    return render(request,'patient/appointment.html',context)

def Booked_appoints(request,id):
    context={}
    context['app']=Appointments.objects.filter(id=id).last()

    return render(request,'patient/booked_appoints.html',context)