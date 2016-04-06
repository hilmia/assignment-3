import os
import wikipedia
from bs4 import BeautifulSoup 
import openpyxl

dictionary = dict()
final_list = []

wb = openpyxl.Workbook()
wb = openpyxl.load_workbook(filename ='a3WB.xlsx')

def find_average(country):
	sheets = wb.sheetnames
	sheet_avg = wb[sheets[0]]
	for i in range(2,117):
		row_num = i
		country_name_C = "A" + str(row_num)
		average_C = "D" + str(row_num)
		if country==sheet_avg[country_name_C].value:
			return float(sheet_avg[average_C].value)


def normalize_by_average(i):
	sheets = wb.sheetnames
	sheet = wb[sheets[2]]
	country_name = sheet["C" + str(i)].value
	average = dictionary.get(country_name)
	if(average == None):
		print country_name + " Not in Hash"
		average = find_average(country_name)
		dictionary[country_name] = average
	commits = sheet["D" + str(i)].value
	normalized_commits = float(commits/average)
	normalized_location = "E" + str(i)
	sheet[normalized_location].value = normalized_commits
	return average

def normalize():
	sheets = wb.sheetnames
	sheet = wb[sheets[2]]
	current_project = "ActionBarSherlock"
	project_dictionary = dict()
	total_commits = 0
	for i in range(2,12613):
		print i
		country_name = sheet["C" + str(i)].value
		project_name = sheet["B" + str(i)].value
		if current_project == project_name:
			avg = normalize_by_average(i)
			total_commits = total_commits + avg
			if(project_dictionary.get(country_name) == None):
				project_dictionary[country_name] = avg
			else:
				project_dictionary[country_name] = dictionary[country_name] + avg
		else:
			current_project = project_name
			final_list.append(project_dictionary)
			print project_dictionary
			project_dictionary = dict()


			

normalize()
wb.save('temp.xlsx')







