	School Management API

############## END POINTS ############################

Note:- Used Default db sqllite which is attached with the project

Note:- create a virtual environment using 
	"python3.6 -m venv venv"
	after this run pip install -r requirments.txt

1. To Add a class in db 
	method = POST  url = http://127.0.0.1:8000/student/classes/
	Post body = {"class_name":"Lkg"}

2. To Get Class Details
	method = POST  url = http://127.0.0.1:8000/student/classes/
	response body = {
			    "error": "",
			    "data": [
				{
				    "class_name": "Nursery",
				    "slug": "nursery"
				},
				{
				    "class_name": "Lkg",
				    "slug": "lkg"
				}
			    ]
			}

3. To Register Student 
	method = Post  url = http://127.0.0.1:8000/student/student-register/

	Note:- all fields are mandatory and used form-data to hit the api with student image
	      fields = ['first_name','last_name','email','password','date_of_birth','class_name','student_image']

	default status is false for every student

4. Admin Panel
	url = http://127.0.0.1:8000/admin
	used django admin panel 
	username = clavax
	password = clavax

5. Student Login 

	method = Post   url = http://127.0.0.1:8000/student/login/
	request body = {
			  "password": "",
			  "email": ""
			}

	response body = {"token":}

	Note:- If student status is false so it will show account is inactive
	       If student status is true then he will get a token in response



