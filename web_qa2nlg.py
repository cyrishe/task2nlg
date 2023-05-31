import json,sys

f = open(sys.argv[1],'r')

web_qa_list = json.load(f)
ret_list = []
for web_qa_key in web_qa_list:
    ret = {}
    web_qa = web_qa_list[web_qa_key]
    question = web_qa['question']
    context_dic = web_qa['evidences']
    context = ''
    answer = ''
    for key in context_dic:
        context = context_dic[key]['evidence']
        answer = context_dic[key]['answer'][0]
    if answer == 'no_answer':
        continue
            
    ret['context'] = context+' ,根据前面的描述，回答如下问题：'+question
    ret['answer'] = question+', 这个问题的答案是"' + answer+'"'
    ret_list.append(ret)
out=open('web_qa_nlg.json','w')

json.dump(ret_list,out,ensure_ascii=False ,indent = 4)




