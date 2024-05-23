# from pyexpat.errors import messages
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import User,tbl_bustype,tbl_bus,tbl_fare,tbl_schedule,Staff,tbl_bank_name,tbl_bank_account,tbl_smartcard,tbl_alert,tbl_complaint
from django.contrib import messages
from django.db.models import Q
import random
from django.contrib.sessions.models import Session
from datetime import date, timedelta
from io import BytesIO
from django.template import TemplateDoesNotExist
from django.db.models import OuterRef, Subquery, Q




# Create your views here.


#admin

def index(request):
    return render(request,'admins/index.html')

def aheader(request):
     return render(request,'admins/ahome.html')

def admin_login(request):
    if request.method=="POST":
        uname=request.POST['name']
        pwd=request.POST['pass']
        
        user=authenticate(request,username=uname,password=pwd)
        print(user)
        if uname=="admin" and pwd=="admin":
          return redirect(aheader)
        return HttpResponse("not approved")
    else:
        return render(request,'admins/index.html')
    
    
def admin_logout(request):
     return render(request,'admins/index.html')


def bustype(request):
     if request.method=='POST':
          bustype=request.POST['bus_type']
          tbl_bustype.objects.create(Bus_type=bustype)
          messages.success(request,"registration successfull")
          return render(request,'admins/bustype.html')
     else:
          return render(request,'admins/bustype.html')
     
def add_bus_details(request):
     if request.method=="POST":
          bus_no=request.POST['bus_no']
          bus_type=request.POST['bus_type']
          source=request.POST['source']
          start=request.POST['start_time']
          dest=request.POST['destination']
          endtime=request.POST['end_time']
          file=request.FILES['file']
          x=tbl_bus.objects.create(bus_no=bus_no,Source=source,Destination=dest,Start_time=start,End_time=endtime,bus_type_id_id=bus_type,bus_image=file,schedule_id_id='')
          messages.success(request,"Added successfull")
          return redirect(add_bus_details)
     else:
          type=tbl_bustype.objects.all()
          return render(request,'admins/add_bus_details.html',{'type':type})
     
def view_bus_details(request):
     # bus=tbl_bus.objects.all()
     buses = tbl_bus.objects.select_related('bus_type_id')
    
     return render(request,'admins/view_bus_details.html',{'buses':buses})

def edit_bus(request,eid):
     a=tbl_bus.objects.get(id=eid)
     return render(request,'admins/edit_bus.html',{'a1':a})

def edit_bus1(request,eid):
    if request.method=="POST":
          source=request.POST['source']
          start=request.POST['start_time']
          dest=request.POST['destination']
          endtime=request.POST['end_time']
          bus=tbl_bus.objects.get(id=eid)
          bus.Source=source
          bus.Start_time=start
          bus.Destination=dest
          bus.End_time=endtime
          bus.save()
          messages.success(request,"Updation successfull")
          return redirect(view_bus_details)
    
def delete_bus(request,did):
     s=tbl_bus.objects.get(id=did)
     s.delete()
     messages.success(request,"Deletion successfull")
     return redirect(view_bus_details)

def add_fare(request):
     if request.method=="POST":
          bus_type=request.POST['bus_type']
          min_chrg=request.POST['min_chrg']
          bus_type1 = request.POST.get('bus_type')
          s=tbl_fare.objects.filter(bus_type_id_id=bus_type1)
          if s.exists():
                x =tbl_fare.objects.filter(bus_type_id_id=bus_type).update(min_charge=min_chrg)
          else:
               x =tbl_fare.objects.create(min_charge=min_chrg,bus_type_id_id=bus_type1)     
              
          messages.success(request,"Added successfull")
          return redirect(add_fare)    
     else:      
          type=tbl_bustype.objects.all()
          return render(request,'admins/add_fare.html',{'type':type})


def view_fare(request):
     buses = tbl_fare.objects.select_related('bus_type_id')
     return render(request,'admins/view_fare.html',{'buses':buses})

def add_schedule(request):
     if request.method=='POST':
          schedule_name=request.POST['schedule_name']
          tbl_schedule.objects.create(schedule_name=schedule_name)
          messages.success(request,"successfully add the bus schedule")
          return render(request,'admins/add_schedule.html')
     else:
          return render(request,'admins/add_schedule.html')
     
def schedule_bus(request):

     first_bus_without_schedule = tbl_bus.objects.filter(Q(schedule_id_id__isnull=True)).first()
    # Handle cases where no buses without schedules are found
     if not first_bus_without_schedule:
        return render(request, 'admins/schedule_bus.html', {'no_buses': True})  # Display a message
     schedules = tbl_schedule.objects.all()  # Fetch all schedules
     context = {'bus': first_bus_without_schedule, 'schedules': schedules}
     return render(request, 'admins/schedule_bus.html', context)

     
