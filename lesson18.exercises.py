students = {'Anna':5,'Jor':10,'Grigor':8,'Hakob':9,'Artavazd':4,'Hranush':3,'Davit':7,'Valod':2,'Artak':5,'Gevorg':6}
# summ = 0
# lenn = 0
# for i in students.values():
# 	lenn += 1
# 	summ += i
# print(summ/lenn)




# minn = 0
# maxx = 0
# for i in students:
# 	if students[i] > minn:
# 		minn = students[i]
# 		c = i
# print(minn,c)		
# for j in students:
# 	if students[j] < minn:
# 		minn = students[j]
# 		v = j
# 		maxx = minn
# print(maxx,v)



# maxx = 5
# for i in students:
# 	if students[i] > maxx:
# 		print(i) 



# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# c = {}
# for i in range(0,len(s),2):
# 	if s[i] in c:
# 		c[s[i]] = int(s[i+1]) + c[s[i]]
# 	else:
# 		c[s[i]] = int(s[i+1])
# print(c)




# word = 'exercises'
# res = {i:word.count(i) for i in word}
# print(res)




old_list = [{'key1':'value1'},{},{},{},{'key1':'value1'},{'key2':'value2'}]
count = 0
for i in range(len(old_list)):
	if old_list.count(old_list[count]) > 1:
		old_list.remove(old_list[count])
	else:
		count += 1
print(old_list)



































