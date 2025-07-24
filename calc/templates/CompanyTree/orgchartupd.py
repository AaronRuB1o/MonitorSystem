import os
import pygsheets

print("Retrieving Data from Gsheets...")
orgChartWorksheet = 'https://docs.google.com/spreadsheets/d/1PqZZibDOG6wpeLL9efyGFBieOu4NcoRr9BTov29h9Ws/edit#gid=308704094'
#path_cred = 'C:\\Scripts\\bons\\IT-DA-9a643fc39003.json'
path_cred = '/mnt/share/scripts/admin_scripts/api/IT-DA-9a643fc39003.json'
gc = pygsheets.authorize(service_file=path_cred)
wks = gc.open_by_url(orgChartWorksheet)
orgChartSheet = wks.worksheet_by_title('LEO')
getOrgChartData = orgChartSheet.get_values('B2', 'G500')

print(str(orgChartSheet))
print("Total Entries : " + str(len(getOrgChartData)))

#templateHtml = 'C:\\Scripts\\xinyx_it\\orgchart\\orgchartTemplate.html'
#orgchartHtml = 'C:\\Scripts\\xinyx_it\\orgchart\\view_leo.html'
templateHtml = '/mnt/share/scripts/admin_scripts/orgchartTemplate.html'
orgchartHtml = '/opt/lampp/htdocs/orgchart/view_leo.html'

def ParseColumnValues(rawList):
    empName, empId, supName, supId, empEmail, empTitle = rawList
    imgPath = 'http://intra.xinyxsemicon.com/orgchart/img/' + empId + '_pic.jpg'
    empDict = {}
    empDict['id'] = empId
    if supName != 'NA':
        empDict['pid'] = supId
    empDict['name'] = empName
    empDict['title'] = empTitle
    empDict['email'] = empEmail
    empDict['img'] = imgPath
    empData = str(empDict).replace("'id'", "id").replace("'title'", "title").replace("'name'", "name").replace("'email'", "email").replace("'img'", "img")
    empData = empData.replace("'pid'", "pid")
    return empData

orgChartList = []
for employee in getOrgChartData:
    empData = ParseColumnValues((employee))
    orgChartList.append(empData)

print("Updating orgchart web page")
mergedList = ',\n'.join(orgChartList)
loadTemplate = open(templateHtml, 'r').read()
outputHtml = open(orgchartHtml, 'w')
outputHtml.write(loadTemplate.replace('ORGCHARTDATA_PLACEHOLDER', mergedList))
outputHtml.close()

print("DONE!")