def modEmail(email):



	index_of_at = email.index("@")
	
	result = ""
	for i in range(0, index_of_at,1):
		if email[i] != ".":
			result = result + email[i]

	result = result + email[index_of_at:len(email)]
	return result




print(modEmail("marshal.wang@gmail.com"))
print(modEmail("m.arshalwang@gmail.com")) 
print(modEmail("ma.rshal.wan.g@gmail.com")) 
print(modEmail("ma.rshal.wan.g@gma@il.com")) 