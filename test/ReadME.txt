Basic Requirement for project setup
1. Python(2.7 or 3.5 work with both)

Steps for setting up the project
1. Create Virtual Environment(virtualenv env)
2. Place the project folder(test_assign) inside virtual environment
3. Activate virtual Environment.
4. Run command- pip install -r Requirements.txt
5. Requirements.txt file contains all the required packages for the project set
6. Database user- Sqlite(Included in the project Setup)
7. Run python manage.py runserver
8. Hit localhost:8000/admin in brower.


Steps to check Each Task-
task 1- Create API for searching the Users. 
	url- localhost:8000/api/user_search/
	Click filter button to search the user by firstname,lastname, email, data, username

Task 2- Documentation only(Explaination as per my assumption)

Task 3- As any API call is made, store all user related info in a Django table.
	url- http://localhost:8000/api/add_user/
	You can add user but that user wont have access to Django-Admin
	User Name must be Unique.

Task 4- Admin Panel, with image if available as thumbnail.
	URL- http://localhost:8000/admin/
	superuser credentials-
	username- sachin
	password- Admin@123
	or create super user by command- python manage.py createsuperuser
	go to image display section in admin dashboard. list page will open with thumbnails of image added with description

Task 5- In Admin Panel users can be searched on the basis date of added, there email.
	URL- http://localhost:8000/admin/
	Click on Users Section and you can search user by email, fname, Lname, lastlogin, datejoined

Task 6- Django Admin Report
	URL- http://localhost:8000/admin/
	     http://localhost:8000/admin/report_builder/report/
	Click Reports on Django admin dashboard.
	List of report will open
	Default date range is added for making the report so you can download directly from the list page.
	If you want to change the report date, you can edit that report and change the date or add new report for future reference.

Please let me know if you have any concern or confusion.
