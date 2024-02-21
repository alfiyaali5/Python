cloud=['aws','azure','gcp','pcf']
l1=['A','B','C']
print(l1)
print(cloud[0:3]) #index from 0 to 3 it will -1
print(type(cloud))
print(cloud[ -1])
print(cloud[-1:0])
print(cloud[ : ])
#methods in list
cloud.append('oracle')
print(cloud)
#to reverse the whole list
cloud.reverse()
print(cloud)
#to combined 2 list together
cloud.extend(l1)
print(cloud)
#index use to find the particular number place of the words, char, and number also
x=cloud.index('azure')
print(x)
# pop will use to dlt the particular index (0,1,2)
cloud.pop( 0 )
print(cloud)
# remove use to dlt the string
cloud.remove('aws')
print(cloud)
#insert is use to replce the word with another word
cloud.insert(2,'test')
print(cloud)
#tupples
l=(1,4,6,8,3)
print(l)
print(type(l))
#method are same as list but we can't do changes in tuple like list
l.index(4)
print(l)
