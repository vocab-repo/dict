import os
import json
base = ''
fileList = os.listdir('/mnt/c/Users/yang/repo/dict/book')
print((fileList))
for fn in fileList:
    print(fn[:-5])
    ouf = open('/mnt/c/Users/yang/repo/dict/list/'+fn[:-5]+'_list.json','w')
    tm = os.listdir('/mnt/c/Users/yang/repo/dict/dict/'+fn[:-5])
    ne = []
    for i in tm:
        ne.append(i[:-5])
        tm = None
    mstr = "["
    flag = False
    for i in ne:
        if flag:
            mstr+=','
        mstr+='"'
        mstr+=i
        mstr+='"'
        flag = True
    mstr+=']'
    ouf.write(mstr)
    ouf.close()
