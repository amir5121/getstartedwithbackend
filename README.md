- Note everything written here is my own opinion
- If you think something is wrong make PR or submit an issue
- Contributions are welcome.

*I hate MS Office so instead of making a PowerPoint I made a `readme.md` file for an online gathering.*

# How to get started with backend development

- [What's Backend?](#whats-backend)
  - [What are the concepts you need to know?](#concepts)
  - [Linux Basic knowledge.](#linux-basic-knowledge)
  - [Learning a language,](#learning-a-language)
  - [Version Control System](#version-control-system)
  - [Database](#database)
  - [Caching](#caching)
  - [Webserver](#webservers)
  - [CI/CD](#cicd)
- [Where should i start](#where-should-i-start)
  - [What is Django](#what-is-django)
  - [Simple app in Django](#simple-app-in-django)



## What's Backend
Basically Frontend is what the user sees and Backend is What user doesn't see but there is more.
- Where the business logic happens, What has happened and What needs to happen?
- Server configuration and Monitoring (Docker, Orchestration tools, Prometheus, Sentry, etc)
- Notification (FCM), Socket, HTTP, etc
- Calculations and long-running tasks
- Logging, Parsing, Dashboards, Business Intelligence tools
- Scaling
- Plus a lot more, Authorization, Load balancing, Networking, DNS, Mail-Server, etc

## Concepts
- How does Internet work? Internet is just a network
- DNS, IP, Route
- Web-server, Firewall, SSH, HTTP
- Request, JSON, SOAP, Graphql 
- Authentication, Authorisation

## Linux basic Knowledge
- Open source Operating system maintained by community
- Basic Networking (netstat, ip, ufw, etc)
- Process Management (htop, ps, etc)
- Storage (du, df, etc) 
- Working with files (SCP, rsync, vim, cp, mv, rm, alias, etc)
- Cron jobs
- Bash scripting

## Learning a language
- Python (Django, Flask, FastApi, etc)
- PHP (Laravel, etc)
- Java (Spring boot, etc)
- Javascript (Nodejs, Express, NextJs, etc)
- Plus a lot more. there is almost no limitation on what language or framework to use. 
- Go, Clojure, C++, Rust, Kotlin, Dart, etc

## Version Control System
- [Git](https://git-scm.com/), SVN
- Repository
- Pulling, Pushing, Cloning,
- (Merge/Pull) Request
- Branching

## Database
- RDB (Relational Database) / No SQL Database
- ORMs
- [Scaling](https://www.freecodecamp.org/news/understanding-database-scaling-patterns/). (Replication / Sharding / Clustering)
- [Postgresql](https://www.postgresql.org/), [MySQL](https://www.mysql.com/)
- [Mongodb](https://www.mongodb.com/), [Redis](https://redis.io/), [Casandra](https://cassandra.apache.org/)

## Caching
- [CDN (Content Delivery Network)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
- [Application Level](https://stackoverflow.com/questions/2963819/why-use-your-application-level-cache-if-database-already-provides-caching)
- [Client Level](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

## Webservers
- [Nginx](https://www.nginx.com/)
- [Apache](https://www.apache.org/)

## CI/CD
- Continuous Integration
- Continuous Deployment
- Testing
- Hard at start good for the long run

# Where should I start
It doesn't matter where you start. What matter is that you start.
- Things to keep in mind when choosing a framework 
    - Choose based on your needs. Some are better at doing something than others
    - Look if it has good documentation
    - Check if it has active community

## What is Django?
- A high-level Python Web framework
- Handling Security, Database (Django ORM), Database Migrations, Forms, ModelViewTemplate
- Fast Development, Extremely Popular, Free and Open Source, Flexible and Customisable
- You can do from simple CMS to Social networks to AI (since it's Python)

## Simple app in Django
- Let's write a phone book app
- It will let you add new contact
- Search through them

# Getting Started with Phone book app
- Install [Python](https://www.python.org/) 

On linux(debian) python2 is installed by default, but I'd recommend installing Python3

    sudo apt-get install python3.6

Then install `Django`

    pip install Django

Then go ahead and start a new project 
*Preferably move to directory for your projects* 

    django-admin startproject phonebook

then add a new app
    
    co phonebook
    python manage.py startapp addressbook

register you app in `phonebook/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'addressbook',
]
```

in addressbook/models.py define your model as
```python
from django.db import models
class Addressbook(models.Model):
    phone_num = models.CharField(max_length=11)
    name = models.CharField(max_length=256)
```

in addressbook/views.py define your view as
```python
from django.views.generic.edit import CreateView
from django.forms import ModelForm
from addressbook.models import Addressbook
class PhonebookForm(ModelForm):
    class Meta:
        model = Addressbook
        exclude = ['id']

class AddressbookView(CreateView):
    form_class = PhonebookForm
    success_url = "/"
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        kwargs["object_list"] = Addressbook.objects.order_by("id")
        return super(AddressbookView, self).get_context_data(**kwargs)
```
and create a file in `templates/index.html` with the following content
```html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send message">
</form>

{% for phonebook in object_list %}
    <p>{{ phonebook.name }} - {{ phonebook.phone_num }}</p>
{% endfor %}
```
Register your template directory in `phonebook/settings.py` 

```python
import os
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"), 
          # by default nothing is registered so register your template directory here
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

then run 

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

open the browser in `127.0.0.1:8000`
You can go ahead and style you view or go further and convert that to JSON endpoint using `djangorestframework`


#My final thoughts:
- You should spend a lot of time learning
- You will never have learned enough  
- It's not the tools that creates a good developer it's 
  - How good of a problem solver you are
  - How patient are you?
  - Facing new challenges
  - Knowing what you need to complete a task.
  - Experience (and this won't come in two or three days it will take years)