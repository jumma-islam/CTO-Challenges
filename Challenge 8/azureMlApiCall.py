

import urllib
import urllib.request
# If you are using Python 3+, import urllib instead of urllib2
import json 
import csv

file="C:\\Users\\jumma.islam\\OneDrive - Accenture Federal Services\\Training\\CTO Challenges\\Challenge 8\\contest-train-mycase.csv"

with open(file, 'r', newline='') as csvFile:
    hasHeader = csv.Sniffer().has_header(csvFile.read())
    csvFile.seek(0)
    importedCsv = csv.reader(csvFile)
    # skip the header
    if hasHeader:
        next(csvFile)
    # loop on each row and make the API call to Azure Machine Learning
    for row in importedCsv:
        org = row[5]
        cap = row[6]
        title = row[11]
        trainingType = row[12]
        courseName = row[16]
        vendorName = row[18]
        certName = row[22]
        consolidatedName = row[25]
        activity = row[27]



        data = {
                "Inputs": {

                        "input1":
                        {
                            "ColumnNames": ["Organization", "Capability", "Title", "Training Type", "Course Name", "Vendor Name", "Certification Name", "Consolidated Course Name", "Activity"],
                            "Values": [ [ org, cap, title, trainingType, courseName, vendorName, certName, consolidatedName, activity ], [ org, cap, title, trainingType, courseName, vendorName, certName, consolidatedName, activity ], ]
                        },        
                },
                    "GlobalParameters": {
                    }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/da667bb0de274bdaa438cb27728d119a/services/c0143c20cdaf4f70a60d5782788a7213/execute?api-version=2.0&details=true'
        api_key = 'putAPIKeyHere' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers) 
            # response = urllib.request.urlopen(req)

            result = response.read()
            print(result) 
        except urllib.request.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))                 

