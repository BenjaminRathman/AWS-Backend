Database - PostgreSQL run through AWS RDS

Authentication and Security - Firebase(Google)

Cloud - We are going to be running the api on a ec2 instance to start and then switch to fargate 

API - Fast API

We need to implement docker 

















detailed flow of what is happening 



 Full Flow with Detailed Explanation
🔹 Step 1: [Mobile App]
The user interacts with your mobile application. At this point:

The app is not yet authenticated.

It likely shows a login screen.

Your app is already set up with the Firebase SDK (Android/iOS) for authentication.

🔹 Step 2: [Firebase Auth for login]
The app uses Firebase Authentication to log the user in.

Depending on the auth method you choose, the user:

Enters email/password

Logs in with Google/Apple/Facebook

Uses a phone number with OTP

Firebase SDK handles this and on successful login:

Firebase verifies the user credentials

Firebase issues an ID Token (a JWT = JSON Web Token) that:

Proves the user is authenticated

Contains the user’s UID, email, and claims

Your app now holds this token in memory.

🔹 Step 3: [Gets Firebase ID Token]
The ID token is just a string, usually starting with eyJhbGciOi....

The app stores this token securely (e.g. in memory or secure storage) and attaches it to each HTTP request to your backend.

For example:

http
Copy
Edit
GET /protected-resource
Authorization: Bearer eyJhbGciOi...
🔹 Step 4: [Sends token to FastAPI backend on AWS]
This is where your FastAPI backend (hosted on EC2, Fargate, etc.) receives the request.

It:

Extracts the Authorization header

Pulls the ID token

Calls Firebase Admin SDK or Google’s token verification endpoint to validate it

Why verify?

To make sure the token is real and not expired or tampered with

To get the user’s identity (UID, email)

🔹 Step 5: [FastAPI verifies token with Firebase]
FastAPI runs something like this under the hood:

python
Copy
Edit
decoded_token = auth.verify_id_token(id_token)
user_id = decoded_token["uid"]
If verification fails:

FastAPI returns HTTP 401 Unauthorized

If successful:

FastAPI now trusts this user identity

You can authorize based on user roles, UID, or claims

You can also add middleware to do this automatically for all routes.

🔹 Step 6: [FastAPI queries PostgreSQL]
Now that the user is verified:

FastAPI:

Opens a connection to your PostgreSQL database hosted on Amazon RDS

Runs a query like:

sql
Copy
Edit
SELECT * FROM messages WHERE user_id = 'abc123';
Or maybe inserts data:

sql
Copy
Edit
INSERT INTO orders (user_id, item, total) VALUES ('abc123', 'Socks', 19.99);
You can use libraries like psycopg2, SQLAlchemy, or asyncpg.

🔹 Step 7: [Returns JSON to Mobile App]
FastAPI wraps the result into a JSON response:

json
Copy
Edit
{
  "orders": [
    {"item": "Socks", "total": 19.99},
    {"item": "Hat", "total": 14.99}
  ]
}
Your mobile app:

Parses the JSON

Displays it to the user in a UI component

If the token was invalid, the app could show a login prompt or error.

🔐 Security Considerations:
Firebase tokens expire ~1 hour after issuance. App may need to refresh them.

Always use HTTPS.

Use firewall/VPC security groups to lock down RDS access.

Token verification should happen on every API request unless using session cookies.




Ben's Words:

In the front end react native code we will have js scripts that handle calling and referencing the api

When the user logins in Firebase issues a token if the app session is restored we find the token in memory if session is expired the user is prompted to login again and then we can give them a new token. (This token is needed in api requests) 

We have an Api endpoint running in a ec2 instance that receives the requests made by our js. The Api will be made using fast api and built with python. We basically just upload code to ec2 

When the api is called the api will then call a function that does the query logic (for organization) 

This query logic function should call another function that handles db connection 

The database will always be "listening" because it is running on aws rds 

So three functions 

one for listening to the app 

one handling query logic 

one making connection to the db 


✔️ API endpoint:
Handles routing + token verification

Calls a query logic function (e.g. get_user_profile(uid))

✔️ Query logic function:
Does business logic (e.g., which user to fetch, what data to include)

Calls a database access function (e.g. get_db_connection() or db.query(...))

✔️ Database function:
Establishes connection to AWS RDS PostgreSQL

Executes raw SQL or ORM query

Returns result to query logic

Data is basically returned in a return statement

 Here’s the Flow (from DB to App)
Your FastAPI endpoint receives a request from the app

It:

Verifies the Firebase token

Calls a query function → which gets data from PostgreSQL

The result is returned up through the function chain

Finally, the endpoint returns a Python dict

FastAPI auto-converts that into JSON

That JSON is sent back to the app as the HTTP response body

We then write java script to parse the JSON into how we need it 


SO 

JS in APP makes API RQ -> API ENDPOINT hears it (because it is being run on ec2) -> This calls 2 more functions that are being hosted in ec2 one for query logic and another for database connection -> the result is then returned as json -> a js script parses the json to be used in the react native code 

The phone is essentially its own server and compiles all of the react code by itself so it can host the ui and make api requests 