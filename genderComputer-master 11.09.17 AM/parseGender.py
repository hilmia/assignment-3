from genderComputer import GenderComputer
import os
import wikipedia
from bs4 import BeautifulSoup 
import openpyxl

#All Countries in the world into hashmap
all_countries = {
'Afghanistan' : True,
'Albania' : True,
'Algeria' : True,
'Andorra' : True,
'Angola' : True,
'Antigua' : True,
'Barbuda' : True,
'Argentina' : True,
'Armenia' : True,
'Australia' : True,
'Austria': True,
'Azerbaijan': True,
'Bahamas': True,
'Bahrain': True,
'Bangladesh': True,
'Barbados': True,
'Belarus': True,
'Belgium': True,
'Belize': True,
'Benin': True,
'Bhutan': True,
'Bolivia': True,
'Bosnia': True,
'Herzegovina': True,
'Botswana': True,
'Brazil': True,
'Brunei': True,
'Bulgaria': True,
'Burkina Faso': True,
'Burundi': True,
'Cabo Verde': True,
'Cambodia': True,
'Cameroon': True,
'Canada': True,
'Central African Republic': True,
'Chad': True,
'Chile': True,
'China': True,
'Colombia': True,
'Comoros': True,
'Congo': True,
'Costa Rica': True,
'Cote dIvoire': True,
'Croatia': True,
'Cuba': True,
'Cyprus': True,
'Czech Republic': True,
'Denmark': True,
'Djibouti': True,
'Dominica': True,
'Dominican Republic': True,
'Ecuador': True,
'Egypt': True,
'El Salvador': True,
'Equatorial Guinea': True,
'Eritrea': True,
'Estonia': True,
'Ethiopia': True,
'Fiji': True,
'Finland': True,
'France': True,
'Gabon': True,
'Gambia': True,
'Georgia': True,
'Germany': True,
'Ghana': True,
'Greece': True,
'Grenada': True,
'Guatemala': True,
'Guinea': True,
'Guinea-Bissau': True,
'Guyana': True,
'Haiti': True,
'Honduras': True,
'Hungary': True,
'Iceland': True,
'India': True,
'Indonesia': True,
'Iran': True,
'Iraq': True,
'Ireland': True,
'Israel': True,
'Italy': True,
'Jamaica': True,
'Japan': True,
'Jordan': True,
'Kazakhstan': True,
'Kenya': True,
'Kiribati': True,
'Kosovo': True,
'Kuwait': True,
'Kyrgyzstan': True,
'Laos': True,
'Latvia': True,
'Lebanon': True,
'Lesotho': True,
'Liberia': True,
'Libya': True,
'Liechtenstein': True,
'Lithuania': True,
'Luxembourg': True,
'Macedonia': True,
'Madagascar': True,
'Malawi': True,
'Malaysia': True,
'Maldives': True,
'Mali': True,
'Malta': True,
'Marshall Islands': True,
'Mauritania': True,
'Mauritius': True,
'Mexico': True,
'Micronesia': True,
'Moldova': True,
'Monaco': True,
'Mongolia': True,
'Montenegro': True,
'Morocco': True,
'Mozambique': True,
'Myanmar': True,
'Namibia': True,
'Nauru': True,
'Nepal': True,
'Netherlands': True,
'New Zealand': True,
'Nicaragua': True,
'Niger': True,
'Nigeria': True,
'North Korea': True,
'Norway': True,
'Oman': True,
'Pakistan': True,
'Palau': True,
'Palestine': True,
'Panama': True,
'Papua New Guinea': True,
'Paraguay': True,
'Peru': True,
'Philippines': True,
'Poland': True,
'Portugal': True,
'Qatar': True,
'Romania': True,
'Russia': True,
'Rwanda': True,
'St. Kitts': True,
'Nevis': True,
'St. Lucia': True,
'St. Vincent': True,
'The Grenadines': True,
'Samoa': True,
'San Marino': True,
'Sao Tome': True,
'Principe': True,
'Saudi Arabia': True,
'Senegal': True,
'Serbia': True,
'Seychelles': True,
'Sierra Leone': True,
'Singapore': True,
'Slovakia': True,
'Slovenia': True,
'Solomon Islands': True,
'Somalia': True,
'South Africa': True,
'South Korea': True,
'South Sudan': True,
'Spain': True,
'Sri Lanka': True,
'Sudan': True,
'Suriname': True,
'Swaziland': True,
'Sweden': True,
'Switzerland': True,
'Syria': True,
'Taiwan': True,
'Tajikistan': True,
'Tanzania': True,
'Thailand': True,
'Timor-Leste': True,
'Togo': True,
'Tonga': True,
'Trinidad': True,
'Tobago': True,
'Tunisia': True,
'Turkey': True,
'Turkmenistan': True,
'Tuvalu': True,
'Uganda': True,
'Ukraine': True,
'United Arab Emirates': True,
'United Kingdom': True,
'United States': True,
'Uruguay': True,
'Uzbekistan': True,
'Vanuatu': True,
'Vatican City': True,
'Venezuela': True,
'Vietnam': True,
'Yemen': True,
'Zambia': True,
'Zimbabwe': True };
#Input: place - String, must have first letter capitalized and rest not capitalized.
#Output: final - returns the country name as string
#This function will scrub wikipedia for the specific country name of a city.
def CityToCountry(place):
	try:
		city = wikipedia.page(place)
	except wikipedia.DisambiguationError:
		#This is if we catch an error - prob will just have to randomely generate 
		return "NOT FOUND"

	#Parse html for the rows on the side
	soup =BeautifulSoup(city.html(), "html.parser")
	data = soup.find_all("tr", {"class": ["mergedtoprow","mergedrow"]})
	country = []

	#check the rows for Country
	for dat in data:
		check_string = str(dat)
		if "Country" in check_string:
			country.append(dat)
	try:
		#I found that there was a pattern and if country appeared, then the sibling of it was always the
		#name of the country
		final = country[0].find_all("td")
		final = (final[0].text).encode("utf-8").strip()
	except IndexError:
		#If there is an error then lets not even worry bout it.  Too hard to calculate all the edge cases.
		return "ERROR PARSING"
	return final

