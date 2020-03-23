import csv
import shutil

with open('./result/result_Tournay-Solvay_DataSM2.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        if count == 0:
            shutil.move("/storage/hd2/2015/SM2-B/Sons/" + row["File"], "/storage/Tournay-Solvay-DataSM2" + row["File"])
            count = 42
        else:
            print("FLIP")
