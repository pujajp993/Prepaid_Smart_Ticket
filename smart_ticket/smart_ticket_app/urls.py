from django.urls import path
from smart_ticket_app import views

urlpatterns = [
    
    #ADMIN

    path('',views.index,name='index'), #admin-admins/index
    path('a',views.aheader,name='aheader'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('bustype',views.bustype,name='bustype'),
    path('add_bus_details',views.add_bus_details,name='add_bus_details'),
    path('view_bus_details',views.view_bus_details,name='view_bus_details'),
    path('edit_bus/<int:eid>',views.edit_bus,name='edit_bus'),
    path('edit_bus1/<int:eid>',views.edit_bus1,name='edit_bus1'),
    path('delete_bus/<int:did>',views.delete_bus,name='delete_bus'),
    path('add_fare',views.add_fare,name='add_fare'),
    path('view_fare',views.view_fare,name='views_fare'),
    path('add_schedule',views.add_schedule,name='add_schedule'),
    path('schedule_bus',views.schedule_bus,name='schedule_bus'),
    path('schedule_bus1/<int:bus_id>',views.schedule_bus1,name='schedule_bus1'),
    path('view_schedule',views.view_schedule,name='view_schedule'),
    path('view_schedule1/<int:vid>',views.view_schedule1,name='view_schedule1'),
    path('staff_approve',views.staff_approve,name='staff_approve'),
    path('staff_approve1/<int:aid>',views.staff_approve1,name='staff_approve1'),
    path('staff_rejection/<int:aid>',views.staff_rejection,name='staff_rejection'),
    path('list_staff',views.list_staff,name='list_staff'),
    # path('payment',views.payment,name='payment'),
    path('platinum',views.platinum,name='platinum'),
    path('gold',views.gold,name='plgoldatinum'),
    path('silver',views.silver,name='silver'),
    path('view_user',views.view_user,name='view_user'),
    path('contact_alert',views.contact_alert,name='contact_alert'),
    path('view_complaint',views.view_complaint,name='view_complaint'),
    path('complaint_replay/<int:uid>/<int:id>',views.complaint_replay,name='complaint_replay'),
    path('replay/<int:id>',views.replay,name='replay'),
   


    #USER

    path('user/index',views.userindex,name='userindex'),
    path('user/u_header',views.u_header,name='u_header'),
    path('user/user_login',views.user_login,name='user_login'),
    path('user/user_logout',views.user_logout,name='user_logout'),
    path('user/edit_profile',views.edit_profile,name='edit_profile'),
    path('user/edit_profile',views.edit_profile,name='edit_profile'),
    path('user/uhome',views.uhome,name='uhome'),
    path('user/change_password',views.change_password,name='change_password'),
    path('user/view_profile',views.view_profile,name='view_profile'),
    path('user/smartcard_apply/',views.smartcard_apply,name='smartcard_apply'),
    path('user/smartcard_payment',views.smartcard_payment,name='smartcard_payment'),
    path('user/view_smartcard',views.view_smartcard,name='view_smartcard'),
    path('user/fare',views.fare,name='fare'),
    path('user/user_view_bus_details',views.user_view_bus_details,name='user_view_bus_details'),
    path('user/user_view_schedule',views.user_view_schedule,name='user_view_schedule'),
    path('user/user_view_schedule1/<int:vid>',views.user_view_schedule1,name='user_view_schedule1'),
    path('user/contact_alerts',views.contact_alerts,name='contact_alerts'),
    path('user/feedback',views.feedback,name='feedback'),
    path('user/complaint',views.complaint,name='complaint'),
    path('user/user_complaint_replay',views.user_complaint_replay,name='user_complaint_replay'),


    #STAFF
    path('staff/index',views.staffindex,name='index'),
    path('staff/shome',views.shome,name='shome'),
    path('staff/home',views.home,name='home'),
    path('staff/staff_login',views.staff_login,name='staff_login'),
    path('staff/staff_logout',views.staff_logout,name='staff_logout'),
    path('staff/staff_list_user',views.staff_list_user,name='staff_list_user'),
   

]