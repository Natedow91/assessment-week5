log_file = open("um-server-01.txt")
# the code from line one is Python accessing the code from "um-server-01.text"

# def sales_reports(log_file): 
#     for line in log_file:
#         line = line.rstrip()
#         day = line[0:3]
#         if day == "Mon":
#             print(line)


# sales_reports(log_file)


# def is defining the function to sales_reports
# line 5 is a for loop going through the file we opened
# line 6 is making a new variable with the extra whitespace removed from the right side.
# line 7 is printing from index 0.
# line 8 is specifying which day from index 0
# line 9 is the to actually print.

for line in log_file:
    line = line.rstrip('\n').split(',')
    if line > 10:
    print(line[0])