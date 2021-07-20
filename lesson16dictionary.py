# res = 0
# c = []
# while True:

# students = {'Name':None,'Email':None,'Phone':None}
# user = input('Name = ')
# email = input('Email = ')
# phone = input('Phone = ')
# students['res']['Name'] = user
# students['res']['Email'] = email
# students['res']['Phone'] = phone
# c.append(students)
# res += 1
# if res == 3:
# 	break

# print(c)
  






# thisdect = {'name':"Aram",'year':1994}
# print(len(thisdect))

# # thisdect = {'name':"Aram",'year':1994}
# # print(lists(thisdect))



# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# for test in students:
# 	print(test)

# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# for test in students.values():
# 	print(test)

# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# for key,value in students.items():
# 	print(key,value)

# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# del students['Anna']
# print(students)


# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# for key,value in students.items():
# 	if value == 12:
# 		print(key,value)



# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# for key in students:
# 	if students[key] == 12:
# 		print(key )

# students = {'Anna':9,'Hakob':12,'Ando':12,'Hasmik':8,'Hermine':13,'Aram':8}
# x = students.popitem()
# print(x)


students = {'Anna':9,'Hakob':10,'Ando':12,'Hasmik':11,'Hermine':13,'Aram':8}
# gn = 0
# qanak = 0
# for value in students.values():
# 	gn += 1
# 	qanak += value
# res = qanak / gn
# print(res)

#amenabarcr stacoxy

mec = 0
z = ''
for i in students:
	if students[i] > mec:
		 mec = students[i]
		 z = i
print(mec,z)

f = ''
for i in students:
	if students[i] < mec:
		 mec = students[i]
		 f = i
print(mec,z)




print(max(students.values()))
print(min(students.values()))