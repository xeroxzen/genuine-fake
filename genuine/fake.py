# -*- coding: utf-8 -*-
"""
Created on Thu December  19 14:10:59 2019

@author: Andile XeroxZen
"""

from . import data_list
from random import choice, randint
import random, string, datetime

class GenuineFake(object):
    def __init__(self):

        """
        >>> GenuineFake.national_id()
        '08-2127709X35'
        >>> GenuineFake.name()
        'Andile Mbele'
        >>> GenuineFake.first_name()
        'Michael'
        >>> GenuineFake.phone_number()
        '+263 73 149 4401'
        >>> GenuineFake.name()
        'Mercy Mandela'
        >>> GenuineFake.name()
        'Chad Makonese'

        # Assigning GenuineFake to variable named fake
        >>> genuine = GenuineFake
        >>> genuine.medical_professions()
        'Medical Surgery Nurse'
        >>> genuine.medical_professions()
        'Podiatrist'
        >>> genuine.medical_professions()
        'Chiropractor'

        >>> genuine.career()
        'Bank Teller'
        >>> genuine.career()
        'Pharmacist'
        >>> genuine.career()
        'Statistician'
        >>> genuine.career()
        'Physician'

        """

        return self

    def name():
        """
        >>> genuine = GenuineFake
        >>> genuine.name()
        'Doreen Dlamini'

        """
        name = choice(data_list.common_names) + ' ' + choice(data_list.common_surnames)
        choice_name = name
        return choice_name

        def __repr__(self):
            return choice_name

    def first_name():
        """
        >>> genuine.first_name()
        'Mongezi'
        """
        choice_name = data_list.common_names
        pick = random.choice(choice_name)
        return pick

        def __repr__(self):
            return pick

    def last_name():
        """
        >>> genuine.last_name()
        'Sikhosana'
        """
        chosen_name = data_list.common_surnames
        pick = random.choice(chosen_name)
        return pick

        def __repr__(self):
            return pick

    def date():
        currentDate = datetime.date.today()
        # days_date = currentDate
        return currentDate.strftime("%Y-%m-%d")

    def random_date():
         day = range(1, 32)
         month = range(1, 13)
         year = range(1900, 2020)
         actual_day = random.choice(day)
         actual_month = random.choice(month)
         actual_year = random.choice(year)
         date = str(actual_year) + '-' + str(actual_month) + '-' + str(actual_day)
         return date

    def date_of_birth():
         day = range(1, 32)
         month = range(1, 13)
         year = range(1900, 2020)
         actual_day = random.choice(day)
         actual_month = random.choice(month)
         actual_year = random.choice(year)
         birthday = str(actual_year) + '-' + str(actual_month) + '-' + str(actual_day)
         return birthday

    def national_id():
        """
        >>> fake.national_id()
        '15-516077P91'
        """
        set1 = string.digits
        set2 = string.digits
        set3 = string.ascii_uppercase
        set4 = string.digits

        issued_set1 = "".join(choice(set1) for x in range(randint(2,2)))
        issued_set2 = "".join(choice(set2) for x in range(randint(6,7)))
        issued_set3 = "".join(choice(set3) for x in range(randint(1,1)))
        issued_set4 = "".join(choice(set4) for x in range(randint(2,2)))

        issued_id = issued_set1 + '-' + issued_set2 + issued_set3 + issued_set4
        return issued_id

        def __repr__(self):
            return str(self.issued_id)

    def address():
        house_no = string.digits
        house_num = "".join(choice(house_no) for x in range(randint(1, 5)))
        place = data_list.places
        street_addr = data_list.streets
        address = house_num + ' ' + random.choice(street_addr) + ', ' + random.choice(place)
        chosen_address = address

        return chosen_address

        def __repr__(self):
            return str(self.chosen_address)

    def phone_number():
        country_code = ('+263')
        network_code = ('77', '73', '71')

        set1 = string.digits
        set2 = string.digits

        code1 = "".join(choice(set1) for x in range(randint(3,3)))
        code2 = "".join(choice(set2) for x in range(randint(4,4)))

        phone_num = country_code + ' ' + random.choice(network_code) + ' ' + code1 + ' ' + code2
        return phone_num

        def __repr__(self):
            return str(self.phone_num)

    def email():
        first_name = choice(data_list.common_names)
        last_name = choice(data_list.common_surnames)
        user_name = first_name.lower() + last_name.lower()
        mail_server = ('gmail.com', 'yahoo.com','aol.com', 'outlook.com', 'hotmail.com', 'iCloud.com', 'yahoo.co.uk', 'protonmail.com')
        mail_address = user_name + '@' + random.choice(mail_server)
        # Want to include _, #s
        return mail_address

        def __repr__(self):
            return str(self.mail_address)

    def medical_aid():
        data = data_list.medical_aid
        medical_scheme = random.choice(data)
        return medical_scheme

        def __repr__(self):
            return str(self.medical_scheme)

    def allergies():
        data = data_list.allergens
        allergy = random.choice(data)
        return allergy

        def __repr__(self):
            return str(self.allergy)

    def hospital():
        data = data_list.hospital
        choice = random.choice(data)
        return choice

        def __repr__(self):
            return str(self.choice)

    def career():
        data = data_list.career
        choice = random.choice(data)
        return choice

        def __repr__(self):
            return str(self.choice)

    def career_position():
        data = data_list.career_position
        choice = random.choice(data)
        return choice

        def __repr__(self):
            return str(self.choice)

    def company():
        data = data_list.company
        choice = random.choice(data)
        return choice

        def __repr__(self):
            return str(self.choice)

    def medical_professions():
        data = data_list.medical_roles
        choice = random.choice(data)
        return choice

        def __repr__(self):
            return str(self.choice)


if __name__ == '__main__':
   data = GenuineFake
