# sex = input('Gender (M/F) ').upper()

# age = int(input('Age: '))

# education = input('Education: ').upper()

# work_exp =int(input('Work experience '))

# res  = sex == 'M' and age >= 18 and (education == 'H' or work_exps > 2)

# print ('You entered',res)


# x = 4
# res = not(x < 5 or x < 10)
# print (res)

# x = None
# print(type(x))

# x = 5
# y = 5
# print(id(x))
# print(id(y))
# print(x is y)

# x = '5'
# y = 5
# print(id(x))
# print(id(y))
# print(x is not y)

# dasaran = 'ani , aram , ashot'
# name = input('NAME: ').lower()
# res = name in dasaran 
# print(name,res)

# cars = '14, opel, klorfar ,14'
# date = '2008, 2000, 1996 '
# car = input('car name ')
# year = input('year ')
# res = car in cars and year in date
# print(res,car, cars.count(car))


# kiwi = int(input('How much kiwi we have? '))
# banana = int(input('How much banana we have?'))
# orange = int(input('How much orange we have?'))
# electrocity = input('Does refregirator working? (Y/N) ').lower() == 'yes'
# res = (kiwi >= 0 or orange >= 0 or banana >= 0) and  electrocity
# print('The fruits are in refregirator and its working !! ',res)

# res2 = (kiwi != 0 and orange != 0 and  banana != 0) and not electrocity
# print('The refregirator is working,but it is empty!!!!',res2)



# word = 'my city is Yerevan'
# res = word.replace('Yerevan','Paris')
# print(res)



# print(abs(-12))
#tpum e tvi moduly



a = int(input('Number = '))
res = a // 100
res1 = a // 10 % 10
res2 = a % 10
print(res * '*'+'\n'+ res1 * '*'+ '\n'+res2 * '*' )


