### Windows

eval "$(docker-machine env default)"
docker-compose run -d web django-admin.py startproject composeexample .
sudo chown -R $USER:$USER .
nano composeexample/settings.py
DATABASES = {      
'default': {
 'ENGINE': 'django.db.backends.postgresql_psycopg2',          
 'NAME': 'postgres',
 'USER': 'postgres',
 'HOST': 'db',
 'PORT': 5432,      
 }
}
docker-compose up -d

If build parameter is used in docker-compose.yml it is not neccesary to build 
compose_django image

It is possible that in the first running of docker-compose up the application gets stuck.
One fix is to run docker-compose stop and run again docker-compose up
