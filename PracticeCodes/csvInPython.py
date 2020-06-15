#Python CSV(comma separated values)
import csv
'''file = open("C:/Users/JT/Documents/SynergisticIT/Python/empno.csv")
reader = csv.reader(file)
data = list(reader)
for i in data:
    print(i)

for i in data:
    print(i[0],'|',i[2])
file.close()'''

#Write over file
'''file = open("C:/Users/JT/Documents/SynergisticIT/Python/empno.csv","w",newline='')
writer = csv.writer(file)
writer.writerow(['8888','sanoths','345434'])
writer.writerow(['7777','jjjj','33333'])
file.close()'''
#Append to file
file = open("C:/Users/JT/Documents/SynergisticIT/Python/empno.csv","a",newline='')
writer = csv.writer(file)
writer.writerow(['555','ssss','34'])
writer.writerow(['7','jkkk','39999'])
file.close()
