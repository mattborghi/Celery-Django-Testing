# Projects

## Minimal Celery Configuration

Under ```minimal_celery/```, to initiate the pipenv environment:

```sh
> python -m pipenv shell
```

To install a new package:

```sh
> python -m pipenv install <package>
```

Run celery first by executing our program (```tasks.py```) with the worker argument:

```sh
> celery -A tasks worker -l info
```

or on Windows

```sh
> celery -A tasks worker -l info gevent
```

Then run the main python script:

```sh
> python main.py
```

## Django Celery

Create the project

```sh
> django-admin startproject app
```

create an app

```sh
> python manage.py startapp todos
```

Migrate the results

```sh
> python manage.py migrate
```

Add the todos app to the ```INSTALLED_APPS``` settings.py file.

Add Todos models and run

```sh
> python manage.py makemigrations
> python manage.py migrate
```

to apply the changes.

Add the Todo model to the Django admin app (```todo/admin.py```).

```python
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)
```

And create a superuser

```sh
> python manage.py createsuperuser
```

The url [https://localhost:8000/admin](https://localhost:8000/admin) should redirect to the admin page.

We can always create tests for our app in ```todo/tests.py``` and subsequently run

```sh
> python manage.py test
```

Now, we ARE NOT going to add ```urls.py``` files, views and templates to the app. We are creating a REST API that sends data to the React client to consume it using Django Rest Framework.

Add ```rest_framework``` to our ```INSTALLED_APPS``` settings file.

In the same settings file, add the  following code

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

This code allows anyone to connect to the REST APIs.

We want our URLs to look like ```api/<id>``` so update the ```app/urls.py``` file accordingly.

Also update the ```todos/urls.py``` file as follows

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view())
]
```

Note that we have referenced to views here: ```ListTodo``` and ```DetailTodo```.

In order to return data in JSON format we need a serializer. So add the following code to the ```todos/serializers.py``` file

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description'
        )
```

Our two views will list all our todos and provide detail view of a single todo object. So add the following code to the ```todos/views.py``` file

```python
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializers


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
```

Then we can go to [http://localhost:8000/api](http://localhost:8000/api) to see our List Todo view. This contains actual JSON available at this point. To see also the Detail Todo views we can go to [http://localhost:8000/api/1/](http://localhost:8000/api/1/) for example.

Finally, add ```django-cors-headers``` to our app. First, add it to ```INSTALLED_APPS```. Add to new middlewear at the top and create a ```CORS_ORIGIN_WHITELIST```.
