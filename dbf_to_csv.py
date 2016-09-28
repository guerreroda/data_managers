import dbfread
from dbfread import DBF
import csv

def to_csv(file_dbf) :
  table = DBF(file_dbf, encoding="latin1")                                                                                    # OPEN DBF WITH LATIN ENCODING
  myfile = open("new.csv", 'wb')                                                                                              # CREATES NEW CSV FILE
  writer = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')                                                 # TO WRITE CSV FILE ROWS
  writer.writerow(table.field_names)                                                                                          # WRITES HEADER
  for record in table :                                                                                                       # READS EACH RECORD OF DBF
      l = list()                                                                                                              # LIST WILL CONTAIN ALL VALUES
      for element in record.values() :
          if isinstance(element, unicode) : l.append(repr(element).replace("u'","").replace("'",""))                          # REPLACES UNICODE BY STRING AND APPENDS TO LIST
          if isinstance(element, type(None)) : l.append("None")                                                               # REPLACES NONETYPE VALUE BY "NONE" AND APPENDS TO LIST
          if isinstance(element, str) or isinstance(element, int) or isinstance(element, float) : l.append(element)           # APPENDS VALUE STR, INT OR FLOAT TO LIST
      writer.writerow(l)                                                                                                      # WRITES CSV.ROW

# ADD FILE ADDRESS IN THE FOLLOWING LINE:
to_csv("*.dbf")
