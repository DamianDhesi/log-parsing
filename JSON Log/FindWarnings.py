import json

file_string : str
with open("./dummy_json.json", "r") as file:
    file_string = file.read()

json_string = json.loads(file_string)

for entry in json_string:
    if (entry["log_level"] == "WARN"):
        print("Warning found:\nevent: {0}\nuser: {1}\nip: {2}\ntarget: {3}".format(entry["event_type"],
                                                                                   entry["user"]["username"],
                                                                                   entry["source"]["ip_address"],
                                                                                   entry["target"]["resource"]))