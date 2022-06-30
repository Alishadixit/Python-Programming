# open mode of file,read mode ,readline
# rb= use to read text in binary form
# rt=usto to read in text form
# readline is use to print line with a new line character
# readlines is use to print character in form of  tuple
f= open("Alisha.txt","rt")
content=f.read()
print(content)
print(f.close())
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())


# content=f.read()
# for line in f:
#     print(line)
# this use to get single letters
# print(content)
# f.close()