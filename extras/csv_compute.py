import csv


with open("helper_files/stocks.csv") as f:
    read_csv = csv.reader(f)
    for i in read_csv:
        print(i)


# with open("mnist_test.csv") as f:
#     read_csv = csv.DictReader(f)
#     for i in read_csv:
#         print(i.get("21x17"))
#         break


# headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
# rows = [
#     ("AA", 39.48, "6/11/2007", "9:36am", -0.18, 181800),
#     ("AIG", 71.38, "6/11/2007", "9:36am", -0.15, 195500),
#     ("AXP", 62.58, "6/11/2007", "9:36am", -0.46, 935000),
# ]


# with open("stocks.csv", "w") as f:
#     writer_object = csv.writer(f)
#     writer_object.writerow(headers)
#     writer_object.writerows(rows)
