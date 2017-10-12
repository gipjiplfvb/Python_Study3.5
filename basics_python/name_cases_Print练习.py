name_erice = "Hello Erice, would you like to learn some Python today?"
print (name_erice)
name_1 = "Tom.had"
print (name_1.title())  #每个单词首字母大写
print (name_1.lower())  #每个字母小写   注：这个是常用的
print (name_1.upper())  #每个字母都大写
print ('Albert Einstein once said, "A person who never made a misktake never tried anything new."')
famous_person = "Albert Einstein "
message = '"A person who never made a misktake never tried anything new."'
print (famous_person + 'once said, ' + message)
print (type(message))
#print ({0} + "oncesaid" + {1}).format(famous_person, str(message))
#print (%s + 'once said' + %s)%(famous_person, message)  #%不会用啊。汗个
name = " Alert Einstein "
print (name)
print (name.strip())
print (name.rstrip())
print (name.lstrip())
print (famous_person + ":" + "\n\tonce said, \n\t"+ message)