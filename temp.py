import pycountry

def generate_country_options():
    countries = list(pycountry.countries)
    countries.sort(key=lambda x: x.name)
    for i, country in enumerate(countries, start=1):
        print(f'<option value="{i}">{country.name}</option>')

generate_country_options()
