# created by Khalid Alqarni 02/21/2020
# NOTE: This program will read files from sims files to be easier to copy and post into table


import csv


# NOTE: enter the files name that has the summary file
file_List = ["batmFCFS","batmrr","batmsjf","batmsrt2"]

# NOTE: you should made the files name "summary_i" where "i" is the number of the file
sub_file_list = ["summary_"]

for k in file_List:
    for j in range(1,11):
        summary_list = []
        f = open(k+"/summary_"+str(j), "r")
        print(k+"/summary_"+str(j))
        # NOTE: skipping the first two lines of the file
        count_row1 = 0
        count_row2 = 0
        checked = False
        
        for line in f:
            row = line.split(": ")
            if(checked):
                print(row[1])
            if(row[0] == "--------------------------------------\n" ):
                print(row[0])
                checked = True
        f.close()
        input("Press Enter to Skip to the NEXT")

