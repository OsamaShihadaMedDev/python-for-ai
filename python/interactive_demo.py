import datetime
import os
import json
import math
# using import a local function to find out what date it is
today = datetime.date.today()
print(today)
#using import yo get a project directory
file_dict = print(os.getcwd())
#using import to parse a JSON object
data = {
    "id": "407882406",
    "name" : "my name",
    "major": "MBBS",
    "job" : "doctor",
    "hobbies": ["reading", "coding", "traveling"]
}
json_object = json.dumps(data)
print(json_object)
# calculating a circlue area using math module
def calculate_area (radius):
    area = math.pi * radius **2
    return area
print("The area of the circle is: ", calculate_area(15))
# claculating crcl based on parameters
def calculate_crcl(age, bw, is_female, cr):
    def make_base(age, bw, cr):
        crcl = ((140 - age) * bw) / (0.9 * cr * 72)
        return crcl
    crcl = make_base(age, bw, cr)
    if (is_female == True):
        answer = crcl * 0.85
    else:
        answer = crcl

    print("The calculated crcl is: ", answer)
    
print(calculate_area(2))
print(calculate_area(10))
calculate_crcl(30, 70, True, 1.2)