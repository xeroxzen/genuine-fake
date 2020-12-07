#! python

"""
Created on Thu December 19 14:10:59 2019
Updated on Sunday September 27 04:33:59 2020

@author: Andile XeroxZen
"""

import datetime
import random
import string
from random import choice, randint

from . import data_list


# noinspection PyUnusedLocal
class GenuineFake:
    def __init__(self=None):
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

    @staticmethod
    def name():
        """
        >>> genuine = GenuineFake
        >>> genuine.name()
        'Doreen Dlamini'

        """
        name_data = choice(data_list.common_names) + ' ' + choice(data_list.common_surnames)
        name = name_data
        return name

    @staticmethod
    def first_name():
        """
        >>> from genuine.fake import GenuineFake
        >>> genuine = GenuineFake
        >>> genuine.first_name()
        'Mongezi'
        """
        first_name_data = data_list.common_names
        first_name = random.choice(first_name_data)
        return first_name

    @staticmethod
    def last_name():
        """
        >>> from genuine.fake import GenuineFake
        >>> genuine = GenuineFake
        >>> genuine.last_name()
        'Sikhosana'
        """
        last_name_data = data_list.common_surnames
        last_name = random.choice(last_name_data)
        return last_name

    @staticmethod
    def gender():
        possibilities = ["male", "female"]
        sex = random.choice(possibilities)
        return sex

    @staticmethod
    def random_date():
        pos_day = range(1, 31)
        pos_month = range(1, 13)
        pos_year = range(1960, 2020)

        return datetime.date(random.choice(pos_year), random.choice(pos_month), random.choice(pos_day)).strftime(
            "%Y-%m-%d")

    @staticmethod
    def date_of_birth():
        pos_day = range(1, 31)
        pos_month = range(1, 13)
        pos_year = range(1960, 2020)

        return datetime.date(random.choice(pos_year), random.choice(pos_month), random.choice(pos_day)).strftime(
            "%Y-%m-%d")

    @staticmethod
    def national_id():
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

        i: int
        issued_set1 = "".join(choice(set1) for i in range(randint(2, 2)))
        j: int
        issued_set2 = "".join(choice(set2) for j in range(randint(6, 7)))
        issued_set3 = "".join(choice(set3) for k in range(randint(1, 1)))
        x: int
        issued_set4 = "".join(choice(set4) for x in range(randint(2, 2)))

        issued_id = issued_set1 + '-' + issued_set2 + issued_set3 + issued_set4
        return issued_id

    @staticmethod
    def address():
        house_no = string.digits
        house_num = "".join(choice(house_no) for x in range(randint(1, 5)))
        place = data_list.places
        street_addr = data_list.streets
        address = house_num + ' ' + random.choice(street_addr) + ', ' + random.choice(place)
        chosen_address = address

        return chosen_address

    @staticmethod
    def phone_number():
        country_code = '+263'
        network_code = ['77', '73', '71']

        set1 = string.digits
        set2 = string.digits

        code1 = "".join(choice(set1) for i in range(randint(3, 3)))
        code2 = "".join(choice(set2) for j in range(randint(4, 4)))

        phone_number = country_code + ' ' + random.choice(network_code) + ' ' + code1 + ' ' + code2
        return phone_number

    @staticmethod
    def email():
        first_name = choice(data_list.common_names)
        last_name = choice(data_list.common_surnames)
        user_name = first_name.lower() + last_name.lower()
        mail_server = ('gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'hotmail.com', 'iCloud.com', 'yahoo.co.uk',
                       'protonmail.com')
        mail_address = user_name + '@' + random.choice(mail_server)
        # Want to include _, #s
        return mail_address

    @staticmethod
    def medical_aid():
        medical_aid_data = data_list.medical_aid
        medical_scheme = random.choice(medical_aid_data)
        return medical_scheme

    @staticmethod
    def allergies():
        allergies_data = data_list.allergens
        allergy = random.choice(allergies_data)
        return allergy

    @staticmethod
    def hospital(self):
        hospital_data = data_list.hospital
        hospital = random.choice(hospital_data)
        return hospital

    @staticmethod
    def career(self):
        career_data = data_list.career
        career = random.choice(career_data)
        return career

    @staticmethod
    def career_position(self):
        career_position_data = data_list.career_position
        career_position = random.choice(career_position_data)
        return career_position

    @staticmethod
    def company(self):
        company_data = data_list.company
        company = random.choice(company_data)
        return company

    @staticmethod
    def medical_professions(self):
        profession_data = data_list.medical_roles
        profession = random.choice(profession_data)
        return profession

    @staticmethod
    def date():
        current_date = datetime.date.today()
        # days_date = current_date
        return current_date.strftime("%Y-%m-%d")


if __name__ == '__main__':
    data = GenuineFake
