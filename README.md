# CalipsoPlus Backend

The aim of this project is to provide a backend RESTful service for the CalipsoPlus JRA2 Demonstrator project.

### Contents

*  [Architecture](#architecture)
    *  [External components](#external-components)
        *  [Guacamole](#guacamole)
        *  [Local authentication provider](#local-authentication-provider)
        *  [Umbrella](#umbrella)
    *  [Versions and major dependencies](#versions-and-major-dependencies)
*  [Requirements](#requirements)
*  [Build & Development](#build-&-development)
    *  [Database configuration](#database-configuration)
    *  [Migrations](#migrations)
    *  [External component configuration](#external-component-configuration)
        *  [Local authentication](#local-authentication)
        *  [Umbrella authentication](#umbrella-authentication)
        *  [Dynamic data retrieval](#dynamic-data-retrieval)
    *  [Run](#run)
*  [Testing](#testing)
*  [Deploy](#deploy)
    *  [Configure uswgi](#configure-uswgi)
    *  [Configure Apache](#configure-apache)
    *  [Restart the service](#restart-the-service)
---
## Architecture

This backend is built using the [Django](https://www.djangoproject.com/) and [Django REST](https://www.django-rest-framework.org/) frameworks, running over Python 3.6 (Python 3.7 and higher should also be supported). You can refer to the documentation of the respective frameworks for more information.

Additionally, this application is configured to use a MySQL database (versions 5.6 and higher are supported). Other database backends are also supported by the Django framework (PostgreSQL, Oracle, SQLite), but require changes in the settings of the application. Check the relevant [Django documentation](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#database-setup) for further details.

### External components
There are several services with which this backend may interact that are not part of this repository.

#### Guacamole
To connect with the resources (Docker containers, virtual machines...) requisitioned by the application users, this application interfaces with an [Apache Guacamole](https://guacamole.apache.org/) service, which provides VNC or RDP connections through HTTP. 

The only settings required in the backend segment is the connection to the database of your Guacamole instance, which will be used to keep track of the active resources and their access credentials (check the [Database configuration](#database-configuration) section).

#### Local data provider
This application can be configured to retrieve information about the experiments performed in the facility dynamically via a REST API interface from a provider (eg.: a Web User Office application). Check further details in the [Dynamic data retrieval](#dynamic-data-retrieval) section of this document. The interface the provider must implement is documented in the [API.md](API.md) file of this repository.

#### Local authentication provider
This application is designed to interface via a REST API with an existing authentication service of the facility. Check further details in the [Local authentication](#local-authentication) of this document. As before, the interface the provider must implement is documented in the [API.md](API.md) file of this repository.

#### Umbrella

In addition to local authentication schemes implemented in each facility, this application is also designed to provide access via the [Umbrella](https://umbrellaid.org/) federated authentication service. The relevant application settings to enable Umbrella support are detailed in the [Umbrella authentication](#umbrella-authentication) section of this document.
(TODO: Reference to documentation and Shibboleth)

## Requirements

(TODO: detail specs, maybe use a table?)

For a minimal deployment of the backend segment of this application, the following resources are required:

*  An application server to host the Django backend (may also host the frontend application).
*  A database server.
*  A server running the Shibboleth identity provider (required to support the Umbrella federated authentication system).
*  A server running Guacamole (TODO: depending on usage, may share the application server? To check)
*  A server to use as host to the docker containers the users may requisition.

## Build & Development

The project has been developed in Python using Django Framework and the source code can be found in [CELLS' Git repository](https://git.cells.es/mis/calipsoplus-backend).

The user will need to install Python 3+, python-pip and python-virtualenv. Some other packages could be required.

```bash
mkdir calipsoplus & cd calipsoplus
mkdir logs
virtualenv ~/.virtualenvs/calipsoenv/bin/activate
git clone git@git.cells.es:mis/calipsoplus-backend.git -b develop backend
env/bin/pip install -r calipsoplus/requirements.txt
```

### Database configuration

By default, the application settings are configured to use a MySQL database server, and we need a new schema to manage app's data, with the necessary user and host credentials to manage it. This document will follow default configuration settings.

```sql
CREATE DATABASE `calipsoplus`;
```

```bash
cd calipsoplus
mkdir config & cd config
mkdir database & cd database
vi guacamole.cnf #guacamole db
vi default.cnf #calipso db
```

Add the following content to the **default.cnf** file to configure the connection to the application database
```bash
[client]
database = calipsoplus
host = localhost
port = 3306
user = *****
password = *****
default-character-set = utf8
```
Add the following content to the **guacamole.cnf** file to configure the connection to the Apache Guacamole database
```bash
[client]
database = guacamoledb
host = localhost
port = 3306
user = *****
password = *****
default-character-set = utf8
```

Set **default.cnf** and **guacamole.cnf** files as read only

```bash
chmod 555 default.cnf
chmod 555 guacamole.cnf
```

### Migrations
The following command will apply the required migrations to create/update the database schema to the latest version:
```
env/bin/python backend/manage.py migrate --settings=calipsoplus.settings_[local|test|demo|prod]
```

### External component configuration
This section details the settings that need to be modified in order to properly configure connections to the external components described in the [Architecture](#external-components) section.

#### Local authentication
In the **calipsoplus/settings_calypso.py** file, you can set whether local authentication is allowed or not. Set the "ALLOW_LOCAL_AUTHENTICATION" setting to 1 to enable this feature.

The next step to take to configure local authentication is to define the login endpoint. In the **calipsoplus/settings_[local|test|demo|prod].py** file (choose the one you will use according to your environment), find the "BACKEND_UO_LOGIN" setting and replace the URL with the endpoint of your provider. This endpoint must implement the expected REST API as described in the [API.md](API.md) file.

(TODO: HTTP AUTH and service login)
#### Umbrella authentication
In order to enable support for the Umbrella federated authentication service, set the relevant endpoints of your Shibboleth identity provider in the **calipsoplus/settings_[local|test|demo|prod].py** file (choose the one you will use according to your environment). Two endpoints need to be set: "UMBRELLA_LOGIN" and "UMBRELLA_LOGOUT".

Additionally, an endpoint must be set for a REST service that will authenticate the Umbrella hash against your user records, "BACKEND_UO_HASH". This endpoint must implement the expected REST API as described in the [API.md](API.md) file.
#### Dynamic data retrieval
This application can be set to dynamically retrieve data of the experiments performed in the site from a REST service. To enable this feature, go to **calipsoplus/settings_calypso.py** and set the "DYNAMIC_EXPERIMENTS_DATA_RETRIEVAL" setting to one.

The endpoint used to retrieve the experiment data is defined in the **calipsoplus/settings_[local|test|demo|prod].py** file (choose the one you will use according to your environment) as the "DYNAMIC_EXPERIMENTS_DATA_RETRIEVAL_ENDPOINT" setting. This endpoint must implement the expected REST API as described in the [API.md](API.md) file.

### Run

Once the environment and the database are configured...

```bash
./manage.py runserver 127.0.0.1:8000 settings=calipsoplus.settings_local
```

The service should be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Testing

The application has its own unit testing settings, which will create a mock database using SQLite and will store it in local memory. This way the testing is faster than using MySQL.

```bash
cd calipsoplus
source ~/.virtualenvs/calipsoenv/bin/activate
./manage.py test --settings=calipsoplus.settings_unittests
```

## Deploy

Follow the same steps as in the **Build & Development** section except the **Run** subsection

### Configure uswgi

Go to uwsgi's directory which contains the apps-available and apps-enabled directories. We will name it UWSGI_DIR.

First of all, review the calipsoplus-backend.ini file to be sure every property is set correctly.

After that, we need to edit the configuration file with correct environment configuration in terms of project location, Django's environment settings and database configuration.

### Configure Apache

Go to Apache's directory which contains the apps-available and apps-enabled directories. We will name it APACHE_DIR.

```bash
cd APACHE_DIR/apps-available
cp SOURCE_DIR/settings/config/apache/calipsoplus-backend.conf .
cd ../apps-enabled
ln -s ../apps-available/calipsoplus-backend.conf XX-calipsoplus-backend.conf
```

### Restart the service

```bash
sudo service apache2 restart
```