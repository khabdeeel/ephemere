import paramiko
import time

# add code to import these credentials from the csv file

#importing pandas as pd
import pandas as pd

# Read and store content
# of an excel file
read_file = pd.read_excel ("test1.xlsx")

# Write the dataframe object
# into csv file
read_file.to_csv ("Test.csv",
				index = None,
				header=True)
	
# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Test.csv"))
csv_data = df.to_csv(columns=['nom du firewall', 'adresse ip correspondante','login','password'])
#print(csv_data)

# show the dataframe
df

fileconnection = open("Test.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
#print(field_names)
for row in lines[1:2]:
    vals = row.strip().split(',')
    
    host=vals[1]  #ipadress
    user=vals[2]  #login
    passx=vals[3] #password
    

#host='140.82.3.191'
#user='hatim'
#passx='anahatim123'


# add code here to bring commands from the csv file
commands = ["mkdir folder","cd folder", "echo 'file created successfuly' > files.txt"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passx)



for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
        print(line.strip('\n'))
        # output all this output to the correspending record in the csv
    time.sleep(.01)
client.close()

