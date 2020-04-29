# Sanias Art Gallery
The main purpose of this project was to allow users to be able to view and purchase the artists work. Features such as being able
to read and make comment on each piece of work would help users in doing so. This is because the comments of other users makes the decision
about wether or not to purchase the work easier. Having a comments section also gives the ability to communicate with different people. One of
the other features that this website provides, is that each user will get a profile account automatically and will be able to edit this.
Through this feature, Users will be able to view each others profiles to know more about them.
The artist's work is monochromatic in its style, and I have reflected this through the design of my website.

# UX
The Target audience of this website is people who like art and want to 

#Deployement
This project is hosted on Heruko. 

### Local deployement

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

### Heruko deployment

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








