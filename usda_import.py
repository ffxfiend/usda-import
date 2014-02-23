#!/usr/bin/env python

import sqlite3
import sys
import codecs

print ""

# Create the DB file
conn = sqlite3.connect('usda.sqlite');
conn.text_factory = str

# Parsing the data files.
# The following is straight from the PDF documention on using these
# data files. Data files can be found here: https://www.ars.usda.gov/Services/docs.htm?docid=23634
     
# ASCII files are delimited. All fields are separated by carets (^) and text fields are
# surrounded by tildes (~). A double caret (^^) or two carets and two tildes (~~) appear
# when a field is null or blank. Format descriptions include the name of each field, its type
# [N = numeric with width and number of decimals (w.d) or A = alphanumeric], and
# maximum record length. The actual length in the data files may be less and most likely
# will change in later releases. Values will be padded with trailing zeroes when imported
# into various software packages, depending on the formats used.

# Here is two sample lines from the FOOD_DES.txt file.
# ~01001~^~0100~^~Butter, salted~^~BUTTER,WITH SALT~^~~^~~^~Y~^~~^0^~~^6.38^4.27^8.79^3.87
# ~01002~^~0100~^~Butter, whipped, with salt~^~BUTTER,WHIPPED,WITH SALT~^~~^~~^~Y~^~~^0^~~^6.38^4.27^8.79^3.87

# parseLine:
#
# In this method we parse a single line from one of the data files turning it into 
# a tuple of data points that will be inserted into one of the DB tables.
#
# print parseLine('~01001~^~0100~^~Butter, salted~^~BUTTER,WITH SALT~^~~^~~^~Y~^~~^0^~~^6.38^4.27^8.79^3.87')
def parseLine(line):
	line = line.rstrip('\n\r')
	line = line.replace('~', '')
	line = line.split('^')
	return tuple(line)

def insertDataForFile(fileName,tableName,valuesString):
	f = codecs.open(fileName, encoding='iso-8859-1')
	import_data = []
	for line in f:
		import_data.append(parseLine(line))

	sql = "INSERT INTO %s VALUES %s" % (tableName, valuesString)
	cursor.executemany(sql, import_data)
	f.close()

cursor = conn.cursor()

# Lets create each table
print "Creating DB Tables..."
createDB = open('create_db.sql', 'r')
createSql = createDB.read();
cursor.executescript(createSql)
createDB.close()
print "DONE"

print "Insert Food Descriptions..."
# Import all the food_description data
insertDataForFile('DATA/FOOD_DES.txt', 'food_description', '(?,?,?,?,?,?,?,?,?,?,?,?,?,?)')
print "DONE"

print "Insert Food Groups..."
# Import all the food_group data
insertDataForFile('DATA/FD_GROUP.txt', 'food_group', '(?,?)')
print "DONE"

print "Insert Food Nutrion Data..."
# Import all the nutrition data
insertDataForFile('DATA/NUT_DATA.txt', 'nutrition', '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)')
print "DONE"

print "Insert Food Nutriant Data..."
# Import all the nutrient data
insertDataForFile('DATA/NUTR_DEF.txt', 'nutrient', '(?,?,?,?,?,?)')
print "DONE"

conn.commit()
conn.close()

print "sqlit DB created."
print ""

