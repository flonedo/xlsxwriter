import xlsxwriter
import datetime
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Export.xlsx', {'constant_memory': True})
worksheet = workbook.add_worksheet()

# Number of rows and columns
columns = 70
rows = 100000

# Start from the first cell. Rows and columns are zero indexed.
start_row = 0

data = "some awesome example data"
start = datetime.datetime.now()
print("START" + str(start))

# Iterate over the data and write it out row by row.
for x in range(columns):
    for y in range(rows):
        worksheet.write(y, x, data)


workbook.close()

end = datetime.datetime.now()
print("END" + str(end))
print(end - start)
