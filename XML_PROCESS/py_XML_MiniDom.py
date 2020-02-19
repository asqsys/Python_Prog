from xml.dom import minidom

mydoc = minidom.parse('sample.xml')
items = mydoc.getElementsByTagName('Object')
v_ligne = mydoc.getElementsByTagName('Row')
v_col = mydoc.getElementsByTagName('Col')

v_i = items.length
v_l = v_ligne.length
v_c = v_col.length

print ('----All attributes:----')
str_separateur = "|"
s_ep = ";"

for j in range(v_i):
	s_valeur_1 = items[j].attributes['Tag'].value
	s_valeur_2 = items[j].attributes['ObjectId'].value
	# i_nbCol_ParSousNoeud = items[j].getAttributeNode('ObjectId').value
	# print s_valeur_1 + str_separateur + s_valeur_2
	p__objets = items[j].getAttribute('Tag')
	# print p__objets
	p__ligne = v_ligne[j].getAttribute('Type')
	p__ligne_D = v_ligne[j].getAttribute('Tag')
	# print p__ligne_D
	p__col = v_col[j].getAttribute('Tag')
	# print p__ligne + s_ep + p__ligne_D + s_ep + p__col
	i_nbRow_ParNoeud = items[j].getElementsByTagName('Row').length
	# print i_nbRow_ParNoeud
	i_nbCol_ParNoeud = items[j].getElementsByTagName('Col').length
	# print i_nbCol_ParNoeud
	for e_elm in v_ligne:
		e_val_1 = e_elm.getAttribute('Tag')
		print (e_val_1)
	for v_elm in v_col:
		# v_val_1 = v_elm.getAttribute('Tag').value
		v_val_1 = v_elm.attributes['Tag'].value
		v_val_2 = "Text"
		print ('\t' + v_val_1 + '\t' + v_val_2)

itemList = mydoc.getElementsByTagName('Object')

for item in itemList [1:]:
	summaryList = item.getElementsByTagName('Row')
	statusList = item.getElementsByTagName('Col')
	# print summaryList.attributes['Tag'].value
	# print get_text(statusList)
