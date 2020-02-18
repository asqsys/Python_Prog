#Author: Achraf AZZOUZI
#Description: Ce script te permet de calculer la longeur de chaque champs dans le fichier input
#Le résultat peut être redirigé vers un fichier output et utilisé dans Excel ou Access
#L'objectif étant de vérifier si un champ respect e la longuer définie 
#Paramètres: 
#--->Au niveau de la ligne 26, Mettez le nom de votre fichier à auditer.  La commande à exécuter dans la console: cli> python py_Longueur_ParChamps_R01.py
#--->Vous pouvez également l'utiliser comme un paramètre. La commande à exécuter dans la console: cli> python py_Longueur_ParChamps_R01.py nom_du_fichier_en_input.txt
#---> Seuls les fichiers csv & txt sont traités
#Exemple d'output: 
#FR93;[4];7622KQ0Q35;[10];tbdXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;[50];0;[1];oooooooooo;[10];P&Lo;[4];Y241;[4];760301oooo;[10];x;[1];
#Entre les crochets, c'est le champ ajouté par le script Python.
import csv
import re
import sys, getopt

def f_calculer_longueur(v_cell):
  len_v_cell = len(v_cell)
  return len_v_cell

def f_creation_fichier_erreur(v_line_to_reject):
  return v_line_to_reject

def f_creation_fichier_output(v_line_to_insert):
  return v_line_to_insert

file_structure = [4,10,50,1,10,4,4,10,1]
# print (len(file_structure))

i=0
output=''
ligne_reader=''
#Si vous voulez utiliser un paramètre au lieu d'un nom de fichier en dure, remplacer le nom_du_fichier dans la ligne 34 [with open('nom_du_fichier')] par la variable file_name. pour l'utilise se référer à bloc description.
#file_name = sys.argv[1]
with open('12K_SAMPLE_Fixe.csv') as csvfile:
    sreader = csv.reader(csvfile)
    row_structure = []
    for row in sreader:
        i+=1
        v_nb_char_by_row=0
        ligne_reader = row[0].split(';')
        v=''
        v_tmp=''
        for cell in ligne_reader:
          #print '\t',cell,'\t', f_calculer_longueur(cell)
          #resolution = ' '.join([str(largeur_video),"*",str(hauteur_video)])
          v_tmp += ''.join([str(cell),';',str(f_calculer_longueur(str(cell))),';'])
          v_nb_char_by_row += f_calculer_longueur(cell)
        #print v_tmp,' > ',i,' ','Longueur de la ligne: ',v_nb_char_by_row
        print (v_tmp)

#Company Code;Account of Operational CoA;Long text of account of operational CoA;Specify if account is P/L or BS;Group Account Number;Account group;Field status group ;Alternative account number;Posting without tax allowed
#MAR34;SII2922121;Impairment (credit loss) - Government bonds AFSXXX;X;oooooooooo;S2AS;MS03;oooooooooo;x
#MAR21;4204000701;Receivables-Salary tax&empl contrib-Education taxX;X;oooooooooo;ASTo;Y048;4473oooooo;x
#MAR93;7622KQ0L00;Bonds- Inc- Bonds-rel-nonLXXXXXXXXXXXXXXXXXXXXXXXX;0;oooooooooo;P&Lo;Y241;760300oooo;x
#MAR93;7622KQ0Q35;tbdXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;0;oooooooooo;P&Lo;Y241;760301oooo;x
