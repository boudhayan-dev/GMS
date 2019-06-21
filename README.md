# GMS

Apply the following steps to replicate the environment.

* Clone repo 

    ```
    git clone <<link>>
    cd GMS
    ```

*  Create and activate virtual environment

    ```
    virtualenv venv
    cd venv/Scripts
    activate
    cd ../..
    cd gym
    ```

*  Create a SuperUser

    ```
    python manage.py createsuperuser
    ```

* Apply all migrations

    ```
    python manage.py migrate
    ```
    If you want to migrate a particular app only (ex- gym_owner), apply this -

    ```
    python manage.py makemigrations gym_owner
    python manage.py migrate gym_owner
    ```

* Start server 
    ```
    python manage.py runserver 0.0.0.0:8000
    ```
    
* Go to /owner/registration and create new user + gym. 
  For other artifacts, use the admin panel for now

### Status

<strong>Model - </strong> All the models have been defined in - gym_owner, gym_customer and gym_payment.

<strong>Views - </strong> The following routes have been defined in gym_owner app -

* /owner/dashboard - Currently empty. Requires Login.
* /owner/login - Login View
* /owner/logout - Logout view
* /owner/registration - Gym and Owner onboarding

