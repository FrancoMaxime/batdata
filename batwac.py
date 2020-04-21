import subprocess
import csv
import datetime
import shutil

def batwac(name, count=0):
    if 'SM' in name or "BARBA_0_" in name:
        return None
    tmp_name = name.split(".")[0]
    tmp_name = tmp_name[0:-4]
    my_val = int(tmp_name.split("_")[-1])
    ret = ''
    while ret == '':
        sub = subprocess.Popen("find /storage/ -name '" + tmp_name + "*'", shell=True, stdout=subprocess.PIPE)
        ret = sub.stdout.read()
        tmp_name  = tmp_name[0:-1]

    ret = ret.split("\n")
    found = None
    val = -1
    for i in ret:
        if i != '' and ".wav" not in i:
            tmp = int(i.split('.wa')[0].split('_')[-1])
            if val < tmp and tmp <= my_val:
                found = i
                val = tmp

    if found == None and count < 5:
            name_split = name.split("_")
            date = datetime.datetime.strptime( name_split[1] + "_" + name_split[2], "%Y%m%d_%H%M%S")
            five = datetime.timedelta(minutes=1)
            date -= five
            tmp_name = name_split[0] + "_" + date.strftime("%Y%m%d_%H%M%S") +"_999.wav"
            return batwac(tmp_name, count+1 )

    return found

def find_wac(csvname):
    print(csvname)
    with open(csvname) as csv_file, open('/storage/wacs/not_found.csv', 'w') as notfound:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        csv_not_found = csv.DictWriter(notfound, fieldnames=csv_reader.fieldnames)
        csv_not_found.writeheader()
        for row in csv_reader:
            name = None
            if 'File' in row:
                name = row['File']
            elif 'Fichier' in row:
                name = row['Fichier']
            else:
                print("ERROR 1 : No column File found")
            print(name)
            path = batwac(name)
            print(path)
            if path is None:
                csv_not_found.writerow(row)
            elif '/storage/hd' in path :
                shutil.move(path , "/storage/wacs/" )



#print(batwac("2-BARBA_20160708_000933_499.wav"))
#print(batwac("2-BARBA_0_20160526_234817_257.wav"))
#print(batwac("SM301748__0__20160513_230201_000.wav"))
#print(batwac("A-BARBA_20160507_214004_000.wav"))
#print(batwac("A-BARBA_20160505_214124_000.wav"))
find_wac("/storage/Barbalux_2016/not_found_Barbalux_2016.csv")
