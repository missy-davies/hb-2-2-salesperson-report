"""Generate sales report showing total melons each salesperson sold."""

# creat empty lists for salespeople and melons 
# salespeople = []
# melons_sold = []

# # open the specific file - an improvement here would be to define a function
# # we could then set a parameter for the function as filename so we could run 
# # this function on any file, not just sales-report.txt
# f = open('sales-report.txt')

# # iterate through each line in the file 
# for line in f:

#     # remote any white space from the right 
#     line = line.rstrip()

#     # create a list entries that splits each line in a pipe character |
#     entries = line.split('|')

#     # save the sales person found at index 0 
#     salesperson = entries[0]

#     # save the number of melons found at index 2 as an integer 
#     melons = int(entries[2])

#     # check if our list of salespeople already contains the person in question
#     if salesperson in salespeople:
#         # if it does, then save the index of where the salesperson is in the list
#         position = salespeople.index(salesperson)
#         # and add to the count in the melons_sold list at the same index
#         melons_sold[position] += melons
#     else:
#         # if the salesperson isn't already on the list, then add them to the end 
#         salespeople.append(salesperson)
#         # and add their melons count to the end of the melons list 
#         melons_sold.append(melons)

# # print a formatted string for each salesperson saying what they sold 
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# this solution is confusing to deal with and difficult to access all relevant
# information for a specific salesperson
# instead it would be more clear to store the data in a dictionary where the 
# salesperson is the key and the melon price total and count are values

# refactored code
def generate_sales_report(filename):
    """Generate sales report showing total melons each salesperson sold.
    
    Create a dictionary of salespeople to easily generate a report of 
    melons sold"""

    logs = open(filename)
    sales_lists = []
    for log in logs:
        split_log = log.rstrip().split("|")
        sales_lists.append(split_log)

    salespeople = {}
    for sales_list in sales_lists:
        person = sales_list[0]
        melons = sales_list[2]
        salespeople[person] = melons

    for salesperson in salespeople.keys():
        print(f"{salesperson} sold {salespeople[salesperson]} melons")

    logs.close()

generate_sales_report("sales-report.txt")