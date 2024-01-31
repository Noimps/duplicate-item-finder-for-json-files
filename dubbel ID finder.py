import json
import os
import glob
# Replace 'your_json_file.json' with the path to your JSON file
directory_path = "path to directory"

import json

def find_and_update_duplicate_ids(file_path):
    for subdirectory in next(os.walk(directory_path))[1]:
        json_file_path = os.path.join(directory_path, subdirectory, 'file_name.json')
        print(f"Processing file: {json_file_path}")
    
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        id_counts = {}
        duplicates = []

        for item in data:
            id_value = item.get('id')
            if id_value:
                if id_value in id_counts:
                    id_counts[id_value] += 1
                    new_id = f"{id_value}-dubbel-{id_counts[id_value]}"
                    item['id'] = new_id  
                    duplicates.append(new_id)
                else:
                    id_counts[id_value] = 1


        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)

        if duplicates:
            print("Duplicate 'id' values found and updated in the file:")
            for duplicate_id in duplicates:
                print(duplicate_id)
        else:
            print("No duplicate 'id' values found.")



find_and_update_duplicate_ids(directory_path)