# Sanias Art Gallery
This project was created for my partner as part of her university degree. She needed a website to showcase her work as an artist, and to allow people to view, comment and purchase pieces. This website has been further developed from ‘My First Milestone Project’.

The client specified the need for a responsive website that is clear, simple and easy to use, while reflecting her style as an artist. I had a look at her work and found that she works with clean lines, keeping her colour palette simple to just black and white. I have reflected this through the design of my website by keeping to a monochromatic colour scheme with simple features.


# UX
This website has quite a specific target audience. The target audience of this website are people who are interested in finding out more about Sania Nadeem as an artist, viewing her artworks and purchasing them.
This project helps to bring these things to the target audience by presenting the artist’s work through a simple and easy to use website that is responsive on different devices. The website is easy to navigate as well as looking aesthetic in line with the artist's theme. The website also showcases the artist’s work through a clear grid format on the ‘works’ page.


### User Stories

- As a user of this website, I want to be able to log in and have my own profile, where I can add a photo and a bio, and delete and edit these when necessary.
- As a user of this website, I want to be able to find out information about the artist, view their artwork and purchase it if I want to.
- As a user of this website, I want to be able to add my own comments on a piece of artwork, and see what other people have commented too.
- As a user of this website, I want to be able to get more information on a piece of artwork when I click on it, including title of the piece, the year it was made, the medium, and the price.
- As a user of this website, I want to be able to purchase the artwork from a safe and secure payment system.
- As a user of this website, I want to be able to view my shopping cart and all the items in my basket, as well as being able to add and remove things from here.
- As a user of this website, I want to be able to view the website on different devices, such as a mobile, tablet and/or desktop.

# Features
- Home page - this is the first page users will see when they open my website.
- Header - the header has the title of the website.
- Footer - the footer has links to the artist’s social media pages. (Facebook, Instagram and YouTube)
- Navigation bar - the navigation bar has links to all the pages in the site.
- Search bar - this allows users to search for content within the website.
- Login/logout - the login and logout features allow users to sign in and out to their own personal accounts within the website.
- Works page - this page allows users to view all the artwork created by the artist in one place through thumbnail images.
- Detailed image page - these pages allow users to view the artwork at a larger scale and see more information about it, such as the title, the year it was made, the medium and the price. 
- Comments - these can be added and deleted, and the user can also see others comments.
- Basket - this allows items to be held in a cart for easy checkout.
- Payment page - the payment page allows the user to make a safe and secure payment.
- Contact form - the contact form allows users to send any questions or queries in a message directly to the artist.
- About page - this page allows users to read up about the artist and what her work is about.
- Register page - the register page allows users to create an account within the website which will allow them to comment on and purchase artwork.
- Sign in page - this page allows users to sign in to an already existing account.
- Cart page - the cart page shows what items are in the basket, and the total price of all items. It is the final page where you can add or delete items before checkout.
- Checkout page - the checkout page allows you to make a payment for items in your basket.

### Features Left to be Implemented
If I was to go back and have more time on this project, I would like to add a few more features to my website to make it easier to use and more user friendly.

- Refund page - I would like to add a refund page where people can submit a request for a refund if they are unhappy with the items they have received.
- Sending a confirmation email to users when order has been placed - I would like to implement the feature of sending an email when an order has been placed, so that users have a confirmation of their purchase for their records.
- Sending a thank you email when registering - I would like to implement the feature of sending an email to users who have created an account with the website, thanking them for signing up and reminding them of their username details.
- Forgotten password link - I would like to implement a ‘forgotten password’ link which users can click to request a new password if they have forgotten the password to their account.

### Technologies used

###### Frontend:
- HTML
- CSS
 - Bootstrap

###### Backend:

- Django
- Python
- Git
- Github
- Heroku 
- PostgreSQL
-  Javascript

#Testing

Please see separate testing file.

### Code Validation:

- I used the W3C HTML validator tool to validate my HTML code.
- I used the W3C CSS validator tool to validate my CSS code. 
- I also manually removed some errors from my code, such as stranded tags.


#Deployement
This project is hosted on Heruko on https://freds-ecommerce.herokuapp.com/

### Local deployement:

1.) I created an env.py file in the my root directory and added all the following information on it:

os.environ.setdefault("SECRET_KEY",'Key details')

os.environ.setdefault("DATABASE_URL",'Key details')

os.environ.setdefault("STRIPE_PUBLISHABLE",'Key details')

os.environ.setdefault("STRIPE_SECRET",'Key details')

os.environ.setdefault("AWS_ACCESS_KEY_ID",'Key details')

os.environ.setdefault("AWS_SECRET_ACCESS_KEY",'Key details')

2.) I then added the following code to my settings file:

import dj_database_url
from os import path

if path.exists('env.py'):
    import env

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

3.) After I had finished adding the code above, I typed in the following:

python3 manage.py makemigrations

python manage.py migrate

### Heruko deployment:

1.) I created a requirements.txt and Procfile through the following code :

- pip freeze > requirements.txt
- echo web: python3 app.py > Procfile

2.) I then commited all my files on to Github through the following code:

- git add
- git commit -m "(description)"
- git push origin master

3.) I created a new app on the Heruko page and then clicked on "Deploy". This lead me to a page where I 
could click on "Deployment method" to select Github. This would link the Heruko app to the Github page.

4.) Once my app was linked with Github, I added all of my config vars.

5.) After all the steps above had been completed, I clicked on the "Deploy Branch" button in the "Deploy" page.


# Credits

###### Content:
All content on the website is written by me, except the artist statement. (Courtesy of the artist, Sania Nadeem)
All images are courtesy of artist, Sania Nadeem

###### Media:
All wireframes created by me, but supported by the artist, Sania Nadeem, to make sure that I fulfilled the client’s website needs.

###### Acknowledgements:

I have gained inspiration for this website from the following webpages;

- Amazon
- Argos
- The artists Instagram page - @san_does_art

I have also received help when making this website from;

- My mentor, Spencer Barriball, who helped me throughout the project
- Youtube tutorials on how to use Django