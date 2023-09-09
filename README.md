
# ECM-backend

Evaluation-Contract management App is a Django project to manage the contracts. 

You can create contract with desired documents. Also you can edit(update) or delete contracts and see a list of your contracts in home page.

Also it has a user-managemnet app that you can define new users to system or edit your profile.


## Deployment

After cloning the repository you need to install python virtual environment

```bash 
  pip install virtualenv
```

Then you should create a python virtual environment. Run the following command at root directory

```bash 
  python -m venv .venv
```
After that activate the virtual environment

```bash 
  .\.venv\Scripts\activate 
```

Then we need to install dependencies

```bash 
  pip install -r .\requirements.txt
```
This version has migrations and tables so you just need to runserver

```bash 
  python manage.py runserver
```
This will run django server at localhost:8000 . You can also run it on local network by this command 

```bash 
  python manage.py runserver YOUR-NETWORK-IP:DESIRED-PORT
```
For example if your network ip is 192.168.42.114 and you want the 8000 port to be served, run this

```bash 
  python manage.py runserver 192.168.42.114:8000
```
This is the IP you should give to frontend.

## Notes
- To talk to this backend you should also deploy [ECM-frontend](https://github.com/MohammadRezaAsgari/ECM-frontend) first and set this backend URL(IP) to it.
- To run django server on local network or other networks you should edit last two lines at /setting.py and set the CORS_ALLOWED_ORIGINS and ALLOWED_HOSTS to the IP in order to allow the requests.
- This project has an existing admin user with username = 'superuser' and password = '12345678' 