def schedule_bus1(request,bus_id):
     if request.method=='POST':
          schedule_id=request.POST['schedule_id']
          print(schedule_id)
          bus=tbl_bus.objects.get(id=bus_id)
          print(bus)
          bus.schedule_id_id=schedule_id
          bus.save()
          # tbl_bus.objects.filter(id=bus_id).update(schedule_id_id=schedule_id)
          messages.success(request,"successfull")
          return redirect(schedule_bus)
     
     else:
         
          a=tbl_bus.objects.get(id=bus_id)

          schedules = tbl_schedule.objects.all()
       
          context = {'a':a, 'schedules': schedules}
          return render(request,'admins/schedule_bus2.html',context)


def view_schedule(request):
     schedules = tbl_schedule.objects.all()
     return render(request,'admins/view_schedule.html',{'schedules':schedules})

def view_schedule1(request,vid):
     x =tbl_bus.objects.filter(schedule_id_id=vid).all()
     return render(request,'admins/view_schedule2.html',{'x':x})

def staff_approve(request):
     staff = Staff.objects.filter(Status=0).select_related('user_ptr')
     return render(request,'admins/staff_approve.html',{'staff':staff})

def staff_approve1(request,aid):
     a=Staff.objects.get(user_ptr_id=aid)
     print(a)
     a.Status=1
     a.save()
     messages.success(request,"Updation successfull")
     # Staff.object.update(Status=1)
     return redirect(staff_approve)
def staff_rejection(request,aid):
     a=Staff.objects.get(user_ptr_id=aid)
     a.delete()
     # messages.success(request,"Updation successfull")
     # # Staff.object.update(Status=1)
     return redirect(staff_approve)

def list_staff(request):
     staff = Staff.objects.filter(Status=1).select_related('user_ptr')
     return render(request,'admins/list_staff.html',{'staff':staff})

# def payment(request):
#      # demo = tbl_smartcard.objects.select_related('user_id')
#      # demo = User.objects.filter(Role=2).select_related('user_id_id')
#      smartcard_data = tbl_smartcard.objects.annotate(
#     user=Subquery(User.objects.filter(pk=OuterRef('user_id')).values('username')))  # Customize fields as needed

#      # a=User.objects.all(demo=id)
#      return render(request,'admins/payment.html',{'smartcard_data':smartcard_data})
     
        
# def payment(request):
#     smartcard_data = tbl_smartcard.objects.annotate(
#         user=Subquery(User.objects.filter(pk=OuterRef('user_id_id')).values('username', 'Cd_type')))  # Customize fields based on your model field names

#     context = {'smartcard_data': smartcard_data}
#     return render(request, 'admins/payment.html', context)

def platinum(request):
     data=User.objects.filter(Cd_type='Platinum')
     return render(request, 'admins/platinum.html',{'data':data})

def gold(request):
     data=User.objects.filter(Cd_type='Gold')
     return render(request, 'admins/platinum.html',{'data':data})

def silver(request):
     data=User.objects.filter(Cd_type='Silver')
     return render(request, 'admins/platinum.html',{'data':data})

def view_user(request):
     user = User.objects.filter(Role=2)
     return render(request,'admins/view_user.html',{'user':user})

def contact_alert(request):
     a=tbl_alert.objects.all()
     return render(request,'admins/contact_alert.html',{'a':a})

def view_complaint(request):
     complaint = tbl_complaint.objects.filter(status='pending').all()
     return render(request,'admins/view_complaint.html',{'complaint':complaint})

def complaint_replay(request,uid,id):
     # if request.method =="POST":
     #      # replay=request.POST['replay']
     #      # print(replay)
     #      # status=request.POST['g1']
     #      # print(status)
     #      print("hiii")
     #      return HttpResponse("not approved")
     #      # return render(request,'admins/complaint_replay.html')
     # else:
          a=User.objects.get(id=uid)
          reply_id = int(id)
          # print("hi:")
          # print(reply_id)
          d=tbl_complaint.objects.filter(id=reply_id).all()
          print(d)
          print(a)
          c=reply_id
          print(c)
          b={
               'a':a,
               'c':c,
               'd':d,
          
          }
          return render(request,'admins/complaint_replay.html',b)

  

def replay(request,id):
     reply_id = int(id)
     print("hi:")
     print(reply_id)
     if request.method=="POST":
          replay=request.POST['replay']
          print(replay)
          print("hgfbdj")
          status=request.POST['g1']
          comp=tbl_complaint.objects.get(id=reply_id)
          sub=comp.subject
          des=comp.description
          userid=comp.user_id_id
          comp.complaint_replay = request.POST['replay']
          comp.status = request.POST['g1']
          comp.save()  # Save changes to database
       
          messages.success(request,"Updation successfull")
          return redirect(view_complaint)
     else:
          return render(request, 'admins/replay.html')









    


