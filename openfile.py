#ex- reading the data from file where is availaible in current directory
file=open('text','r')
c=file.read()
print(c)
#ex- reading the data from file where file from specific location
file2=open('C:/Users//user//OneDrive//Desktop//sample.txt','r')
c1=file2.read()
print(c1)
# for read a single line
file2=open('C:/Users//user//OneDrive//Desktop//sample.txt','r')
c1=file2.readline()
print(c1)
# to close the file
file2=open('C:/Users//user//OneDrive//Desktop//sample.txt','r')
c1=file2.read()
print(c1)
file2.close()
#write  operation example
file2=open('C:/Users//user//OneDrive//Desktop//sample.txt','a')
c1=file2.write("this is new line added in the file ")
print(c1)
# with variable
file2=open('C:/Users//user//OneDrive//Desktop//sample.txt','a')
v1="\n************************************"
c1=file2.write(v1)
print(c1)

#append
file2=open('C:/Users//user//OneDrive//Desktop//sample.txt','a')
c1=file2.write("\nAppend the new data without over riding ")
print(c1)



