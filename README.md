# mysite

As a class, this is where we'll start for Session 09.

To get this set up on your machine:

1. Fork and clone the repository
2. Open a command prompt and activate your djangoenv
3. Navigate to the directory containing manage.py
4. Create a database using the model
`$ python manage.py migrate`
5. Create a super user - follow the instructions to finish creating super user
`$ python manage.py createsuperuser`
6. Start the server
`$ python manage.py runserver`
7. In your browser, open localhost:8000 to see the application


#Changes made since the end of Session 08:

*myblog/admin.py*

1. Created PostAdmin and CategoryAdmin classes
2. Added make_published function
3. Added CategorizationInline class
2. Registered Post and Category classes with their new Admin classes

*myblog/models.py*

1. Added a metaclass to Categories to make the name in the admin appear as "Categories" instead of "Categorys"
2. Added __unicode__ methods to both Post and Category classes
