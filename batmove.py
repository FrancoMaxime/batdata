import csv
import shutil
import subprocess
import os

def batmove(csvname):
    path = '/Storage/' + csvname.split(".csv")[0].replace(" ", "_")
    try:
        os.mkdir(path)
    except OSError:
        print("ERROR 0 : Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
    
    pathtmp = "/storage/tests/"
        
    with open('./result/result_' + csvname) as csv_file, open(path + '/found_' + csvname) as found, open(path + '/not_found_' + csvname) as notfound:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        
        csv_found = csv.DictWriter(found, fieldnames=csv_reader.fieldnames)
        csv_found.writeheader()
        
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
                
            sub = subprocess.Popen("find /storage/ -name'" + name + "'", shell=True, stdout=subprocess.PIPE)
            ret = sub.stdout.read()
            
            if ret == '':
                print('NOT FOUND FILE : ' + name )
                csv_not_found.writerow(row)
            else:
                ret = ret.split('\n')
                shutil.move(ret[0], pathtmp)
    
    for x in os.listdir(pathtmp):
        sub = subprocess.Popen("soxi " + pathtmp + x , shell=True, stdout=subprocess.PIPE)
        ret = sub.stdout.read()
        ret = ret.split("\n")
        rate = int(ret[3].split(":")[-1])
        if rate > 100 000):
            rate /= 10
            
        sub = subprocess.Popen("sox -r " + str(rate) + " " + pathtmp + x + " " + path + x  , shell=True, stdout=subprocess.PIPE)
        
