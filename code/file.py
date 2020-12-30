#Convert file contents into uppercase
with open('data.txt', 'r') as inp:
    content = inp.read().upper()
with open('write.txt', 'a') as out:
    out.write(content)

#Convert file contents into lowercase
with open('data.txt', 'r') as inp:
    content = inp.read().lower()
with open('write.txt', 'a') as out:
    out.write(content)

#Convert file contents into swapcase
with open('data.txt', 'r') as inp:
    content = inp.read().swapcase()
with open('write.txt', 'a') as out:
    out.write(content)

#Convert file contents into capitalize
with open('data.txt', 'r') as inp:
    content = inp.read().capitalize()
with open('write.txt', 'a') as out:
    out.write(content)

#Convert file contents into capitalize
with open('data.txt', 'r') as inp:
    str='a'
    content = inp.read().count(str)
    print(content)

#with open('write.txt', 'a') as out:
#    out.write(content)


