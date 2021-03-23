import pandas as pd
from math import gcd,sqrt
import sys


df = pd.read_csv("olympic-medals-2012.csv")
rowsnr = len(df.axes[0])
df.head(rowsnr)

def fix_cell(row,col,new_data):
    if col == 0:
        colname = "CountryName"
    elif col == 1:
        colname = "GPD"
    elif col == 2:
        colname = "Population"
    elif col == 3:
        colname = "SilverMedals"
    elif col == 4:
        colname = "GoldenMedals"
    df.at[row,colname]=new_data
    df.to_csv("olympic-medals-2012.csv", index=False)

def hermes_magic_number():
    magicnrval = []
    for i in range(0,rowsnr):
        gdp_value = df.loc[i].at['GDP']
        pop_value = df.loc[i].at['Population']
        magicnumber = sqrt(gcd(gdp_value,pop_value))
        magicnr_formatted = "{:.2f}".format(magicnumber) #2 decimals after . 
        magicnrval.insert(i,magicnr_formatted)
    df['HermesMagicNumber'] = magicnrval
    df.to_csv("olympic-medals-2012.csv", index=False)

def total_medals_column():
    medalsvalues = []
    for i in range(0,rowsnr):
        silvermedalsnr = df.loc[i].at['SilverMedals']
        goldenmedalsnr = df.loc[i].at['GoldenMedals']
        sumofmedals = silvermedalsnr + goldenmedalsnr
        medalsvalues.insert(i,sumofmedals)
    df['Total Medals'] = medalsvalues
    df.to_csv("olympic-medals-2012.csv", index=False)

print(df.head(rowsnr))
user_input = input("Welcome!\nYou can use these 3 functions\n1. Edit a column value\n2. Create the total medals column\n3. Create Hermes magic number column\nPlease type the number of the function you want to use. To exit type exit.\nYour input:")

if user_input == "exit":
    sys.exit(0)
elif user_input == "1":
    usr_input = input("Please type the row number, column number and the new value you want to set.\nSeparate these parameters by one comma\nYour input:")
    split = usr_input.split(",",3)
    row_input = int(split[0])
    col_input = int(split[1])
    new_data_input = split[2]
    fix_cell(row_input,col_input,new_data_input) 
    print("Column value set successfully!")
    print(df.head(rowsnr))
    input("Press Enter to continue...")
elif user_input == "2":
    total_medals_column()
    print("The total medals column has been created successfully!")
    print(df.head(rowsnr))
    input("Press Enter to continue...")
elif user_input == "3":
    hermes_magic_number()
    print("The Hermes magic number column has been created successfully!")
    print(df.head(rowsnr))
    input("Press Enter to continue...")
else:
    user_input = input("Your input was incorrect!")
    sys.exit(0)
       

