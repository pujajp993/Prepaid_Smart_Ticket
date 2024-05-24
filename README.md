PREPAID SMART TICKET

Prepaid Smart Ticket using SQLite,Python Django Framework,HTML,CSS,Bootstrap

Description of the project :
        The project entitled as “PREPAID SMART TICKET” is a project for students for developing prototypes of KSRTC season ticket booking system. The project aims to provide
an effective solution of maintaining bus ticket using various cards categorized as platinum, gold and silver. The system has three logins one for user and other two for admin and staff.The user is provided with a website he/she can login to the corresponding website, it consists of details of validity of the card and the user can refill their account and extend the validity when the time expires. Thus, while travelling the users only need to show these cards to the conductor. The cards are categorized based on: using platinum cards users can travel everywhere in Kerala with fast, superfast, AC Volvo bus services and all other services of worth 3000, using gold cards users can travel in Kerala with ordinary and limited services of worth 1500 and using silver cards users can travel only within a district with ordinary and limited services of worth 1000. The admin module is handled by the admin who will look after all the activities taking place in the system and he will add bus, fare of bus, bus schedule etc.The staff can view the booking, cancellation details etc.

Modules:
There are 3 modules in this project. Admin module, User module, and Staff module.
1. Functions of administrative module:
        a. Add bus type:
                In this case admin can add bus type like Ordinary, Fast, Super-fast, Volvo,Super express, Super deluxe etc.
        b. Add bus details:
                In this case admin can add bus number, bus type, source, starting time,destination, and arrival time.
        c. View bus details:
                Admin can view all the bus details add on the database with the details of bus number, bus type, source, departure time, destination, arrival time and the                   admin can edit and delete those bus details.
        d. Add fare:
                Admin can add the fare details of bus by including the bus type and minimum charge of bus in rupees.
        e. View fare:
                Admin can view the fare details of bus with the bus type and minimum charge of buses in rupees and he can also edit and delete those details.
        f. Add schedule:
                Admin can add bus schedule like Kollam schedule, Trivandrum schedule likewise i.e. schedule the bus based upon the source station of bus.
        g. Schedule the bus:
                Admin can schedule the bus based on bus number, bus type, source,destination, start time, end time, schedule to which shows the bus belongs to which schedule                 example like Kollam schedule, Trivandrum schedule likewise
        h. View schedule:
                Admin can view the schedule of buses based upon their corresponding schedule with details of bus number, bus type, source, departure time,destination,arrival                 time and he can also edit and delete the bus schedule.
        i. View smart card uses:
                Admin can view users and also, he can view the platinum card user, gold card users, sliver card users separately. He can delete users.
        j. Staff:
                Admin can approve a staff, disapprove a staff and can view the details of staff with name, address, email id, contact, district, state.
        k. Complaint:
                Admin can view the user’s complaints and can also replay back.
        l. View feedback and contact details:
                Admin can view the messages from the users.
        m. View contact form:
                Admin can view the contact form send by use users in notification section
2. Functions of administrative module:
   a. Registration:
        First of all, user want to register on the site. Then using the username and
password they can login the site and can-do further activity
b. My profile:
Users can add their details to my profile section which include their
personal information from time of registration and also include details to enter
the account information such as account holder, account name, bank name etc.
c. Apply:
After entering all profile details, he/she can apply for the smart cards like
platinum, gold, silver. Here he can view the validity of the card and after the
payment users will receive a smart ticket layout which include the details of
validity and type of card.
d. Ticket-Future Enhancement:
Platinum users can book the bus by viewing bus _no, bus _type, source,
destination, arrival time, departure time and also users can cancel the bus.
e. Bus details:
Users can view the details of bus like its fare details, schedule details and all
available bus details. In fare details users can view all the buses minimum
charges in rupees, in schedule details he can view the bus details based on the
corresponding schedule and in bus details he can view all available buses.f. Complaint:
User can register five types of complaints like generic complaint,
misbehavior of conductor, money not refund, delayed services of bus, ladies
seat concession and also can add complaint description.
g. Complaint replay:
User can view the complaint replay from the admin
h. Feedback:
User can view the feedbacks from the admin.
4. Functions of staff module
a. Booking details and generate bill-Future Enhancement:
In this case staff can view the bus booking details of users and can also
view bill for each booking.
b. View user details:
Staff can view the user details who are applied for each type of smart card
and also can delete the details.
c. View Feedback:
Staff can view feedback send by users.

Prerequisites
1. Install DB Browser
2. Any Editor (Preferably Visual Studio Code)
3. Any web browser with latest version
   
Languages and Technologies used
1. HTML5/CSS3
2. JavaScript (to create dynamically updating content)
3. Bootstrap (An HTML, CSS, and JS library)
4. Python Django framework
5. SQLite

Steps to run the project in your machine
1. Download and install DB Browser in your machine
2. Clone or download the repository
3. Extract all the files
4. Migrate the database (py manage.py makemigrations and py manage.py migrate)
5. Run the project (py manage.py runserver)
