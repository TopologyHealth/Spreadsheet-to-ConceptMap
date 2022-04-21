import json
import csv
from datetime import date

today = date.today()

with open ('Scott_Query_wscPopulated.xlsx - Sheet1.csv', 'r') as f1:
    reader = csv.reader(f1)
    next(reader)
    groupElements = []
    for index, row in enumerate(reader):
        if(len(row[14].split('|'))>1):
                groupElements.append({
                        'code':row[9],
                        'display':row[11],
                        'target':[{
                            'code':row[14].split('|')[0][:-1],
                            'display':row[14].split('|')[1],
                            'equivalence':'equivalent'
                        }]    
                })
    data =[]
    data.append({
        "resourceType": "ConceptMap",
        "status": "draft",
        'name': 'CAPCkeyToSNOMEDmap', 
        'title': 'CAPCkeyToSNOMEDmap',
        'experimental': True, 
        'date': str(today),
        'publisher': 'College of American Pathologists',
        "contact":[
            {
                "telecom": [
                    {
                    "system": "email",
                    "value": "agoel@cap.org"
                    }
            ]
            }],
        'description': 'mapping of SNOMED to CAP CKeys',
        'purpose': 'mapping of SNOMED to CAP CKeys',
        'copyright': 'College of American Pathologists 2022',
        'group':[
                
                {
                    'source': 'http://cap.org/eCC',
                    'target': 'http://snomed.info/sct',
                    'element':
                        groupElements
                }
            ]
    })
    with open('./NotFormatted/CAPCkeyToSNOMEDmapNotFormatted.json', 'w') as f:
        json.dump(data,f,indent=4, allow_nan=False)
