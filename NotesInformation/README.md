We have only been thinking about userside we also need a login side for the bar so they can input things  

(https://docs.google.com/spreadsheets/d/10e4lAYXwBNQuj3MjdLekqqpzzNDVwylKzLZStJRgMGU/edit?gid=0#gid=0)

possible name: Bar Buddy?

Deliverable idea pre-ordering drinks with an integrated loyalty system 

## MVP

# UI - 

Page 1 (info page) 

based on selected location the user sees:
info about daily specials at partnered bars 
maybe the bar comes to us to promote a one time special (maybe we charge here)

page 2 (ordering page)
The user sees all partnered bars 
when user clicks on a bar the user sees list of drinks that can be bought before the bar opens at a discount (options on pre-ordering menu worked out in advance with bar)
Then there is a max amount of points that the user can get per bar (resets everyday) this can then be redeemed for a free drink (loyalty program, need to agree with each bar on this)

Looking at having two incentives for users to pre-order drinks: 1. Beers will be slightly cheaper (somewhere 5-20%???) 2. Loyalty program givs customers free beers eventually
*pre-ordered drinks expire when that bar closes for the day

Page 3 (social tab)

Add friends and send them friend requests by typing in their username
You can see where your friends have pre-ordered beers and leave comments underneath these announcments ??
You can gift your friends a pre-ordered beer/special 
You can go to freind's accounts and push a button which sends a push notification to their device which says "XXXXX invited you to drink!"  ???

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Vendor Side UI:
When first creating an account, you can select either "I'm a customer" or "I'm a vendor"
If you select "I'm a Vendor", we (somehow) link you up to your bar and give you a page where you can upload/update specials, and update prices for the pre-ordering service


# auth0 for login -
Handles creating an account with user inputting unique email, unique username, and password
Auth0 shares with us each account's username and email, they keep PW in their own database

# Stripe to handle transactions

