import json ,sys

f = open(sys.argv[1],'r')

all_record_dic = {}
for line in f.readlines():
    line = line.rstrip("\n")
    obj = json.loads(line)
    text = obj['text']
    target = obj['target']
    span2_index = target['span2_index']
    key = text +"\t" + str(span2_index)
    if key not in all_record_dic:
        all_record_dic[key] = []
    tmp_dic = []
    tmp_dic['label'] = obj['label']
    tmp_dic['text'] = text
    tmp_dic['ref_from'] = target['span2_text']
    tmp_dic['ref_to'] = target['span1_text']
    all_record_dic[key].append(tmp_dic)

def gen_statement(tmp_dic):
    ret = {}
    for record in tmp_dic:
        label = record['label']
        if label == 'false':
            continue
        text = record['text']
        ref_from = record['ref_from']
        ref_to = record['ref_to']
        context = '"'+text+'"中的，'+ref_from+"指的是谁？"A
        answer = ref_from+'指的是原文中的"' + ref_to+'"'
        ret['context'] = context
        ret['answer'] = answer
    return ret

def gen_choice(tmp_dic):
    ret = {}
    for record in tmp_dic:
        label = record['label']
        if label == 'false':
            continue
        text = record['text']
        ref_from = record['ref_from']
        ref_to = record['ref_to']
        context = '"'+text+'"中的，'+ref_from+"指的是谁？"A
        answer = ref_from+'指的是原文中的"' + ref_to+'"'
        ret['context'] = context
        ret['answer'] = answer
    return ret



def gen_judgement(tmp_dic):
    return ""

for key in all_record_dic:




