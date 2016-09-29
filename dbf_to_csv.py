'''The program reads all *.dbf files in a folder and exports to *.csv.
Several programs like this are available online. However, I use encoders to read non-ascii characters and latin words. Particularly useful with Spanish databases.
'''

# ADD FOLDER ADDRESS IN THE FOLLOWING LINE:
address = "C:\files\...\"

# ==================================================================================================
import dbfread
from dbfread import DBF
import csv

def file_name(file) :                                                                                                         # OUTPUT HAS THE SAME NAME AS ORIGINAL FILE
	file = file[0:len(file)-3] + "csv"
	return file

def to_csv(file_dbf) :
  table = DBF(file_dbf, encoding="latin1")                                                                                    # OPEN DBF WITH LATIN ENCODING
  myfile = open(file_name(file_dbf), 'wb')                                                                                    # CREATES NEW CSV FILE
  writer = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')                                                 # TO WRITE CSV FILE ROWS
  writer.writerow(table.field_names)                                                                                          # WRITES HEADER
  for record in table :                                                                                                       # READS EACH RECORD OF DBF
      l = list()                                                                                                              # LIST WILL CONTAIN ALL VALUES
      for element in record.values() :
          if isinstance(element, unicode) : l.append(repr(element).replace("u'","").replace("'",""))                          # REPLACES UNICODE BY STRING AND APPENDS TO LIST
          if isinstance(element, type(None)) : l.append("None")                                                               # REPLACES NONETYPE VALUE BY "NONE" AND APPENDS TO LIST
          if isinstance(element, str) or isinstance(element, int) or isinstance(element, float) : l.append(element)           # APPENDS VALUE STR, INT OR FLOAT TO LIST
      writer.writerow(l)                                                                                                      # WRITES CSV.ROW

import glob
all_files = glob.glob(address + "*.dbf")                                                                                      # LISTS ALL DBF FILES IN FOLDER

# EXPORT:
for f in all_files :                                                                                                          # ITERATES FOR EACH FOLDER
	print "Exporting..." + f
	to_csv(f)
