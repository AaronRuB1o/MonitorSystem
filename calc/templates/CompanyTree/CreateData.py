import csv

# Initialize the datasource object
datasource = {
    'id': 'rootNode',
    'collapsed': True,
    'nodeTitlePro': 'Root Node',
    'nodeContentPro': 'Root Node Content',
    'relationship': '111',
    'children': []
}

# Create a dictionary to keep track of nodes by username
node_map = {}

# Read data from the CSV file
with open('OrgChartMatrix.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        name = row['EE Name']
        username = row['EE username']
        sup_name = row['SUP NAME']
        sup_username = row['SUP username']
        title = row['EE Job Title']

        if sup_username == '-':
            # If SUP username is '-', it's the root node
            datasource['children'].append({
                'nodeTitlePro': name,
                'nodeContentPro': title,
                'relationship': '110',
                'children': []
            })
        else:
            if sup_username not in node_map:
                node_map[sup_username] = {
                    'nodeTitlePro': sup_name,
                    'nodeContentPro': '',
                    'relationship': '110',
                    'children': []
                }
            node_map[sup_username]['children'].append({
                'nodeTitlePro': name,
                'nodeContentPro': title,
                'relationship': '110',
                'children': []
            })

# Convert the datasource to JSON format
import json
datasource_json = json.dumps(datasource, indent=2)
print(datasource_json)
