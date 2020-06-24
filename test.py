"""
このファイルに解答コードを書いてください
"""
#path = 'sample1.txt'
path = 'input.txt'

with open(path,"r") as f:
    l = [s.strip() for s in f.readlines()]
    #print(type(l))
    #print(l)

integer = int(l[len(l)-1])

str_list =[]

for i in range(len(l) - 1):
    l_i_split = l[i].split(sep=":", maxsplit=-1)
    #print(l_i_split)
    
    int_i = int(l_i_split[0])
    if integer % int_i == 0:
        #print(l_i_split[0],l_i_split[1])
        str_list.append([l_i_split[0],l_i_split[1]])
        
#print(str_list)

str_list.sort(key=lambda x: int(x[0]))
#print(str_list)

out = []

if not str_list:
    out.append(integer)
    print(out[0])
else:
    for i in range(len(str_list)):
        out += str_list[i][1]

    print("".join(out))