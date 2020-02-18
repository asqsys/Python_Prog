import csv
import re
import sys, getopt

#file_name = '84K_NF_Fixe_2PK.csv' #@param {type:'string'}
file_name = '12K_SAMPLE_Fixe.csv' #@param {type:'string'}
def f_calculer_longueur(v_cell):
  len_v_cell = len(v_cell)
  return len_v_cell

def f_creation_fichier_erreur(v_line_to_reject):
  return v_line_to_reject

def f_creation_fichier_output(v_line_to_insert):
  return v_line_to_insert

def f_invite_choisir_fichier():
  print ()

file_structure = [4,10,50,1,10,4,4,10,1]
file_output = 'Trans_File.csv'
file_error = 'log_err.txt'
print (len(file_structure))
print (len(sys.argv))

i=0
char_to_delete = 'Xo'
output=''
ligne_reader=''
longueur_fixe= 94
new_line='\n'
#--fin variables
with open(file_name) as csvfile:
    sreader = csv.reader(csvfile)
    with open(file_output,'w') as wfile:
      row_structure = []
      for c_row in sreader:
        i+=1
        v_nb_char_by_row=0
        ligne_reader = c_row[0].split(';')
        for cell in ligne_reader:
          v_nb_char_by_row += f_calculer_longueur(cell)
          #print('.')
          #-----------------LOG Stdout
          #print (i,' ', 'Longueur de la ligne: ', v_nb_char_by_row)
          #print ('\t',cell.replace('X','x'),'\t', f_calculer_longueur(cell))
        if v_nb_char_by_row == longueur_fixe:
            v_tmp=''.join(c_row)
            sec_pass=v_tmp.replace('o','x')
            wfile.write(sec_pass+new_line)
        else:
          with open(file_error,'w') as logFile:
              v_tmp=''.join(c_row)
              logFile = open(file_error,'w')
              logFile.write('L: '+str(i)+' Nb char: '+str(v_nb_char_by_row)+'\t'+v_tmp+new_line)

logFile.close()
wfile.close()
