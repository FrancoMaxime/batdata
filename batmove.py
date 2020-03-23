import csv
import shutil

with open('./result/result_SM2-Ligne161.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        if count == 0:
            shutil.move("/storage/hd2/2017/SM2-B/Sons/" + row["File"], "/storage/SM2_Ligne_161_hd2_2017/" + row["File"])
            count = 42
        else:
            print("FLIP")
