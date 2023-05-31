import json,sys

f = open(sys.argv[1],'r')

json_objs = json.load(f)

for x in json_objs:
    if 'content' not in x :
        continue
    content = x['content']
    content = content.replace("\n",'\\n')
    print(content)


