import json,sys

f = open(sys.argv[1],'r')

obj = json.load(f)

out = open('webqa.decode.json','w')

json.dump(obj,out,ensure_ascii=False ,indent = 4)
