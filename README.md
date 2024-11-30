# googleauth-todo

Thses are the steps to run the project.
<!-- Steps -->
1. Have to install virual environment if already installed then have to create a virtual env
code => python3 -m venv venv

2. Now we have to activa te the vitual environment
code => venv/Scripts/activate

3. After activating the virtual environment ny using the above command we have to install the requiremnts for the user the below command
code => pip install -r requirements.txt

4. After that run the the server onec for checking everything is right of not
code => python3 manage.py runserver

5. To make migrations user the below code
code => python3 manage.py makemigrations

6. To migrate the databse
code => python3 manage.py migrate

7. To deactivate the virtual environment we have to run the below command
code => deactivate

7. ALdo we have to go to the setting and then change the database's user and password what you have given. 

8. The api keys of google is hidden so maybe there are some issue related that.