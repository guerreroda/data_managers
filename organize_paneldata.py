# GENERATES PANEL X_(i,t)
# Diego Guerrero
# guerreroda at gmail.com
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ADD *.TXT WITH A LINE FOR EACH ID
id_file = ""
# ADD ORIGINAL DATA *.CSV
original_data = ""
# ADD TIME RANGE AS INTEGER.
time = [t1, t2]
'''
This program takes a csv with shape:
         t t+1 t+2 t+3
i    v1  .  .   .   .
i+1  v2  .  .   .   .
i+2  v3  .  .   .   .

returns panel.csv w/ shape:
         v1 v2 v3
i   t     . . .
i   t+n   . . .
i+n t     . . .
'''

import csv
if id_file[len(id_file)-4:len(id_file)] != "txt" : id_file = id_file + ".txt"
handle = open(id_file)                                                                           # TXT w/ i
ids = list()
for line in handle :
    line = line.strip()
    ids.append(line)                                                                             # LIST w/ i

handle = open(original_data, 'r')                                                                # OPENS ORIGINAL DATA FILE
header = ["id", "time"]                                                                          # CREATES A LIST WITH HEADERS

for line in handle :
    line = line.strip()
    line = line.split(",")
    var = line[2]
    if var not in header : header.append(var)                                                     # LIST W/ ALL VARIABLES [v1, v2...]
        
with open("panel.csv", 'wb') as myfile :
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')                       # CSV W COMMAND
    wr.writerow(header)                                                                           # FIRST LINE: HEADER
    for i in ids :                                                                                # FOR EACH COUNTRY
        full_vars = dict()                                                                        # DICTIONARY OF VARIABLES
        for v in header :                                                                         # FOR EACH VARIABLE A LIST OF DATA
            if v != "id" and v != "time" : full_vars[v] = list()
        handle = open(original_data, 'r')                                                         # OPEN FULL FILE (DATA)
        for l in handle :
            l = l.strip()
            l = l.split(",")
            i_element = l[0]                                                                      # takes i
            variable = l[1]                                                                       # TAKES VARIABLE NAME
            if i_element.lower() == i.lower() :                                                   # LOOK DATA F EACH i
                t = time[0] -1
                ind = 2                                                                           # BEGINS TO LOOK DATA IN POSITION 2
                data = list()                                                                     # DATA FOR EACH YEAR
                while t < time[1] :
                    t = t + 1
                    data.append(l[ind])
                    ind = ind + 1                                                                 # MOVES TO FOLLOWING POSITION t+1
                full_vars[variable] = data                                                        # INTRODUCE DATA IN VARIABLE
        t = time[0]
        ix = 0
        while t < time[1] :
            i = i.replace(",", "")
            tw = [i, t]                                                                           # TO WRITE LIST COUNTRY/YEAR/DATA
            for it in xrange(len(header)) :
                if it == 0 or it == 1 : continue                                                  # SKIP ID & T
                else :
                    try : tw.append(full_vars[header[it]][ix])
                    except : print i, t, header[it]
            try : wr.writerow(tw)                                                                 # WRITES EACH ROW IN NEW PANEL
            except : print i, t, len(tw)
            ix = ix + 1
            t = t + 1
