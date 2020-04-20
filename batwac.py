import subprocess

def batwac(name):
    tmp_name = name.split(".")[0]
    tmp_name = tmp_name[0:-4]
    my_val = int(tmp_name.split("_")[-1])
    ret = ''
    while ret == '':
        sub = subprocess.Popen("find /storage/ -name '" + tmp_name + "*'", shell=True, stdout=subprocess.PIPE)
        ret = sub.stdout.read()
        tmp_name  = tmp_name[0:-1]

    ret = ret.split("\n")
    print(ret)
    print(name)
    found = None
    val = -1
    for i in ret:
        if i != '':
            tmp = int(i.split('.')[0].split('_')[-1])
            if val < tmp and tmp < my_val:
                found = i
                val = tmp
    return found



#print(batwac("B-BARBA_20160507_022854_000.wav"))
print(batwac("B-BARBA_20160829_032146_626.wav"))
