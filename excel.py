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
print(field_names)
for row in lines[1:2]:
    vals = row.strip().split(',')
    print(vals[1])#ipadress
    print(vals[2])#login
    
