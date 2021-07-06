# Genuine-Fake documentation

### Definition

Genuine Fake means an imitation of a (usually) valuable object that is so good that it is, to all intents and purposes, identical. Literally genuine fake means something that is real but not real at the same time. Take it like this, it's more of a perfect replica of the original.

### Why

As I was building a Django app that involved forms a lot, I got tired from filling the forms and having to think of the testing data at the same time. As curious as I am I wondered if there might be a package that can handle this for me, fortunately there was one, but I didn't like it, well not because it wasn't good, it was brilliant actually but it didn't have all the necessary and broad range of data I was looking for. Then I asked myself "What now?" The decision was to write my own. I did write it within 6 hours. I have changed it's name about 3 times now, hopefully this time it will stick.

### Inspiration

Well, truthfully the inspiration came from me trying to challenge myself and be out there. I was so inspired to write the code for this to the point that I wrote half the code on paper as I was travelling from school to home on the train.

### How It Works

### ```Installation``` 

```sh
$ pip install genuine-fake
```

### Different Environments

#### ```MacOS and Linux Terminal```
```python
$ pip3 install Genuine-fake
$ python3
>>>
```

#### ```Windows Command Prompt```
```cmd
C:\Users\andil> pip install genuine-fake
C:\Users\andil> python
```
```py
>>> from genuine.fake import GenuineFake as gf
>>>
```

### ```In Action```

```python
>>> from genuine.fake import GenuineFake as gf
>>> gf.name()
'Mbonisi Ncube'
>>> gf.first_name()
'Phumzile'
>>> gf.last_name()
'Moyo'
>>> gf.hospital()
'Queen of Peace Clinic'
>>> gf.medical_aid()
'For All Medical Aid Society'
>>> gf.medical_professions()
'Orthotist'
>>> gf.national_id()
'08-906712V35'
>>> gf.phone_number()
'+263 77 647 5160'
>>> gf.email()
'ivynkala@outlook.com'
>>> gf.address()
'32 Casper Road, Sunninghill'
>>> gf.career()
'Physician'
>>> gf.company()
'Standard Chartered Bank'
>>> gf.career_position()
'Chauffeur'
>>> gf.date()
'2020-04-13'
>>> gf.random_date()
'1988-06-21'
>>> gf.date_of_birth()
'1995-05-19'
>>> gf.allergies()
'Fish'
>>> gf.house_account_number()
'34746237'
>>> gf.covid_symptom()
'fever'
>>> gf.payment_method()
'EcoCash'
>>> gf.covid_age_group()
'13 - 19'
```

### Other functions include

```python
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
