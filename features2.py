import ipaddress
import pandas as pd
import numpy as np
import os

dataset = pd.DataFrame(columns=['Web', 'IP', 'Descript'])
classes = pd.DataFrame(columns=['Id_class'])
# ------------------------------
file = open("WEB.txt", "r")
data = file.read()
list_WEB = data.split("\n")
file.close()
# ------------------------------
file = open("DESCRIPTION.txt", "r")
data = file.read()
list_DESCRIPT = data.split("\n")
file.close()
# ------------------------------
web_ids = np.array(list_WEB)
descript_ids = np.array(list_DESCRIPT)
# ------------------------------------------------------------
# ------------------------------------------------------------
df = pd.ExcelFile('Hacker_Data_Base.xlsx').parse('Patterns')
webs = df['Web_Server_Type'].tolist()
webs = [str(c).upper() for c in webs]
address = df['IP_Address'].tolist()
descripts = df['FROMscription'].tolist()
descripts = [str(c).upper() for c in descripts]
# ------------------------------------------
# SAVE HACKING DATA IN NUMERICAL FEATURES
# ------------------------------------------
total_data = len(webs) if len(webs) < 200 else 400
for i in range(total_data):
    web, descript = webs[i], descripts[i]
    # convert ip address to int
    id_addr = int(ipaddress.ip_address(address[i]))
    # according to save values]
    id_web = np.where(web_ids == web)[0][0]
    id_descript = np.where(descript_ids == descript)[0][0]
    # save features dataset
    new_row = pd.DataFrame.from_records([{'Web': id_web, 'IP': id_addr, 'Descript': id_descript}])
    dataset = pd.concat([dataset, new_row], ignore_index=True)
    new_row1 = pd.DataFrame.from_records([{'Id_class': 0}])
    classes = pd.concat([classes, new_row1], ignore_index=True)

# ------------------------------------------------------------
# ------------------------------------------------------------
df = pd.ExcelFile('Hacker_Data_Base.xlsx').parse('Patterns1')
webs1 = df['Web_Server_Type'].tolist()
webs1 = [str(c).upper() for c in webs1]
address1 = df['IP_Address'].tolist()

# ------------------------------------------
# SAVE NOT HACKING DATA IN NUMERICAL FEATURES
# ------------------------------------------
total_data = len(webs1) if len(webs1) < 200 else 400
for i in range(total_data):
    print(i)
    web = webs1[i]
    # convert ip address to int
    id_addr = int(ipaddress.ip_address(address1[i]))
    # according to save values
    id_web = np.where(web_ids == web)[0][0]
    # save features dataset
    new_row = pd.DataFrame.from_records([{'Web': id_web, 'IP': id_addr, 'Descript': -10}])
    dataset = pd.concat([dataset, new_row], ignore_index=True)
    new_row1 = pd.DataFrame.from_records([{'Id_class': 1}])
    classes = pd.concat([classes, new_row1], ignore_index=True)

path_des = os.getcwd() + '\\'
root_file = os.path.join(path_des, 'features_patternT.csv')
dataset.to_csv(root_file, index=False)
root_file1 = os.path.join(path_des, 'features_classes.csv')
classes.to_csv(root_file1, index=False)
print('save successfully')
