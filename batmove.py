import csv
import shutil

with open('./csv/result_Tournay-Solvay_DataSM2.csv' + x) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        shutil.move("/storage/hd2/2015/SM2-B/Sons" + row["File"], "/storage/Tournay-Solvay-DataSM2" + row["File"])
