import json
import csv
from datetime import date

today = date.today()

with open ('Scott_Query_Sheet.csv', 'r') as f1:
    reader = csv.reader(f1)
    reader2 = csv.reader(f1)
    next(reader2)
    next(reader)
    titles = []
    titlesRow = []
    for index, row in enumerate(reader):
        titlesRow.append(row[3])
        if(row[3] in titles):
            continue
        else: titles.append(row[3])

firstIndexOfTitle = []
for value in titles:
    firstIndexOfTitle.append(titlesRow.index(value))


print(firstIndexOfTitle)
print(titles)

currentTitleIndex = 0 

with open ('Scott_Query_Sheet.csv', 'r') as f1:
    reader = csv.reader(f1)
    next(reader)
    groupElements = []
    for index, row in enumerate(reader):
        if(index>22658):
            groupElements.append({
                    'code':row[9],
                    'display':row[11],
                    'target':[{
                        'code':row[14],
                        'display':row[18],
                        'equivalence':'equivalent'
                    }]    
            })
            data =[]
            data.append({
                "resourceType": "ConceptMap",
                "status": "draft",
                'name': 'Vulva.Res', 
                'title': 'Vulva.Res',
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
            with open('./NotFormatted/Vulva.ResnotFormatted.json', 'w') as f:
                json.dump(data,f,indent=4, allow_nan=False)