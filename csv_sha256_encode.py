import csv
import hashlib
read_filename = '/Users/sakairyoei/Desktop/samp.csv'

with open(read_filename, mode='r', encoding='utf8', newline='') as f:
    reader = csv.reader(f)
    for data in reader:
        data = "".join(data)
        hash_data = hashlib.sha256(data.encode()).hexdigest()
        print(hash_data)