def getCountry(check_place):
	#Parsing of the single entity
	splits = check_place.split(',')
	c_found = False;
	c_found_str = "";
	#Check for country in input
	for section in splits:
		white_space_removed = section.strip()
		if white_space_removed in all_countries:
			c_found = True
			c_found_str = white_space_removed

	#This is for an edge case like Saitama Japan (& Hangzhou, China).  pretty much just try to find the country name. 
	splits = check_place.split(" ")
	for section in splits:
		#Parse for white space
		white_space_removed = section.strip()
		if white_space_removed in all_countries:
			c_found = True
			c_found_str = white_space_removed
	#Output
	if check_place == "NULL" or check_place =="":
		return "NULL VALUE"
	elif c_found:
		return c_found_str
	else:
		#If no country is found check wikipedia
		return CityToCountry(check_place)


#Instantiation
gc = GenderComputer(os.path.abspath('./nameLists'))
#Open excel spreadsheet
wb = openpyxl.load_workbook('users_filtered.csv.xlsx')
sheet = wb.get_sheet_by_name('users_filtered.csv')
for cell in sheet.columns[4]:
	#Instantiate cell names
	row_num = cell.coordinate[1:]
	name_location = "C"+ row_num
	gender_location = "J"+row_num
	country_location = "K"+row_num
	if cell.coordinate != "E1":
		if cell.value:
			#check if name value is there if there is no name then we obviously can't infer gender
			if sheet[name_location].value:
				try:
					#Find Country
					country = getCountry(cell.value)
				except:
					country = "NULL"
				try:
					if sheet[name_location].value:
						#Infer gender only if there exists a name
						sheet[gender_location] = gc.resolveGender(sheet[name_location].value,country)
						sheet[country_location] = country
						print "Row "+row_num
				except:
					print "ERROR"
	#JUST IN CASE MY COMPUTER CRASHES - Saves every 50 rows.
	if int(row_num)%50 == 0:
		wb.save('filtered.xlsx')

			





#TO DO
#Add functionality for taking in input from csv
#Add more edge cases - there are alot. I think we just need just a general one, we can then just fill in the blanks.




