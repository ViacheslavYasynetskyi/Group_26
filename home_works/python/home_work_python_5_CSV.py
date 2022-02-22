

import random
import mimesis
import csv
from mimesis import Person

# for _ in range(0, 20):
#     person_1 = Person('en')
#     f = person_1.full_name()
#     print(f)

file_path ="D:/new_folder/newfolder/QA/IT/python/"
empty_file_title = "empty.csv"
digits_file_title = "digits.csv"
names_file_title = "names.csv"
file_title = file_path + digits_file_title
# with open(file_title,"w") as csv_f:
#     writer = csv.writer(csv_f)

with open(file_title,"w") as csv_2:
    writer = csv.writer(csv_2)
    for i in range(0, 151):
        writer.writerow({str(i)})

# with open(file_title,"w") as csv_2:
#     columns = ["Id"]
#     writer = csv.DictWriter(csv_2, fieldnames=columns)
#     writer.writeheader()
#     for i in range(0, 151):
#         writer = csv.writer(csv_2)
#         writer.writerow(str(i))
# with open(file_title,"w") as csv_2:
#     writer = csv.writer(csv_2)
#     for _ in range(0, 20):
#         person_1 = Person('en')
#         f = person_1.full_name()
#         writer.writerow({str(f)})