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

def find_wac(csv):
    with open(csvname) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            name = None
            if 'File' in row:
                name = row['File']
            elif 'Fichier' in row:
                name = row['Fichier']
            else:
                print("ERROR 1 : No column File found")
                
            print(batwac(name))
            
        

#print(batwac("B-BARBA_20160507_022854_000.wav"))
print(batwac("B-BARBA_20160829_032146_626.wav"))
