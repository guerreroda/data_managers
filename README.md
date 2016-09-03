# data_managers
Here I post some codes I use to manage data structures.

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
