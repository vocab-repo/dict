import os
import json
fileList = os.listdir('/mnt/c/Users/yang/repo/dict/book')
print(len(fileList))
for fn in fileList:
    inf = open("/mnt/c/Users/yang/repo/dict/book/"+fn,'r')
    os.mkdir("/mnt/c/Users/yang/repo/dict/dict/"+fn[:-5])
    while True:
        tline = inf.readline()
        if(tline):
            tobj = json.loads(tline)
            tword = tobj['headWord']
            tword=tword.replace(r'/',r'%2F')
            print("/mnt/c/Users/yang/repo/dict/dict/"+fn[:-5]+'/'+tword+'.json')
            ouf = open("/mnt/c/Users/yang/repo/dict/dict/"+fn[:-5]+'/'+tword+'.json','w')
            ouf.write(tline)
            ouf.close()
        else:
            break
    inf.close()
