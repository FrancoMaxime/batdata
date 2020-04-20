import subprocess

def batwac(name):
    tmp_name = name.split(".")[0]
    my_val = int(tmp_name.split("_")[-1])
    ret = ''
    while ret == '':
        sub = subprocess.Popen("find /storage/ -name '" + tmp_name + "'", shell=True, stdout=subprocess.PIPE)
        ret = sub.stdout.read()
        tmp_name  = tmp_name[0:-1]
        
    ret = ret.split("\n")
    found = None
    val = -1
    for i in ret:
        tmp = int(i.split('.')[0].split('_')[-1])
        if val < tmp and tmp < my_val:
            found = i
            val = tmp
    return found
         
