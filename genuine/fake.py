#! python

"""
Created on Thu December 19 14:10:59 2019
Updated on Tuesday July 6 06:58:59 2021
@author: Andile Jaden Mbele
"""

import datetime
import random
import string
from random import choice, randint
from . import data_list
from pycountrycode.countrycode import get_country, get_code


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
        """Return a randomly generated date of birth.

        >>> Generator.date_of_birth()
        '3 Dec 2000'
        """
        days = random.randrange(1, 31)
        months = random.randrange(1, 13)
        years = random.randrange(1900, 2022)

        dob = datetime.date(years, months, days).strftime("%-d %b %Y")
        return dob

    @staticmethod
    def national_id():
        """Return a valid Zimbabwean issued National ID

        >>> Generator.national_id()
        '33-3432018L80'
        """
        digits1 = ''.join(choice(string.digits) for _ in range(2))
        digits2 = ''.join(choice(string.digits) for _ in range(randint(6, 7)))
        uppercase_letter = choice(string.ascii_uppercase)
        digits3 = ''.join(choice(string.digits) for _ in range(2))

        issued_id = f"{digits1}-{digits2}{uppercase_letter}{digits3}"
        return issued_id

    @staticmethod
    def address():
        """Return a valid home address

        >>> Generator.address()
        '52908 Jason Moyo Ave, Harrisvale'
        """
        house_num = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 5)))
        place = data_list.places if hasattr(data_list, 'places') and data_list.places else []
        street_addr = data_list.streets if hasattr(data_list, 'streets') and data_list.streets else []
        
        address = f"{house_num} {random.choice(street_addr)}, {random.choice(place)}"
        return address

    @staticmethod
    def phone_number():
        """Return a valid Zimbabwean cell phone number for all three operational mobile networks.

        To achieve this, use the handy functions provided by the random module, including randint and choice.

        >>> Generator.phone_number()
        '+263 78 385 4016'
        """
        country_code = '+263'

        set1 = string.digits
        set2 = string.digits

        code1 = ''.join(random.choices(set1, k=random.randint(3, 3)))
        code2 = ''.join(random.choices(set2, k=random.randint(4, 4)))

        prioritized_network_codes = ['77', '78', '71', '73', '73', '73']
        chosen_network_code = random.choice(prioritized_network_codes)

        formatted_number = f"{country_code} {chosen_network_code} {code1} {code2}"
        return formatted_number



    @staticmethod
    def international_number():
        """
        Returns a valid international mobile number for selected countries.

        >>> gf.international_number()
        '+61 401 983 162'
        >>> gf.international_number()
        '+27 87 172 9803'
        """
        country_codes = [
            get_code('South Africa'),
            get_code('United States'),
            get_code('Canada'),
            get_code('Australia'),
            get_code('United Kingdom'),
            get_code('New Zealand'),
            get_code('Ireland'),
            get_code('India'),
            get_code('China'),
            get_code('Japan'),
            get_code('Brazil'),
            get_code('Russia'),
            get_code('France'),
            get_code('Germany'),
            get_code('Italy'),
            get_code('Spain'),
            get_code('Mexico'),
            get_code('Indonesia'),
            get_code('Turkey'),
            get_code('Netherlands'),
            get_code('Saudi Arabia'),
            get_code('Switzerland'),
            get_code('Argentina'),
            get_code('Sweden'),
            get_code('Poland'),
            get_code('Belgium'),
            get_code('Norway'),
            get_code('Austria'),
            get_code('United Arab Emirates')
        ]

        phone_numbers = {
            'South Africa': {
                'network_code': ['61', '87']
            },
            'Australia': {
                'network_code': ['401', '413', '453']
            },
            'United States': {
                'network_code': ['201', '202', '203', '204', '205', '206', '207', '208', '209', '210']
            },
            'Canada': {
                'network_code': ['401', '413', '453']
            },
            'United Kingdom': {
                'network_code': ['401', '413', '453']
            },
            'New Zealand': {
                'network_code': ['401', '413', '453']
            },
            'Ireland': {
                'network_code': ['401', '413', '453']
            },
            'India': {
                'network_code': ['401', '413', '453']
            },
            'China': {
                'network_code': ['401', '413', '453']
            },
            'Japan': {
                'network_code': ['401', '413', '453']
            },
            'Brazil': {
                'network_code': ['401', '413', '453']
            },
            'Russia': {
                'network_code': ['401', '413', '453']
            },
            'France': {
                'network_code': ['401', '413', '453']
            },
            'Germany': {
                'network_code': ['401', '413', '453']
            },
            'Italy': {
                'network_code': ['401', '413', '453']
            },
            'Spain': {
                'network_code': ['401', '413', '453']
            },
            'Mexico': {
                'network_code': ['401', '413', '453']
            },
            'Indonesia': {
                'network_code': ['401', '413', '453']
            },
            'Turkey': {
                'network_code': ['401', '413', '453']
            },
            'Netherlands': {
                'network_code': ['401', '413', '453']
            },
            'Saudi Arabia': {
                'network_code': ['401', '413', '453']
            },
            'Switzerland': {
                'network_code': ['401', '413', '453']
            },
            'Argentina': {
                'network_code': ['401', '413', '453']
            },
            'Sweden': {
                'network_code': ['401', '413', '453']
            },
            'Poland': {
                'network_code': ['401', '413', '453']
            },
            'Belgium': {
                'network_code': ['401', '413', '453']
            },
            'Norway': {
                'network_code': ['401', '413', '453']
            },
            'Austria': {
                'network_code': ['401', '413', '453']
            },
            'United Arab Emirates': {
                'network_code': ['401', '413', '453']
            }

        }

        selected_country = None
        for country_code in country_codes:
            if country_code:
                selected_country = get_country(country_code)
                break

        if selected_country in phone_numbers:
            country_data = phone_numbers[selected_country]
            network_code = country_data['network_code']
            num1 = string.digits
            num2 = string.digits

            first_3_digits = "".join(random.choice(num1) for _ in range(random.randint(3, 3)))
            last_4_digits = "".join(random.choice(num2) for _ in range(random.randint(4, 4)))

            phone = country_code + ' ' + random.choice(network_code) + ' ' + first_3_digits + ' ' + last_4_digits # type: ignore
            return phone

        return 'Undefined country'



    @staticmethod
    def email():
        """Return a valid email address registered with popular email clients.

        This is achieved by combining first names and last names and then randomly assigning correspondence.

        >>> Generator.email()
        'ngonidzashegweshe@gmail.com'
        """
        first_name = random.choice(data_list.common_names)
        last_name = random.choice(data_list.common_surnames)
        username = first_name.lower() + last_name.lower()

        prioritized_providers = ['gmail.com', 'outlook.com', 'gmail.com', 'outlook.com']
        other_providers = ['aol.com', 'yahoo.com', 'hotmail.com', 'iCloud.com', 'yahoo.co.uk', 'protonmail.com']
        mail_server = prioritized_providers + other_providers

        email_address = username + '@' + random.choice(mail_server)
        return email_address

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
    
    @staticmethod
    def covid_vaccine():
        """ Return a COVID-19 vaccine type

        >>> gf.covid_vaccine()
        'AstraZeneca'
        >>>
        """
        vaccines_data = data_list.covid_vaccines
        vaccine = random.choice(vaccines_data)
        return vaccine
    
    @staticmethod
    def currency():
        """ Return a currency

        >>> gf.currency()
        'USD'
        >>>
        """
        currency_data = data_list.currency
        currency = random.choice(currency_data)
        return currency
    
    @staticmethod
    def colour():
        """ Return a colour

        >>> gf.colour()
        'blue'
        >>>
        """
        colour_data = data_list.colours
        colour = random.choice(colour_data)
        return colour
    
    @staticmethod
    def car_brand():
        """Return a car maker
        
        >>> gf.car_brand()
        'Tesla'
        """
        car_brand_data = data_list.car_brands
        car_brand = random.choice(car_brand_data)
        return car_brand
    
    @staticmethod
    def billionaire():
        """Return a billionaire's name
        
        >>> gf.billionaire()
        'Jeff Bezos'
        """
        billionaire_data = data_list.billionaires
        billionaire = random.choice(billionaire_data)
        return billionaire
    
    @staticmethod
    def country():
        """Return a country name
        
        >>> gf.country()
        'Zimbabwe'
        """
        country_data = data_list.countries
        country = random.choice(country_data)
        return country
    
    @staticmethod
    def capital_city():
        """Return a city name
        
        >>> gf.capital_city()
        'Harare'
        """
        city_data = data_list.capital_cities
        capacity_city = random.choice(city_data)
        return capacity_city
    
    @staticmethod
    def url():
        """Return a URL
        
        >>> gf.url()
        'https://www.google.com'
        """
        url_data = data_list.url
        url = random.choice(url_data)
        return url
    
    @staticmethod
    def smartphone_brand():
        """Return a smartphone brand
        
        >>> gf.smartphone_brand()
        'Apple'
        """
        smartphone_data = data_list.smartphone_makers
        smartphone = random.choice(smartphone_data)
        return smartphone
    
    @staticmethod
    def programming_language():
        """Return a programming language
        
        >>> gf.programming_language()
        'Python'
        """
        programming_data = data_list.programming_languages
        programming_language = random.choice(programming_data)
        return programming_language


if __name__ == '__main__':
    data = GenuineFake
