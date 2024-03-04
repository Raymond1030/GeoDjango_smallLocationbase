# GeoDjango-smallLocationbase

A Django Geo-server for my [CloudMapMobleMap](https://github.com/Raymond1030/CloudMapMobileApp)

Database: PostgreSQL

Set Your Default Database `NAME, USER,PASSWORD,HOST` in [setting.py](https://github.com/Raymond1030/GeoDjango_smallLocationbase/blob/main/MobileCloud/MobileCloud/settings.py)


## Prerequisites

#### Install Django:

`pip install Django`

or

`conda install Django`

#### Install psycopg2:

`pip install psycopg2-binary`

or

`conda install psycopg2-binary`

------

### Start the Server

```
cd 'YourPath'\MobileCloud
```

If you start in LAN network:

```
python manage.py runserver 0.0.0.0:8080
python manage.py migrate 
```



