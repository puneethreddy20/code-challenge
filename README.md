#How to build and run the application:

To run the application you would need docker installed. Install docker first.
Unzip the package

```
$ cd code-challenge

//Create a docker custom network
$ sudo docker network create --subnet=172.18.0.0/16 mycustomnet

//build a image with dockerfile in the directory which is named as backend
$ sudo docker build -t backend .

//Run the container. Which starts the backend service on port 8080
$ sudo docker run -d -p 8080:8080 --net mycustomnet --ip 172.18.0.10 backend

$ cd greetingAPI

//build a image with dockerfile in the directory which is named as greetingapi
$ sudo docker build -t greetingapi .

//Run the container. Which starts the API service on port 8000
sudo docker run -d -p 8000:8000 --net mycustomnet --ip 172.18.0.20 greetingapi

```

On the host machine open browser and visit http://localhost:8080 .

It displays a page with login form and Register form. You can register for new user and then login.

Default Credentials:
```
username: test

password: test

```
If those doesn't work, please create/register.

Once login, you will be directed to main page/ index page. On the main page, please click on the link which directs to greeting page, where the backend
makes a API call to greetingAPI. It processes and returns the output to backend service. The backend service displays a the greeting page with content from API.

For the above username, the page displays as follows:
```
Greetings! test
```

where test is username.

The mechanism is explained in code documentation below.


#Code Documentation
There are two services involved:

(1) Website Service:

The backend is written  in Golang. It has the following functionalities: 
1. Users can register, login with a username and password, and view a custom greeting page.
2. When a user visits creating page, the backend calls the GreetingAPI with a signed token Json signed web tokens which is valid for 30 mins.
3. Once the login, it creates a cookie for further authentication and is valid for 6 hours.
4. It uses sqlite3 database for storing users information such as useremail, username, and password stored as hash (generated using bcrypt library).


I haven't choosen any big frameworks such as gorilla, martini, because net/http package provides more than enough functions. And I didn't want to make the application heavy by importing many packages.

The website checks for CSRF attacks, XSS and uses secure cookies for authentication purposes, prevents sql injection by preparing statements before hand.
Using mutex/locks to avoid access at same time.

JWT token is signed with a shared secret key, There are basically two ways for signing Token.

One is using shared secret key. This key is used to generate signed token and also validate at other end.

Other is signing with private certificate and validating with public certificate.

Its better to use shared key, I have assumed the key is already present with two services. 

As for unit tests, i have implemented test values for verifying the handlers. It is possible mock the database functions for testing, but as sqlite3 is lightweight, creating dummy test db should be fine.

config.yml consists database url, GreetingAPI url, templates path. It would be easy just to change config file for frequently used values.

(2) Greeting API Service:

It is written in Python and uses Flask framework, which is light weight for implementing API's.

The API has only one end point which validates the JWT tokens using shared key and extracts the username from jwt claims.

And returns Greeting! username to the backend.

(3) Build.

To avoid a lot dependency installation on host machine, i have implemented with containers (docker)

There are two docker files one for Website service and API service. Just build and run as docker container.

#Futher work:
1. With certificates, TLS/SSL (https) can be implemented.
2. Logout can be implemented with clearing the cookies.
3. JWT with public and private certificates.
4. Add Forgot password, Forgot username.
5. Implement Email Functions.



