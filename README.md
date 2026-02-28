Fitness Tracker API
Overview

The Fitness Tracker API is a backend project built with Django and Django REST Framework. It allows users to register, log in, and manage their fitness activities. Users can create, view, update, and delete workouts, and track their activity history securely.

This project focuses on authentication, database management, API design, and deployment.

Features

User registration and authentication (JWT)

Create, read, update, and delete workouts

Users can only manage their own activities

Activity filtering (by date and activity type)

Pagination for workout lists

Activity metrics summary (total duration, distance, calories)

Custom homepage template

Deployment on PythonAnywhere

Technologies Used

Python

Django

Django REST Framework

SimpleJWT

SQLite

API Endpoints
Authentication

POST /api/token/
Get access and refresh tokens.

Users

GET /api/users/
POST /api/users/

Workouts

GET /api/workouts/
POST /api/workouts/
GET /api/workouts/{id}/
PUT /api/workouts/{id}/
DELETE /api/workouts/{id}/

Metrics

GET /api/workouts/metrics/
Returns total duration, distance, and calories burned.


The project is deployed on PythonAnywhere.
Deployment included setting up a virtual environment, installing dependencies, configuring the WSGI file, running migrations, and setting allowed hosts.

Author

Oluwadamilola Olaniyan
