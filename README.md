# cyber-project, security vulnerabilities

### Installation
Clone or download zip from the github page, install django if not already installed.

The code should be ready to use, you can run the code in terminal by running \
`python3 manage.py runserver`

### About the code
The code is based on the Django Basics tutorial found here (multiple parts): \
https://www.pythontutorial.net/django-tutorial/getting-started-with-django/  \
The source code for the tutorial can be downloaded using this link:\
https://www.pythontutorial.net/wp-content/uploads/2023/01/django_project_11.zip

Not all parts of the code have been applied in this app, but it is mostly a one to one copy in construct and naming. \
The main difference being that posts viewable to all users are changed to messages only viewable to a specified user. 

The idea has been to “break” the code as much as possible to create security issues. Since django has a lot of built-in safety features, parts of the code have been “rewritten” to create these vulnerabilities. So this project turned more into fighting against djangos security measures, rather than showcasing already existing security vulnerabilities. I’m sure it would have been easier to write the code from scratch without using django rather than trying to work around it. There are also a lot of deliberate bad coding practices in the code to make the vulnerabilities easier to showcase.
In the essay submitted I present simple ways to fix the code, but once again note that many of the issues would not exist if they were not intentionally made. Many of the vulnerabilities and their fixes are based on the course exercises.

In the app you can:
- register as user
- login as user
- logout as user
- send message to another user
- delete messages you have received


The code has the following security vulnerabilities referencing the OWASP Top Ten Application Security Risks 2017 \
https://owasp.org/www-project-top-ten/2017/Top_10: 
- Injection
- Broken authentication
- Sensitive data exposure
- Broken access control
- Cross-site scripting
- Insufficient logging and monitoring

(maybe also “Using components with known vulnerabilities”, considering the code that is used to bypass django safety measures)

### Other things to note:
It is a bad practice having no way to reset passwords, since now if a user's password get’s leaked there is no way for the user to change it. The code itself is also missing a lot of error handling, and is not the best written even without the security flaws.

Any other security issues that the app may or does have, have gone unnoticed due to the writer's limited security knowledge or just pure oversight.
