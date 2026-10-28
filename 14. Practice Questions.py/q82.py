#Q82
#Create a dict mapping five countries to thier capital cities. Iterate through this dictionary using the items() method and print each pair in the format: Country --> Capital.

countries = {
    "India": "New Delhi",
    "Usa": "Washington DC",
    "Japan": "Tokyo",
    "France": "Paris",
    "Canada": "Ottawa",
}
#country = "India"
#capital = countries.get(country)
for countries, capital in countries.items():
    print(countries, capital)