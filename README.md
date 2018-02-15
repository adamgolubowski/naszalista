# Nasza Lista / Simple gift list
This is a simple gift list. Owners can add items with description and pictures. Users can book items and view bookings.
Main screen:
![main screen](https://github.com/adamgolubowski/naszalista/raw/master/main.PNG)

Booking form:
![booking form](https://github.com/adamgolubowski/naszalista/raw/master/booking.PNG)

## Setup
Add two files to the /naszalista folder:
- secretkey - the file must contain Dajngo secret key
- bookingpwd_secret - put the booking password here. The password will be verified to make a booking.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
