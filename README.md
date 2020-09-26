# Genuine-Fake documentation

### Definition
Genuine Fake means an imitation of a (usually) valuable object that is so good that it is, to all intents and purposes, identical. Literally genuine fake means something that is real but not real at the same time. Take it like this, it's more of a perfect replica of the original.

### Why
As I was building a Django app that involved forms a lot, I got tired from filling the forms and having to think of the testing data at the same time. As curious as I am I wondered if there might be a package that can handle this for me, fortunately there was one, but I didn't like it, well not because it wasn't good, it was brilliant actually but it didn't have all the necessary and broad range of data I was looking for. Then I asked myself "What now?" The decision was to write my own. I did write it within 6 hours. I have changed it's name about 3 times now, hopefully this time it will stick.

### Inspiration
Well, truthfully the inspiration came from me trying to challenge myself and be out there. I was so inspired to write the code for this to the point that I wrote half the code on paper as I was travelling from school to home on the train.

### How It Works
### Installation

```sh
$ pip install genuine-fake
```
### Different Environments
```sh
Terminal
$ pip3 install genuine-fake
$ python3
>>> 
```

```sh
Windows Command Prompt
C:\Users\Andile XeroxZen> pip install genuine-fake
C:\Users\Andile XeroxZen> python
>>>
```
### Usage
```sh
>>> from genuine.fake import GenuineFake
>>> data = GenuineFake
>>> data.name()        
'Mbonisi Ncube'
>>> data.first_name()
'Phumzile'
>>> data.last_name()
'Moyo'
>>> data.hospital()
'Queen of Peace Clinic'
>>> data.medical_aid()
'For All Medical Aid Society'
>>> data.medical_professions()
'Orthotist'
>>> data.national_id()
'08-906712V35'
>>> data.phone_number()
'+263 77 647 5160'
>>> data.email()
'ivynkala@outlook.com'
>>> data.address()
'32 Casper Road, Sunninghill'
>>> data.career()
'Physician'
>>> data.company()
'Standard Charteresd Bank'
>>> data.career_position()
'Chauffeur'
>>> data.date()
'2020-04-13'
>>> data.random_date()
'1988-06-21'
>>> data.date_of_birth()
'1995-05-19'
>>> data.allergies()
'Fish'
```

### Other functions include
```sh
>>> import genuine
>>> genuine.__author__
'Andile Jaden Mbele'
>>> genuine.__email__
'andilembele020@gmail.com'
>>> genuine.__package__
'genuine-fake'
>>> genuine.__github__  
'https://github.com/xeroxzen/genuine-fake'
>>>
```

