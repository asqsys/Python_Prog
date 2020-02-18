# -*- coding: UTF-8 -*-
import csv
import re
import sys

################################################################################
#Traitement contenu de fichier en utilisant les REGEX
#-IMPORTATION DE MODULES INTERNES
# from datetime import datetime

################################################################################
#-ARGUMENT A UTILISER EN LIGNE DE COMMANDE
file_name = sys.argv[1]
# file_name = 'NewFile.csv'
# longueur_fixe= int(sys.argv[2])

################################################################################
#-DECLARATION DE FONCTIONS
def f_horodatage():
    v_date_traitement = datetime.today()
    return str(v_date_traitement)

def f_calculer_longueur(v_cell):
  len_v_cell = len(v_cell)
  return len_v_cell

################################################################################
#-Messages consoles
##print "Process ongoing ..."
##print 'DATE DEBUT DE TRAITEMENT: '+'\t'+f_horodatage()

################################################################################
#-VARIABLES POUR LE PROGRAMME

################################################################################
#-CORPS PROGRAMME
with open(file_name ) as csvfile:
    sreader = csv.reader(csvfile)
    row_structure = []
    for c_row in sreader:
        # print c_row
        tmp = re.compile('^[\[\']{2}([M,D]{1,2}[5]);([A-Z-0-9]{32});.*(_\d+_\d+.*.);.*')
        first_groupe = re.search(tmp, str(c_row))
        if first_groupe:
          print first_groupe.group(2),';',first_groupe.group(3)

csvfile.close()

#Exemple d'input:---------------------------- Pour l'input j'utise une commande powershell afin de lire les dossier en mode récursif.
#MD5;DBF251FCBE94CC5B5535C40F28BC58C2;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\_07_252019_C\R03\compartool-frontend.zip                        
#MD5;ABE2051715D3CB39FE54B03B5A71EFBC;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\_07_252019_C\R03\html.zip
#MD5;089B936D19C916A05801F095B87E05F2;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolDeployed\ComparTool-0.0.1-SNAPSHOT.jar;  
#MD5;935F3587D2DDDA87476C2B1DED6E601A;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V00\Build_V00.jar  
#MD5;089B936D19C916A05801F095B87E05F2;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V01\ComparTool-0.0.1-SNAPSHOT.jar            
#MD5;D201AE24C6A1FE3617DB1F3CCDEB13DC;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V07\Build_V00.jar  
#MD5;3C8F1B813D78EB8BE78FFFAA56F812F7;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V08\Build_V00.jar  
#MD5;D7995FDA6B9875936FCE65F0752D5123;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V09\Build_V00.jar  
#MD5;E1885FEEACBE0E8B8AFDCB3FFD13EA74;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V10\Build_V00.jar  
#MD5;CFC2993A9CEE45AF04C96DB1C8199973;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V11\Build_V00.jar  
#MD5;D8A29F52D63AA6E28C46FAB9A1D50F1C;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V12\Build_V00.jar  
#MD5;181D1D2DDF98E47E6FC6496B0F57FA85;C:\Users\a-azzouzi\OneDrive - AXA\AXA One IT\QASolutions\00_DataComp\Delivery\CompareToolVersion\V13\Build_V00.jar  

#Exemple d'output:
#089B936D19C916A05801F095B87E05F2 ; _03_192019\\ComparTool-0.0.1-SNAPSHOT.jar
#0F1DF8368A2C94217BDABA5C80BC840F ; _03_252019\\html.zip
#44AF938010E66A25C3A1560CCF96C5B1 ; _03_292019\\html.zip
#72DF890E44841DC20F50EB2DCD69C36B ; _04_012019\\html.zip
#02A256F1D66579D36394835B13A9AAB9 ; _04_032019\\04_R01\\ComparTool-0.0.1-SNAPSHOT.jar
#B5155F2E92115A70B58ED0F7520FC538 ; _04_162019_C\\04_CodeSource\\compartool-frontend.zip
#4885FB135E4ADE0643190851F0E6A9A4 ; _04_162019_C\\04_CodeSource\\data-comparison.zip
#69FDCC7BA826926B97DBA4FF08217F84 ; _04_162019_C\\04_R01\\ComparTool-0.0.1-SNAPSHOT.jar
#2BA4AD7BEA02BA9F3E35BB17CFAC6789 ; _04_162019_C\\04_R02\\ComparTool-0.0.1-SNAPSHOT.jar
#FD5AF251060D02A9FFB5CD8A63D10C4A ; _04_262019_C\\04_R01\\html_2604191200.zip
#FD5AF251060D02A9FFB5CD8A63D10C4A ; _3004191200_1404.zip
#F0A8910A679EDE487639CDFCC8473DDF ; _05_032019\\CompTool.zip
