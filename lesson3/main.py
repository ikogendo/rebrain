disks_array = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

answer_parts = {
    0:'На диске ',
    1:' сейчас: ',
    2:'Gb доступно из ',
    'good':'Gb, достаточно место',
    'warning':'Gb, мало место',
    'alarm':'Gb, это ппц как критически мало'
    }

limits = {
    'alarm_gb':10,
    'alarm_percent':5,
    'warn_gb': 30,
    'warn_perc': 10
    }

num =  input ('Введите номер диска от 1 до 7: ')

check=dict()
ratio=[0,0]

if num.isdigit():
    num = int(num)
    if (num>0 and num<8):
        #
        hdd = int(disks_array[num - 1]['total']/(1024*1024*1024))
        used = int(disks_array[num - 1]['used']/(1024*1024*1024))
        ratio[0],ratio[1] = int(hdd-used),int(100-used/hdd*100)
        #
        answer = str(answer_parts.get(0)+str(num)+str(answer_parts.get(1))+str(ratio[0])+str(answer_parts.get(2))+str(hdd))
        #
        if (ratio[0]>=limits.get('warn_gb') and ratio[1]>=limits.get('warn_perc')):
            check['result'] = 'good'
        elif ( ratio[0]<limits.get('alarm_gb') or ratio[1]<limits.get('alarm_percent')):
            check['result'] = 'alarm'
        else:
            check['result'] = 'warning'

        print(answer+str(answer_parts.get(str(check['result']))))

    else:
        print("Такого диска нет")
else:
    print("Не корректный ввод")