#user

def userindex(request):
     if request.method=="POST":
          name=request.POST['name']
          email=request.POST['email']
          address=request.POST['addrs']
          phone=request.POST['phno']
          Dob=request.POST['dob']
          district=request.POST['district']
          state=request.POST['state']
          aadhar=request.POST['aadharno']
          role=request.POST['role']
          uname=request.POST['username']
          pwd=request.POST['pass']
          repws=request.POST['cpass']
          random_number = random.randint(0, 100)
          if role=='2':
               User.objects.create_user(first_name=name,email=email,Address=address,Phone_no=phone,DOB=Dob,District=district,State=state,Aadhar_no=aadhar,Role=role,username=uname,password=pwd)
          else:
               Staff.objects.create_user(first_name=name,email=email,Address=address,Phone_no=phone,DOB=Dob,District=district,State=state,Status=0,Staff_id=random_number,Role=role,username=uname,password=pwd)
          messages.success(request,"registration successfull")
          return render(request,'user/index.html')
                  
          # return HttpResponse('Registration Successfully Completed')
     else:
         return render(request,'user/index.html')
     
def u_header(request):
     return render(request,'user/user.html')

def user_login(request):
     if request.method=="POST":
          username = request.POST['user_name']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None and username==username and password==password:
            print(user.id)
            data=user.id
            login(request, user)
            request.session['user_id']=user.id
            # print('studid')
            return render(request,'user/user.html')
          return HttpResponse("not approved")
     else:
        return render(request,'user/index.html')

def user_logout(request):
     logout(request)
     return render(request,'user/index.html')

def edit_profile(request):
     if request.method=="POST":
          email=request.POST['email']
          address=request.POST['address']
          contact=request.POST['c_no']
          sid = request.session.get('user_id')
          a=User.objects.get(id=sid)
          a.email=email
          a.Address=address
          a.Phone_no=contact
          a.save()
          messages.success(request,"Updation successfull")
          # Staff.object.update(Status=1)
          return render(request,'user/user.html',status=301)
     else:     
          return render(request,'user/edit_profile.html')

def uhome(request):
     return render(request,'user/user.html')

def change_password(request):
     if request.method=="POST":
          old_password=request.POST['old']
          print(old_password)
          new_passwd=request.POST['newpassword']
          print(new_passwd)
          sid = request.session.get('user_id')
          a=User.objects.get(id=sid)
          if a.password!=new_passwd:
               a.set_password(new_passwd)
               a.save()
               # a.password=new_passwd
               # a.save()
               # new_password = request.POST.get('new_password')  # Get new password from form or user input
               # update_password(User, new_passwd)
               messages.success(request,"Updation successfull")
               # Staff.object.update(Status=1)
          else:
              messages.success(request,"old password and new password same") 
          return redirect(uhome)
     else:          
          return render(request,'user/change_password.html')

def view_profile(request):
     if request.method=="POST":
          a_name = request.POST['a_name']
          acc_no = request.POST['acc_no']
          b_name = request.POST['b_name']
          cvv = request.POST['cvv']
          month = request.POST['month']
          year = request.POST['year']
          sid = request.session.get('user_id')
          tbl_bank_account.objects.create(holder_name=a_name,bank_name=b_name,account_number=acc_no,cvv=cvv,month=month,year=year,amount=50000,user_id_id=sid)
          messages.success(request,"Added successfull")
          return redirect(uhome)
     else:
          sid = request.session.get('user_id')
          bank=tbl_bank_name.objects.all()
          print(bank)
          a=User.objects.get(id=sid)
          context={
               'a':a,
               'bank':bank
          }
          return render(request,'user/view_profile.html',context)

def smartcard_apply(request):
     if request.method=="POST":
          a_name = request.POST['name']
          print(a_name)
          card_type=request.POST['card_type']
          print(card_type)
          valid_from=request.POST['v_from']
          print(valid_from)
          district=request.POST['district']
          print(district)
          valid_to=request.POST['vto']
          sid = request.session.get('user_id')
          a=User.objects.get(id=sid)
          a.Cd_type=card_type
          a.save()
          context = {'valid_from': valid_from}
          # return render(request,'user/smartcard_payment.html')
          return redirect(smartcard_payment)
     else:
          today1 = date.today()
          thirty_days_from_now = today1 + timedelta(days=30)
          formatted_date = thirty_days_from_now.strftime("%Y-%m-%d")
          today2 = today1.strftime("%Y-%m-%d")
          sid = request.session.get('user_id')
          a=User.objects.get(id=sid)
          
          time={
               'today2':today2,
               'formatted_date':formatted_date,
               'a':a
          }
         
          return render(request,'user/smartcard_apply.html',time)

def smartcard_payment(request):
     if request.method=='POST':
          sid = request.session.get('user_id')
          today1 = date.today()
          thirty_days_from_now = today1 + timedelta(days=30)
          formatted_date = thirty_days_from_now.strftime("%Y-%m-%d")
          today2 = today1.strftime("%Y-%m-%d")
          card_prize=request.POST['amount']
          tbl_smartcard.objects.create(card_prize=card_prize,valid_from=today2,valid_to=formatted_date,district="",payment_status=1,user_id_id=sid)
          messages.success(request,"")
          # return redirect(u_header)
          return redirect(view_smartcard)
     else:  
          sid = request.session.get('user_id')
          print(sid)
          a=User.objects.get(id=sid)
          b=tbl_bank_account.objects.filter(user_id_id=sid).all()
          print(b)
          c={
               'a':a,
               'b':b
          } 
          return render(request,'user/smartcard_payment.html',c)
     
def view_smartcard(request):
     sid = request.session.get('user_id')
     print(sid)
     # demo=tbl_smartcard.objects.filter(user_id_id=sid).all()
     demo = tbl_smartcard.objects.filter(user_id_id=sid).last()
     a=User.objects.get(id=sid)
     # demo = tbl_smartcard.objects.filter(user_id_id=sid).select_related('user_id').first()

     # user_details = demo.User 
     print(demo)
     return render(request,'user/view_smartcard.html',{'demo':demo,'a':a})

def fare(request):
     buses = tbl_fare.objects.select_related('bus_type_id')
     return render(request,'user/fare.html',{'buses':buses})

def user_view_bus_details(request):
     # bus=tbl_bus.objects.all()
     bus = tbl_bus.objects.select_related('bus_type_id')
     return render(request,'user/user_view_bus_details.html',{'bus':bus})

def user_view_schedule(request):
     schedules = tbl_schedule.objects.all()
     return render(request,'user/user_view_schedule.html',{'schedules':schedules})

def user_view_schedule1(request,vid):
     x =tbl_bus.objects.filter(schedule_id_id=vid).all()
     return render(request,'user/user_view_schedule1.html',{'x':x})

def contact_alerts(request):
     if request.method=='POST':
          email=request.POST['cemail']
          name=request.POST['cname']
          msg=request.POST['message']
          tbl_alert.objects.create(email=email,name=name,message=msg)
          messages.success(request,"")
          # return redirect(u_header)
          return render(request,'user/index.html')

def feedback(request):
     sid = request.session.get('user_id')
     a=User.objects.get(id=sid)
     user_email = a.email 
     print(user_email)
     name=a.first_name
     if request.method=='POST':
          email=user_email
          name=name
          msg=request.POST['msg']
          tbl_alert.objects.create(email=email,name=name,message=msg)
          messages.success(request,"")
          # return redirect(u_header)
          return render(request,'user/user.html')
     else:
          return render(request,'user/feedback.html')
     
def complaint(request):
     sid = request.session.get('user_id')
     if request.method=='POST':
          ctype=request.POST['type']
          description=request.POST['cdes']
          tbl_complaint.objects.create(subject=ctype,description=description,complaint_replay='',status='pending',user_id_id=sid)
          messages.success(request,"Complaint Register successfull")
          return redirect(uhome)
     else:
          return render(request,'user/complaint.html')


def user_complaint_replay(request):
     sid = request.session.get('user_id')
     complaint = tbl_complaint.objects.filter(user_id_id=sid)
     return render(request,'user/user_complaint_replay.html',{'complaint':complaint})
     









#staff

def shome(request):
     return render(request,'staff/shome.html')
def home(request):
     return render(request,'staff/shome.html')


def staffindex(request):
     return render(request,'staff/index.html')

def staff_login(request):
    if request.method=="POST":
        uname=request.POST['name']
        pwd=request.POST['pass']
        
        user=authenticate(request,username=uname,password=pwd)
        print(user)
        if uname=="staff" and pwd=="staff":
          print('hi')
          return redirect(shome)
        print('hi1')
        return HttpResponse("not approved")
    else:
        return render(request,'staff/index.html')
    print('hi2')
    
    
def staff_logout(request):
     return render(request,'staff/index.html')

def staff_list_user(request):
     user = User.objects.filter(Role=2)
     return render(request,'staff/staff_list_user.html',{'user':user})


# def csrf_failure(request, reason=""):
#     ctx = {'message': 'some custom messages'}
#     return render('admin/a.html', ctx)