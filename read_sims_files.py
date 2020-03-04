# created by Khalid Alqarni 02/21/2020
# NOTE: This program will read files from sims files to be easier to copy and post into table


import csv


# NOTE: enter the files name that has the summary file
file_List = ["def","max300","q30"]

# NOTE: you should made the files name summary_i where i is the number of the test
sub_file_list = ["summary_"]

for k in file_List:
    for j in range(1,11):
        summary_list = []
        f = open(k+"/summary_"+str(j), "r")
        print(k+"/summary_"+str(j))
        # NOTE: skipping the first two lines of the file
        count_row1 = 0
        count_row2 = 0
        count = 0
        for line in f:
            row2 = line.split(" ")
            row = line.split(": ")
            if count_row1 == 0 or count_row1 == 1:
                count_row1+=1
            elif(count_row1!=0):
                if(len(row)==2):
                    summary_list.append(row[1].strip("\n\n").strip("\t"))
                    count+=1
                if(count == 18):
                    summary_list.append(row2[4].strip("\n\n").strip("\t"))
            count_row2+=1
        f.close()

        count = 0
        for data in summary_list:
            if count == 16:
                summary_list.remove(data)
            print(data)
            count +=1
        input("Press Enter to Skip")


        with open(k+"_results.csv",mode="w") as data_file:
            file_writer = csv.writer(data_file)
            file_writer.writerow(["summary_"+str(j)])
            file_writer.writecolumn(summary_list)
