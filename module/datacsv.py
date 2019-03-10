import csv
import random
import os

def dataCSV_userscloud():
    with open(os.getcwd()+'/data/userscloud.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row

def dataCSV_intoupload():
    with open(os.getcwd()+'/data/intoupload.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row

def dataCSV_easyfiles():
    with open(os.getcwd()+'/data/easyfiles.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row

def dataCSV_4downfiles():
    with open(os.getcwd()+'/data/4downfiles.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row