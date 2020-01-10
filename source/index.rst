.. Chameleon documentation master file, created by
   sphinx-quickstart on Fri Dec 20 11:47:23 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


**Welcome to Chameleon's documentation!** 
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**Definition***
===================
Chameleon is a type of lizard. There are around 160 species of chameleons which can be found mostly on the Madagascar (half of all species live there), in the Africa, southern Europe, south Asia and Sri Lanka. Chameleons do not have ear opening or outer ears, but they are not deaf. They can detect sounds in the frequency range from 200 to 600 Hz. The best known characteristic of chameleons is their ability to change the color of the skin. Most people believe that chameleons change their color to blend in with environment.


**Why**
=========
I named this package CHAMELEON because like a chameleon it is constantly changing and is highly in terms of the data output it generates. The data it generates is legit, 100% authentic and usable. At first I had called the package FONGKONG then 24hrs after coming with the idea and having deployed it to PYPI I wanted to change its name and I did. 

This package is best for developers who are in need of testing data. Instead of having to think of names of stuff you need to use for your app, you could have this package do everything for you.

**Inspiration**
============
The inspiration for writing this package came as I was building my own Django web app that dealt with a lot of forms, I found it tiresome having to think of the data to input, I looked around for solutions then bumped onto #faker. I must admit faker is a good package but it's not conclusive as the data it has is mostly American and cannot be applied in an African context. I then started writing the code for FongKong which later changed to Chameleon on paper on my way home in the train, by the time I got home, I had a rough idea then I started implementing the code and now I'm ready to deploy.   

**How It Works**
**Installation**

>>> pip install chameleon

**Importing the necessary module**
>>> from chameleon.chameleon import DeepFake

**Assigning FongKong to a variable named fake**
>>> fake = DeepFake

**Calling the name function, name contains full names**

>>> fake.name()
	'Andile Mbele'

**Calling the first_name function**

>>> fake.first_name()
	'Andile'

**Calling the first_name function**
>>> fake.last_name()
	'Moyo'

**Author Information**
>>> chameleon.__author__
	'Andile Jaden Mbele'
>>> chameleon.__email__
	'andilembele020@gmail.com'
>>> chameleon.__package__
	'chameleon'
>>> chameleon.Author
	'Andile Jaden Mbele'

**Other functions include**

- fake.hospital()
- fake.medical_aid()
- fake.career()
- fake.medical_professions()
- fake.national_id()
- fake.career_positions()
- fake.company()

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`





