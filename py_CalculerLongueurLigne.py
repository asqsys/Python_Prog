# -*- coding: UTF-8 -*-
import os
import csv
import re
import sys, getopt
################################################################################
#-IMPORTATION DE MODULES INTERNES
from datetime import datetime

################################################################################
#-ARGUMENT A UTILISER EN LIGNE DE COMMANDE
file_name = sys.argv[1]
v_separateur = sys.argv[2]
v_longueur_cible = sys.argv[3]
#file_name = '84K_NF_Fixe_2PK.csv' #@param {type:'string'}
#file_name = '12K_SAMPLE_Fixe.csv' #@param {type:'string'}

################################################################################
#-DECLARATION DE FONCTIONS
def f_calculer_longueur(v_cell):
  len_v_cell = len(v_cell)
  return len_v_cell

def f_invite_choisir_fichier():
  print ()

def f_output_fichier(v_result_output, v_curseur, v_num_ligne):
 fw=open(v_result_output,'w')
 v_tmp=''.join(v_curseur)
 fw.write('L: '+str(i)+' Nb char: '+str(v_num_ligne)+'\t'+v_tmp+new_line)
 fw.close()

def f_horodatage():
 v_date_traitement = datetime.today()
 return str(v_date_traitement)
################################################################################
#-VARIABLES ET DECLARATIONS PROPRES AUX TRAITEMENTS A EFFECTUER
file_structure = [4,10,50,1,10,4,4,10,1] #not used
longueur_fixe= v_longueur_cible
#longueur_fixe= 135 #94
new_line='\n'
char_to_delete = 'Xo' #not used

#print (len(file_structure)) #to check how many fields in structure file
#print (len(sys.argv)) #to check how many argument are used

#print 'Process ongoing ...'
#print 'DATE DEBUT DE TRAITEMENT: '+'\t'+f_horodatage()
################################################################################
#-VARIABLES POUR LE PROGRAMME
file_output = 'RES'+'.csv' #+str(v_date)+
file_error = 'ERR'+'.csv'
i=0
ligne_reader=''

################################################################################
#-CORPS PROGRAMME
with open(file_name) as csvfile:
    sreader = csv.reader(csvfile)
    with open(file_output,'w') as wfile:
      row_structure = []
      for c_row in sreader:
        i+=1
        v_nb_char_by_row=0
        #ligne_reader = c_row[0].split(v_separateur)
        ligne_reader = c_row[0]
        for cell in ligne_reader:
          v_nb_char_by_row += f_calculer_longueur(cell)
          #-----------------LOG Stdout
          #print (i,' ', 'Longueur de la ligne: ', v_nb_char_by_row)
          #print ('\t',cell.replace('X','x'),'\t', f_calculer_longueur(cell))
        if v_nb_char_by_row == longueur_fixe:
            v_tmp=''.join(c_row)
            wfile.write(v_tmp+new_line)
            #sec_pass=v_tmp.replace('o','x')
            #wfile.write(sec_pass+new_line)
        else:
            f_output_fichier(file_error,c_row,v_nb_char_by_row)
          #with open(file_error,'w') as logFile:
              #v_tmp=''.join(c_row)
              #logFile = open(file_error,'w')
              #logFile.write('L: '+str(i)+' Nb char: '+str(v_nb_char_by_row)+'\t'+v_tmp+new_line)
#print 'DATE FIN DE TRAITEMENT: '+'\t'+f_horodatage()
wfile.close()
print ('Longueur cible est : ',v_longueur_cible, ' </> Longueur calculée est: ',v_nb_char_by_row)

#Author: Achraf AZZOUZI
#Description: Ce script permet de repérer les lignes qui ne respectent pas la longueur fixe cible
#Le résultat: Si la longueur de la ligne diffère de celle de la cible, la ligne en question est redirigée vers un fichier erreur
#L'objectif étant de vérifier si une ligne respecte la longuer définie 
#Paramètres: 
#---> python py_Creation_FixedLength_R12.py [Fichier_à_véririer] [séparateur_des champs] [Longueur_cible]
#---> exemple: python py_Creation_FixedLength_R12.py input.csv ; 100

#Exemple de INPUT: #1;BAJ;10.2018;PT005;1;;;;FSPTB102;;;0.000;;C00056;EFSL3.1;Billing Adjustment;1;BAJ;10.2018;PT005;1;;;;FSPTB102;;;0.000;;C00056;EFSL3.1;Billing Adjustment;
