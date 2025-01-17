import csv
import shutil
import subprocess
import os

def batmove(csvname):
    path = '/storage/' + csvname.split(".csv")[0].replace(" ", "_")
    try:
        os.mkdir(path)
    except OSError:
        print("ERROR 0 : Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
    
    pathtmp = "/storage/tests/"
    
    print "Finding file : " 
    with open('./result/result_' + csvname) as csv_file, open(path + '/found_' + csvname, 'w') as found, open(path + '/not_found_' + csvname, 'w') as notfound, open(path + '/duplicate_'+ csvname, 'w') as duplicate:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        
        csv_found = csv.DictWriter(found, fieldnames=csv_reader.fieldnames)
        csv_found.writeheader()
        
        csv_not_found = csv.DictWriter(notfound, fieldnames=csv_reader.fieldnames)
        csv_not_found.writeheader()

        csv_duplicate = csv.DictWriter(duplicate, fieldnames=csv_reader.fieldnames)
        csv_duplicate.writeheader()

        for row in csv_reader:
            name = None
            if 'File' in row:
                name = row['File']
            elif 'Fichier' in row:
                name = row['Fichier']
            else:
                print("ERROR 1 : No column File found")
            if row['Contact'] != 'Secondaire':
                sub = subprocess.Popen("find /storage/ -name '" + name + "'", shell=True, stdout=subprocess.PIPE)
                ret = sub.stdout.read()
            
                if ret == '':
                    print('NOT FOUND FILE : ' + name )
                    csv_not_found.writerow(row)
                else:
                    ret = ret.split('\n')
                    if not os.path.exists(pathtmp + name):
                        if 'storage/hd' in ret[0]:
                            shutil.move(ret[0], pathtmp)
                            csv_found.writerow(row)
                            print "."
                        else:
                            print("ERROR 3 : File found not in hdx!")
                            csv_duplicate.writerow(row)
                    else:
                            csv_duplicate.writerow(row)
            else:
                csv_duplicate.writerow(row)

    print "Time Expansion : "
    for x in os.listdir(pathtmp):
        sub = subprocess.Popen("soxi " + pathtmp + x , shell=True, stdout=subprocess.PIPE)
        ret = sub.stdout.read()
        ret = ret.split("\n")
        rate = int(ret[3].split(":")[-1])
        if rate > 100000:
            rate /= 10
            
        sub = subprocess.Popen("sox -r " + str(rate) + " " + pathtmp + x + " " + path + "/" + x , shell=True, stdout=subprocess.PIPE)
        print "."

    print "Manage duplicate : "
    try:
        os.mkdir(path+"/duplicate")
    except OSError:
        print("ERROR 0 : Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
        
    with open(path + '/duplicate_'+ csvname) as duplicate:
        csv_duplicate = csv.DictReader(duplicate, delimiter=',')
        for row in csv_duplicate:
            name = None
            if 'File' in row:
                name = row['File']
            elif 'Fichier' in row:
                name = row['Fichier']
            else:
                print("ERROR 1 : No column File found")
            if os.path.exists(path + "/" + name):
                shutil.move(path + "/" + name, path + "/duplicate/" )
                print "."
        


#batmove('LPB2018.csv')
batmove('Barbalux_2016.csv')
