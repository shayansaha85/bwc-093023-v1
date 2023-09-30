import os
import re
import time

filenames = os.listdir("./logs")
files = []
for file in filenames:
    files.append(file)

content = ""

for file in files:
    f_logs = open(os.path.join("./logs", file), "r")
    data = f_logs.readlines()
    f_logs.close()

    filtered_data = []
    for x in data:
        filtered_data.append(x.strip())
    
    for y in filtered_data:
        content = content + y + "\n"


output_file = open("LOGS.log", "w")
output_file.write(content)
output_file.close()

time.sleep(5)

file = open("./LOGS.log", "r")
data = file.read()
file.close()

content = "Work_Orders\n"

x = re.findall(r'Generated WO : (\d+)', data)

unique_wo = list(set(x))

for x in unique_wo:
    content = content + x + "\n"

WO_list = open("Generated_Work_Order.csv", "w")
WO_list.write(content)
WO_list.close()
