import sys
import json,random

f = open(sys.argv[1],'r')

prompt_list = []
prompt_list.append('请解释如下概念：%s')
prompt_list.append('%s 是什么?')
prompt_list.append('描述一下%s')
ret_list = []
for line in f.readlines():
    ret = {}
    line = line.rstrip("\n")
    line = line.replace('.','。')
    arr = line.split("  ",1)
    if len(arr) !=2:
        continue
    term , exp = arr
    if len(exp) < 20:
        continue
    if len(exp) > 300:
        arr = exp.split('。')
        new_exp = ''
        idx = 0
        while len(new_exp) <300 and idx < len(arr):
            new_exp = new_exp + arr[idx]
            idx += 1
        exp = new_exp    
    prompt = random.choice(prompt_list)
    context = prompt % term
    ret['context'] = context
    ret['answer'] = exp
    ret_list.append(ret)

out_file = open('baike_qa.json','w')

json.dump(ret_list , out_file , ensure_ascii=False ,indent = 4)



