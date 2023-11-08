import copy
import json
import avro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader

print("Hello avro from python")
schema = avro.schema.parse(open("../resources/emp.avsc").read())
print(schema)

#read data from avro file to array 'employees'
with open('../resources/emp-data.txt', 'rb') as f:
    reader = DataFileReader(f, DatumReader())
    metadata = copy.deepcopy(reader.meta)
    schema_from_file = json.loads(metadata['avro.schema'])
    employees = [emp for emp in reader]
    reader.close()

print(f'Users:\n {employees}') # print entire list
print(employees[0]["name"]) #we can get ATTRIBUTES also
