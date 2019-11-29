import datetime
from pyexcelerate import Workbook

# Number of rows and columns
columns = 70
rows = 100000

# Start from the first cell. Rows and columns are zero indexed.
start_col = 0

data = [["somedata" for x in range(columns)] for y in range(rows)]

start = datetime.datetime.now()
print("START " + str(start))

# Iterate over the data and write it out row by row.
wb = Workbook()
wb.new_sheet("sheet name", data=data)
wb.save("output.xlsx")

end = datetime.datetime.now()
print("END " + str())
print(end - start)
