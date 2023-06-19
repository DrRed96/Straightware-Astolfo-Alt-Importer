import os
import json

print("Importing alts from Astolfo")

appdata = os.getenv("appdata")

straightware_alt_file_name = appdata + "\\.minecraft\\Straightware\\cookiealts.txt"
astolfo_alt_file_name = appdata + "\\astolfo\\alts.json"

astolfo_alt_file = open(astolfo_alt_file_name)
astolfo_alt_data = json.loads(astolfo_alt_file.read())
astolfo_alt_file.close()

imported_alts = 0

straightware_alt_file = open(straightware_alt_file_name, "a")

for name,value in astolfo_alt_data.items():
    if value["microsoft"]:
        imported_alts += 1
        display = value["display"]
        clientToken = value["clientToken"].replace("-", "")
        accessToken = value["accessToken"]
        straightware_alt_file.write(f"\n{display}:{clientToken}:{accessToken}")
        
straightware_alt_file.close()
        
        
print(f"Imported {imported_alts} alts")
