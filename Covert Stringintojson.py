#.Question07 Convert the string into json and extract the following attributes and print 
#Type Description - #Win32 DLL
#Type Tags - #["executable", "windows", "win32" ,"pe", "pedll"]
#Names - #[ "d196dee3ea38475845b79232b0732084", "d4f49b363cab452602260c2c658df12b36d27279.bin", "ldss9PQPC.xlsm", "I0znS.msc" ]
#Last #Modification Date - 1657137577



import json

# The provided JSON response
json_data = '''
{
   "data":{
      "attributes":{
         "type_description":"Win32 DLL",
         "type_tags":[
            "executable",
            "windows",
            "win32",
            "pe",
            "pedll"
         ],
         "names":[
            "d196dee3ea38475845b79232b0732084",
            "d4f49b363cab452602260c2c658df12b36d27279.bin",
            "ldss9PQPC.xlsm",
            "I0znS.msc"
         ],
         "last_modification_date":1657137577
      }
   }
}
'''

parsed_data = json.loads(json_data)

type_description = parsed_data['data']['attributes']['type_description']
type_tags = parsed_data['data']['attributes']['type_tags']
names = parsed_data['data']['attributes']['names']
last_modification_date = parsed_data['data']['attributes']['last_modification_date']

print("Type Description:", type_description)
print("Type Tags:", type_tags)
print("Names:", names)
print("Last Modification Date:", last_modification_date)
