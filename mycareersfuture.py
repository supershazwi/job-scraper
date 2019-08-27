from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import csv
from datetime import datetime

# driver.get('https://www.mycareersfuture.sg/search?sortBy=new_posting_date&page=0')

page = 0

while page < 101:
	print str(page)
	url = "https://www.mycareersfuture.sg/search?sortBy=new_posting_date&page="+str(page)

	ff = webdriver.Firefox()
	ff.get(url)
	try:
	    element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.NAME, "job_title")))
	finally:
		soup=BeautifulSoup(ff.page_source, 'html.parser')

		soup_link_array = soup.find_all("a", {"class":"bg-white"})

		id_array = []
		link_array = []
		company_array = []
		title_array = []
		type_array = []
		level_array = []
		category_array = []
		job_array = []

		for link in soup_link_array:
			if "https://" not in link['href']:
				link_array.append("https://www.mycareersfuture.sg" + link['href'])
				split_link = link['href'].split("-")
				id_array.append(split_link[-1])

		ff.quit()

		for link in link_array:
			print(link)
		
		for link in link_array:
			ff = webdriver.Firefox()
			ff.get(link)
			print(link)
			try:
			    element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "job_title")))
			finally:
				soup=BeautifulSoup(ff.page_source, 'html.parser')

				level = soup.find("p", {"id":"seniority"})
				level = level.text.strip()
				if u'\xa0' in level:
					level = level.replace(u'\xa0', u' ')
				if u'\u2013' in level:
					level = level.replace(u'\u2013', u'-')
				if u'\uff08' in level:
					level = level.replace(u'\uff08', u'(')
				if u'\uff09' in level:
					level = level.replace(u'\uff09', u')')
				if u'\u2019' in level:
					level = level.replace(u'\u2019', u"'")
				if u'\u2018' in level:
					level = level.replace(u'\u2018', u"'")
				if u'\u200b' in level:
					level = level.replace(u'\u200b', u"")
				if u'\u201c' in level:
					level = level.replace(u'\u201c', u'"')
				if u'\u201c' in level:
					level = level.replace(u'\u201c', u'"')
				if u'\u201d' in level:
					level = level.replace(u'\u201c', u'"')

				level_array.append(level)

				company = soup.find("p", {"class":"f6 fw6 mv0 black-80 mr2 di ttu"})
				company = company.text.strip()
				if u'\xa0' in company:
					company = company.replace(u'\xa0', u' ')
				if u'\u2013' in company:
					company = company.replace(u'\u2013', u'-')
				if u'\uff08' in company:
					company = company.replace(u'\uff08', u'(')
				if u'\uff09' in company:
					company = company.replace(u'\uff09', u')')
				if u'\u2019' in company:
					company = company.replace(u'\u2019', u"'")
				if u'\u2018' in company:
					company = company.replace(u'\u2018', u"'")
				if u'\u200b' in company:
					company = company.replace(u'\u200b', u"")
				if u'\u201c' in company:
					company = company.replace(u'\u201c', u'"')
				if u'\u201d' in company:
					company = company.replace(u'\u201c', u'"')

				company_array.append(company)

				title = soup.find("h1", {"id":"job_title"})
				title = title.text.strip()
				if u'\xa0' in title:
					title = title.replace(u'\xa0', u' ')
				if u'\u2013' in title:
					title = title.replace(u'\u2013', u'-')
				if u'\uff08' in title:
					title = title.replace(u'\uff08', u'(')
				if u'\uff09' in title:
					title = title.replace(u'\uff09', u')')
				if u'\u2019' in title:
					title = title.replace(u'\u2019', u"'")
				if u'\u2018' in title:
					title = title.replace(u'\u2018', u"'")
				if u'\u200b' in title:
					title = title.replace(u'\u200b', u"")
				if u'\u201c' in title:
					title = title.replace(u'\u201c', u'"')
				if u'\u201d' in title:
					title = title.replace(u'\u201c', u'"')

				title_array.append(title)

				type = soup.find("p", {"id":"employment_type"})
				type = type.text.strip()
				if u'\xa0' in type:
					type = type.replace(u'\xa0', u' ')
				if u'\u2013' in type:
					type = type.replace(u'\u2013', u'-')
				if u'\uff08' in type:
					type = type.replace(u'\uff08', u'(')
				if u'\uff09' in type:
					type = type.replace(u'\uff09', u')')
				if u'\u2019' in type:
					type = type.replace(u'\u2019', u"'")
				if u'\u2018' in type:
					type = type.replace(u'\u2018', u"'")
				if u'\u200b' in type:
					type = type.replace(u'\u200b', u"")
				if u'\u201c' in type:
					type = type.replace(u'\u201c', u'"')
				if u'\u201d' in type:
					type = type.replace(u'\u201c', u'"')

				type_array.append(type)

				category = soup.find("p", {"id":"job-categories"})
				category = category.text.strip()
				if u'\xa0' in category:
					category = category.replace(u'\xa0', u' ')
				if u'\u2013' in category:
					category = category.replace(u'\u2013', u'-')
				if u'\uff08' in category:
					category = category.replace(u'\uff08', u'(')
				if u'\uff09' in category:
					category = category.replace(u'\uff09', u')')
				if u'\u2019' in category:
					category = category.replace(u'\u2019', u"'")
				if u'\u2018' in category:
					category = category.replace(u'\u2018', u"'")
				if u'\u200b' in category:
					category = category.replace(u'\u200b', u"")
				if u'\u201c' in category:
					category = category.replace(u'\u201c', u'"')
				if u'\u201d' in category:
					category = category.replace(u'\u201c', u'"')

				category_array.append(category)

				try:
					description_1_exists = soup.find("div", {"id":"descrption-content"})
					description_1 = unicode(soup.find("div", {"id":"description-content"}).find("ul"))

					if description_1 == "None":
						description_1 = unicode(soup.find("div", {"id":"description-content"}).find("p"))

					if description_1 == "None":
						description_1 = unicode(soup.find("div", {"id":"description-content"}))

					if u'\xa0' in description_1:
						description_1 = description_1.replace(u'\xa0', u' ')
					if u'\u2013' in description_1:
						description_1 = description_1.replace(u'\u2013', u'-')
					if u'\uff08' in description_1:
						description_1 = description_1.replace(u'\uff08', u'(')
					if u'\uff09' in description_1:
						description_1 = description_1.replace(u'\uff09', u')')
					if u'\u2019' in description_1:
						description_1 = description_1.replace(u'\u2019', u"'")
					if u'\u2022' in description_1:
						description_1 = description_1.replace(u'\u2022', u"-")
					if u'\u2018' in description_1:
						description_1 = description_1.replace(u'\u2018', u"'")
					if u'\u200b' in description_1:
						description_1 = description_1.replace(u'\u200b', u"")
					if u'\u201c' in description_1:
						description_1 = description_1.replace(u'\u201c', u'"')
					if u'\u201d' in description_1:
						description_1 = description_1.replace(u'\u201c', u'"')

				except AttributeError:
					print(".")

				try:
					description_2_exists = soup.find("div", {"id":"requirements-content"})
					description_2 = unicode(soup.find("div", {"id":"requirements-content"}).find("ul"))

					if description_2 == "None":
						description_2 = unicode(soup.find("div", {"id":"requirements-content"}).find("p"))

					if description_2 == "None":
						description_2 = unicode(soup.find("div", {"id":"description-content"}))

					if u'\xa0' in description_2:
						description_2 = description_2.replace(u'\xa0', u' ')
					if u'\u2013' in description_2:
						description_2 = description_2.replace(u'\u2013', u'-')
					if u'\uff08' in description_2:
						description_2 = description_2.replace(u'\uff08', u'(')
					if u'\uff09' in description_2:
						description_2 = description_2.replace(u'\uff09', u')')
					if u'\u2019' in description_2:
						description_2 = description_2.replace(u'\u2019', u"'")
					if u'\u2022' in description_2:
						description_2 = description_2.replace(u'\u2022', u"-")
					if u'\u2018' in description_2:
						description_2 = description_2.replace(u'\u2018', u"'")
					if u'\u200b' in description_2:
						description_2 = description_2.replace(u'\u200b', u"")
					if u'\u201c' in description_2:
						description_2 = description_2.replace(u'\u201c', u'"')
					if u'\u201d' in description_2:
						description_2 = description_2.replace(u'\u201c', u'"')

				except AttributeError:
					print(".")

				try:
				  description_1
				except NameError:
				  description_1 = ""
				else:
				  print('ok')

				try:
				  description_2
				except NameError:
				  description_2 = ""
				else:
				  print('ok')


				job_array.append(description_1 + "<br/>" + description_2)

				ff.quit()

		# open a csv file with append, so old data will not be erased
		with open('mycareersfuture.csv', 'a') as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(["", "", "", "", "", "", "", "", ""])
			print('writing to excel')
			for counter, data in enumerate(id_array):
				print(id_array[counter])
				writer.writerow([id_array[counter], link_array[counter], company_array[counter], title_array[counter], type_array[counter], level_array[counter], category_array[counter], job_array[counter], datetime.now()])
	page = page + 1