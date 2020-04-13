# Welcome to Genuine-Fake documentation

## Definition
Genuine Fake means an imitation of a (usually) valuable object that is so good that it is, to all intents and purposes, identical. Literaly genuine fake means something that is real but not real at the same time. Take it like this, it's more of a perfect replica of the original.

## Why
As I was building a Django app that involved forms a lot, I got tired from filling the forms and having to think of the testing data at the same time. As curious as I am I wondered if there might be a package that can handle this for me, fortunately there was one, but I didn't like it, well not because it wasn't good, it was brilliant actually but it didn't have all the necessary and broad range of data I was looking for. Then I asked myself "What now?" The decision was to write my own. I did write it within 6 hours. I have changed it's name about 3 times now, hopefully this time it will stick.

## Inspiration
Well, truthfully the inspiration came from me trying to challenge myself and be out there. I was so inspired to write the code for this to the point that I wrote half the code on paper as I was travelling from school to home on the train.

## How It Works
### Installation and Use

```sh
$ pip install genuine-fake
$ python
>>> #Importing the necessary module
>>> from genuine.fake import GenuineFake
>>> #Assigning GenuineFake to a variable
>>> data = GenuineFake
>>> dir(data)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'address', 'allergies', 'career', 'career_position', 'company', 'date', 'date_of_birth', 'email', 'first_name', 'gender', 'hospital', 'last_name', 'medical_aid', 'medical_professions', 'name', 'national_id', 'phone_number', 'random_date']
>>>
>>> #Calling the name function, name contains full names
>>> data.name()        
'Mbonisi Ncube'
>>> 
>>> #Calling the first_name function
>>> data.first_name()
'Phumzile'
>>> data.first_name()
'Peter'
>>> data.first_name()
'Janet'
>>> data.first_name()
'Anele'
>>> data.first_name()
'Janice'
>>> #Calling the first_name function
>>> data.last_name()
'Moyo'
>>> data.last_name()
'Nyathi'
>>> data.last_name()
'Dywili'
>>> data.hospital()
'Clay Bank Group of Hospitals'
>>> data.hospital()
'Esigodini District Hospital'
>>> data.hospital()
'West End Clinic'
>>> data.hospital()
'Queen of Peace Clinic'
>>> data.medical_aid()
'Corporate 24 Medical Aid'
>>> data.medical_aid()
'Emf Medical Aid Society'
>>> data.medical_aid()
'For All Medical Aid Society'
>>> data.medical_professions()
'Chiropractor'
>>> data.medical_professions()
'Pediatric Nurse'
>>> data.medical_professions()
'Orthotist'
>>>
>>> data.national_id()
'08-906712V35'
>>> data.national_id()
'41-6462288G84'
>>> data.national_id()
'20-6350086I46'
>>>
>>> data.phone_number()
'+263 73 614 4973'
>>> data.national_id()
'20-6350086I46'
>>> data.phone_number()
'+263 77 585 1594'
>>> data.phone_number()
'+263 77 647 5160'
>>>
>>> data.email()
'ivynkala@outlook.com'
>>> data.email()
'shaniqiphiri@yahoo.com'
>>> data.email()
'pennympofu@gmail.com'
>>> data.email()
'charmainemoyo@wordpress.com'
>>>
>>> data.address()
'32 Casper Road, Sunninghill'
>>> data.address()
'750 Casper Road, Malindela'
>>> data.address()
'2760 Game Free Road, Nkulumane'
>>>
>>> data.career()
'Statistician'
>>> data.career()
'Physiotherapist'
>>> data.career()
'Physician'
>>>
>>> data.company()
'Standard Charteresd Bank'
>>> data.company()
'Telecel ZW'
>>> data.company()
'OK Zimbabwe'
>>> data.company()
'MBCA'
>>>
>>> data.career_position()
'Chauffeur'
>>> data.career_position()
'Chief Executive Officer'
>>> data.career_position()
'Vice President of Product Development'
>>> data.career_position()
'Vice President of Engineering'
>>> 
>>> data.date()
'2020-04-13'
>>> data.random_date()
'1988-06-21'
>>> data.random_date()
'2000-11-26'
>>> data.random_date()
'1980-05-11'
>>> data.random_date()
'1987-09-13'
>>> data.random_date()
'1971-01-03'
>>>
>>> data.date_of_birth()
'2004-09-22'
>>> data.date_of_birth()
'2000-09-25'
>>> data.date_of_birth()
'1961-03-29'
>>> data.date_of_birth()
'1966-12-15'
>>> data.date_of_birth()
'1995-05-19'
>>>
>>> data.allergies()
'Fish'
>>> 
data.gender()
'female'
```


### Other functions include

```sh
>>> import genuine   
>>> dir(genuine) 
['__author__', '__builtins__', '__cached__', '__doc__', '__email__', '__file__', '__github__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
>>> genuine.__author__
'Andile Jaden Mbele'
>>> genuine.__package__
'genuine-fake'
>>>
>>> genuine.__github__  
'https://github.com/xeroxzen/genuine-fake'
>>>
```

