# -*- coding: utf-8 -*-
"""
Created on Thu December  19 14:10:59 2019

@author: Andile XeroxZen
"""

import datetime
import random
import string
from random import choice, randint

from . import data_list


class GenuineFake:
    def __init__(self):
        """
        >>> from genuine.fake import GenuineFake
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

    def name(self):
        """
        >>> genuine = GenuineFake
        >>> genuine.name()
        'Doreen Dlamini'

        """
        name = choice(data_list.common_names) + ' ' + choice(data_list.common_surnames)
        choice_name = name
        return choice_name

    def first_name(self):
        """
        >>> from genuine.fake import GenuineFake
        >>> genuine = GenuineFake
        >>> genuine.first_name()
        'Mongezi'
        """
        choice_name = data_list.common_names
        pick = random.choice(choice_name)
        return pick

    def last_name(self):
        """
        >>> from genuine.fake import GenuineFake
        >>> genuine = GenuineFake
        >>> genuine.last_name()
        'Sikhosana'
        """
        chosen_name = data_list.common_surnames
        pick = random.choice(chosen_name)
        return pick

    def gender(self):
        possibilities = ["male", "female"]
        sex = random.choice(possibilities)
        return sex

    def date(self):
        current_date = datetime.date.today()
        # days_date = current_date
        return current_date.strftime("%Y-%m-%d")

    def random_date(self):
        pos_day = range(1, 31)
        pos_month = range(1, 13)
        pos_year = range(1960, 2020)

        return datetime.date(random.choice(pos_year), random.choice(pos_month), random.choice(pos_day)).strftime(
            "%Y-%m-%d")

    def date_of_birth(self):
        pos_day = range(1, 31)
        pos_month = range(1, 13)
        pos_year = range(1960, 2020)

        return datetime.date(random.choice(pos_year), random.choice(pos_month), random.choice(pos_day)).strftime(
            "%Y-%m-%d")

    def national_id(self):
        """
        >>> from genuine.fake import GenuineFake
        >>> fake = GenuineFake
        >>> fake.national_id()
        '15-516077P91'
        """
        set1 = string.digits
        set2 = string.digits
        set3 = string.ascii_uppercase
        set4 = string.digits

        issued_set1 = "".join(choice(set1) for i in range(randint(2, 2)))
        issued_set2 = "".join(choice(set2) for j in range(randint(6, 7)))
        issued_set3 = "".join(choice(set3) for k in range(randint(1, 1)))
        x: int
        issued_set4 = "".join(choice(set4) for x in range(randint(2, 2)))

        issued_id = issued_set1 + '-' + issued_set2 + issued_set3 + issued_set4
        return issued_id

    def address(self):
        house_no = string.digits
        house_num = "".join(choice(house_no) for x in range(randint(1, 5)))
        place = data_list.places
        street_addr = data_list.streets
        address = house_num + ' ' + random.choice(street_addr) + ', ' + random.choice(place)
        chosen_address = address

        return chosen_address

    def phone_number(self):
        country_code = '+263'
        network_code = ['77', '73', '71']

        set1 = string.digits
        set2 = string.digits

        code1 = "".join(choice(set1) for i in range(randint(3, 3)))
        code2 = "".join(choice(set2) for j in range(randint(4, 4)))

        phone_number = country_code + ' ' + random.choice(network_code) + ' ' + code1 + ' ' + code2
        return phone_number

    def email(self):
        first_name = choice(data_list.common_names)
        last_name = choice(data_list.common_surnames)
        user_name = first_name.lower() + last_name.lower()
        mail_server = ('gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'hotmail.com', 'iCloud.com', 'yahoo.co.uk',
                       'protonmail.com')
        mail_address = user_name + '@' + random.choice(mail_server)
        # Want to include _, #s
        return mail_address

    def medical_aid(self):
        medical_aid_data = data_list.medical_aid
        medical_scheme = random.choice(medical_aid_data)
        return medical_scheme

    def allergies(self):
        allergies_data = data_list.allergens
        allergy = random.choice(allergies_data)
        return allergy

    def hospital(self):
        hospital_data = data_list.hospital
        hospital = random.choice(hospital_data)
        return hospital

    def career(self):
        career_data = data_list.career
        career = random.choice(career_data)
        return career

    def career_position(self):
        career_position_data = data_list.career_position
        career_position = random.choice(career_position_data)
        return career_position

    def company(self):
        company_data = data_list.company
        company = random.choice(company_data)
        return company

    def medical_professions(self):
        profession_data = data_list.medical_roles
        profession = random.choice(profession_data)
        return profession


if __name__ == '__main__':
    data = GenuineFake
