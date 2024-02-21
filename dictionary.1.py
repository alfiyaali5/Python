#dictionary keys : value
name={'john':32,
      'mike':20,
      'time':43,
      'rohan':19
    }
print(name)
print(name['mike'])
name['mike']=40
print(name)

#with dict funtion
people= dict(name="john",age=20,city="nagpur")
print(people)
del people['name']
print(people )
people.clear()
print(people)
#to combine n update
# to update and check the value
cells={
    'samsung':30000,
   'vivo':40000
}
print(cells)
prices={
    'samsung':80000,
    'realme':30000
 }
print(prices)
cells.update(prices)
print(cells)
#to check the condition
print('john' in name)
#to check the length of the dictionary
print(len(name))
#check the items
name.items()
print(name)
print(name.keys( ))
print(name.values( ))
#type 2 we can write the dictionary
dic1=dict()
dic1['john']='40',
dic1['mike']='30',
dic1['rohan']='30'
print(dic1)
#type 3 we
dic2=[('john','13'),('mike','19')]
print(dict(dic2))

