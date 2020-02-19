import xml.etree.ElementTree as ET
import csv

tree = ET.parse("data.xml")
root = tree.getroot()

# open a file for writing

Resident_data = open('axaData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []
count = 0
for member in root.findall('Report'):
	print "member"
	resident = []
	address_list = []
	if count == 0:
		name = member.find('MOD_ESG_Score_Spread').tag
		resident_head.append(name)
		PhoneNumber = member.find('TAG_ESGScorePortfolio').tag
		resident_head.append(PhoneNumber)
		EmailAddress = member.find('TAG_ESG_Score_Spread').tag
		resident_head.append(EmailAddress)
		Address = member[3].tag
		resident_head.append(Address)
		csvwriter.writerow(resident_head)
		count = count + 1

	name = member.find('Chart').text
	resident.append(name)
	PhoneNumber = member.find('TAG_Portfolio').text
	resident.append(PhoneNumber)
	EmailAddress = member.find('TAG_Benchmark').text
	resident.append(EmailAddress)
	Address = member[3][0].text
	address_list.append(Address)
	City = member[3][1].text
	address_list.append(City)
	StateCode = member[3][2].text
	address_list.append(StateCode)
	PostalCode = member[3][3].text
	address_list.append(PostalCode)
	resident.append(address_list)
	csvwriter.writerow(resident)
Resident_data.close()
