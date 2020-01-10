**Welcome to Genuine-Fake documentation!**
=========================================

**Definition**
An imitation of a (usually) valuable object that is so good that it is, to all intents and purposes, identical.Literaly genuine fake means something that is real but not real at the same time. Take it like this, it's more of a perfect replica of the original.


**Why**
As I was building a Django app that involved forms a lot, I got tired from filling the forms and having to think of the testing data at the same time. As curious as I am I wondered if there might be a package that can handle this for me, fortunately there was one, but I didn't like it, well not because it wasn't good, it was brilliant actually but it didn't have all the necessary and broad range of data I was looking for. Then I asked myself "What now?" The decision was to write my own. I did write it within 6 hours. I have changed it's name aboout 3 times now, hopefully this time it will stick.

**Inspiration**
Well, truthfully the inspiration came from me trying to challenge myself and be out there. I was so inspired to write the code for this to the point that I wrote half the code on paper as I was travelling from school to home on the train.

**How It Works**
**Installation**

1. **pip install genuine-fake**

**Importing the necessary module**

2. from genuine.fake import GenuineFake

**Assigning Deepfake to a variable named fake**

3. genuine = GenuineFake

**Calling the name function, name contains full names**

4. genuine.name()
**'Andile Mbele'**

**Calling the first_name function**

5. genuine.first_name()
**'Andile'**

**Calling the first_name function**

6. genuine.last_name()
**'Moyo'**

**Author Information**

7. genuine.__author__
**'Andile Jaden Mbele'**

8. genuine.__email__
**'andilembele020@gmail.com'**

9. genuine.__package__
**'chameleon'**

10. genuine.Author
**'Andile Jaden Mbele'**

**Other functions include**

- genuine.hospital()
- genuine.medical_aid()
- genuine.career()
- genuine.medical_professions()
- genuine.national_id()
- genuine.career_positions()
- genuine.company()
