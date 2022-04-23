from array import array
from distutils.command.build import build
import enum
from hashlib import new
from genson import SchemaBuilder 
import json 




class Data2Bot:

    def __init__(self, jsonData=open('./data/data_1.json', 'r'),schema2 = open('./schema/schema_2.json', 'w'),schema1 = open('./schema/schema_1.json', 'w'), jsonData2 =open('./data/data_2.json', 'r')):
        self.jsonData = jsonData
        self.jsonData2 = jsonData2
        self.schema2 = schema2
        self.schema1 = schema1


    def readOpenDataOne(self):
        schema_builder = SchemaBuilder()
        schema_builder2 = SchemaBuilder()
        list_values = []
        list_keys =[]
        Data1 = json.load(self.jsonData)["message"]
        for DataKeys in Data1:
            values = Data1[DataKeys]
            list_keys.append(DataKeys)
            list_values.append(values)
       


        schema_builder.add_schema({"type": "string", "properties": {
            "tag": "",
            "description": ""
        }})
        schema_builder.add_object({list_keys[0]:list_values[0] })
        schema_builder.add_object({list_keys[1]:list_values[1] })
        schema_builder.add_object({list_keys[2]:list_values[2] })
      
        
        
        Data1=schema_builder.to_schema()
        # Data2=schema_builder2.to_schema()
        json.dump(Data1, self.schema1, indent=2)
        # json.dump(Data2, self.schema2, indent=2)


    def readOpenDataTwo(self):
        schema_builder2 = SchemaBuilder()
        list_values = []
        list_keys =[]
        Data2 = json.load(self.jsonData2)["message"]
        for DataKeys in Data2:
            values = Data2[DataKeys]
            list_keys.append(DataKeys)
            list_values.append(values)
    
        schema_builder2.add_schema({"type": "string", "properties": {}})
        schema_builder2.add_object({list_keys[0]:list_values[0] })
        schema_builder2.add_object({list_keys[1]:list_values[1] })
        schema_builder2.add_object({list_keys[2]:list_values[2] })
        schema_builder2.add_object({list_keys[3]:list_values[3] })
        schema_builder2.add_object({list_keys[4]:list_values[4] })

        schema_builder2.add_object({"tag": ""})
        schema_builder2.add_object({"description": ""})
        
        
        Data2=schema_builder2.to_schema()
        # Data2=schema_builder2.to_schema()
        json.dump(Data2, self.schema2, indent=2)

        

