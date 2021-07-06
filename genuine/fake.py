#! python

"""
Created on Thu December 19 14:10:59 2019
Updated on Monday March 3 16:16:59 2020
@author: Andile XeroxZen
"""

import datetime
import random
import string
from random import choice, randint
# from genuine import data_list
from . import data_list


# noinspection PyUnusedLocal
class GenuineFake:
    def __init__(self=None):
        """Return the corresponding exact value

        """

    @staticmethod
    def name():
        """When this function is called, it should return a full person name. 

        >>> gf.name()
        'Nokuzola Mbele'
        """
        name_data = choice(data_list.common_names) + ' ' + \
            choice(data_list.common_surnames)
        name = name_data
        return name

    @staticmethod
    def first_name():
        """When this function is called, it should return a firstname. 

        >>> gf.first_name()
        'Miranda'
        """
        first_name_data = data_list.common_names
        first_name = random.choice(first_name_data)
        return first_name

    @staticmethod
    def last_name():
        """When this function is called, it should return a lastname/surname. 

        >>> gf.last_name()
        'Washington'
        """
        last_name_data = data_list.common_surnames
        last_name = random.choice(last_name_data)
        return last_name

    @staticmethod
    def gender():
        """When this function is called, it should return one of two gender possibilities. 

        >>> gf.gender()
        'female'
        """
        possibilities = ["male", "female"]
        sex = random.choice(possibilities)
        return sex

    @staticmethod
    def random_date():
        """Return a a randomly generated date. 

        >>> gf.random_date()
        '1968-04-29'
        """
        pos_day = range(1, 31)
        pos_month = range(1, 13)
        pos_year = range(1960, 2040)

        return datetime.date(random.choice(pos_year), random.choice(pos_month), random.choice(pos_day)).strftime(
            "%Y-%m-%d")

    @staticmethod
    def date_of_birth():
        """Return a a randomly generated date of birth. 

        >>> gf.date_of_birth()
        '2018-10-11'
        """
        pos_day = range(1, 31)
        pos_month = range(1, 13)
        pos_year = range(1900, 2021)

        return datetime.date(random.choice(pos_year), random.choice(pos_month), random.choice(pos_day)).strftime(
            "%Y-%m-%d")

    @staticmethod
    def national_id():
        """Return a valid Zimbabwean issued National ID

        >>> gf.national_id()
        '33-3432018L80'
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
        """ Return a valid home address

        >>> gf.address()
        '52908 Jason Moyo Ave, Harrisvale'
        """
        house_no = string.digits
        house_num = "".join(choice(house_no) for x in range(randint(1, 5)))
        place = data_list.places
        street_addr = data_list.streets
        address = house_num + ' ' + \
            random.choice(street_addr) + ', ' + random.choice(place)
        chosen_address = address

        return chosen_address

    @staticmethod
    def phone_number():
        """Return a valid Zimbabwean cell phone number for all the three operational mobile network.

        To achieve this use the many handy functions provided by the random module including randint and choice.


        >>> gf.phone_numbers()
        '+263 78 385 4016'
        """
        country_code = '+263'
        network_code = ['77', '78', '73', '71']

        set1 = string.digits
        set2 = string.digits

        code1 = "".join(choice(set1) for i in range(randint(3, 3)))
        code2 = "".join(choice(set2) for j in range(randint(4, 4)))

        phone_number = country_code + ' ' + \
            random.choice(network_code) + ' ' + code1 + ' ' + code2
        return phone_number

    @staticmethod
    def email():
        """Return a valid email address registered with the popular email clients you can think of. 

        This is possible by combining firstnames and lastnames and then running the choice function to randomly assign correspondence.

        >>> gf.email()
        'ngonidzashegweshe@yahoo.co.uk'
        """

        first_name = choice(data_list.common_names)
        last_name = choice(data_list.common_surnames)
        user_name = first_name.lower() + last_name.lower()
        mail_server = ('gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'hotmail.com', 'iCloud.com', 'yahoo.co.uk',
                       'protonmail.com')
        mail_address = user_name + '@' + random.choice(mail_server)

        return mail_address

    @staticmethod
    def medical_aid():
        """ Return a medical aid service provider

        >>> gf.medical_aid()
        'Pro Health Medical Aid Society'
        """
        medical_aid_data = data_list.medical_aid
        medical_scheme = random.choice(medical_aid_data)
        return medical_scheme

    @staticmethod
    def allergies():
        """ Return an allergy 

        >>> gf.allergies()
        'Tartrazine'
        >>> 
        """
        allergies_data = data_list.allergens
        allergy = random.choice(allergies_data)
        return allergy

    @staticmethod
    def hospital():
        """ Return a hospital name

        >>> gf.hospital()
        'Beitbridge District Hospital'
        >>>
        """
        hospital_data = data_list.hospital
        hospital = random.choice(hospital_data)
        return hospital

    @staticmethod
    def career():
        """ Return a career type

        >>> gf.career()
        'Nurse'
        >>>
        """
        career_data = data_list.career
        career = random.choice(career_data)
        return career

    @staticmethod
    def career_position():
        """Return a career position

        >>> gf.career_position()
        'Programs Manager'
        >>>
        """
        career_position_data = data_list.career_position
        career_position = random.choice(career_position_data)
        return career_position

    @staticmethod
    def company():
        """ Return a valid company name
        >>> gf.company()
        'CBZ Holdings'
        >>>
        """
        company_data = data_list.company
        company = random.choice(company_data)
        return company

    @staticmethod
    def medical_professions():
        """ Return a position in the medical profession

        >>> gf.medical_professions()
        'Pediatrician'
        >>>
        """

        profession_data = data_list.medical_roles
        profession = random.choice(profession_data)
        return profession

    @staticmethod
    def date():
        """Return the current date 

        >>> gf.date()
        '2021-07-06'
        >>>
        """
        current_date = datetime.date.today()
        # days_date = current_date
        return current_date.strftime("%Y-%m-%d")

    @staticmethod
    def house_account_number():
        """ Returns a valid house billing account number

        >>> gf.house_account_number()
        '37532600'
        >>>
        """
        rand_num = str(randint(30000000, 39999999))
        return rand_num

    @staticmethod
    def covid_symptoms():
        """ Return a COVID-19 symptom

        >>> gf.covid_symptom()
        'tiredness'     
        >>>
        """

        symptoms_data = data_list.coronavirus_symptoms
        symptom = random.choice(symptoms_data)
        return symptom

    @staticmethod
    def payment_method():
        """ Return a universally acceptable payment method 

        >>> gf.payment_method()
        'VISA'
        >>>
        """
        payment_methods_data = data_list.payment_methods
        payment_method = random.choice(payment_methods_data)
        return payment_method

    @staticmethod
    def covid_age_group():
        """ Return an age group used to categorize COVID-19 infections 

        >>> gf.covid_age_group()
        '55 - 64'
        >>>
        """
        ages_data = data_list.covid_age_range
        age_group = random.choice(ages_data)
        return age_group


if __name__ == '__main__':
    data = GenuineFake
