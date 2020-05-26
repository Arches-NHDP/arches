import urllib.request, json
import xlsxwriter
import argparse

argparser = argparse.ArgumentParser(
    description="DANAM image extract")

argparser.add_argument("-u", "--uuid", help="The uuid of the monument in DANAM")

args = argparser.parse_args()

monumentuuid = args.uuid

mnmnt = "https://nhdp-test.kjc.uni-heidelberg.de/resources/" + monumentuuid + "?format=json"
#mnmnt = "https://nhdp-test.kjc.uni-heidelberg.de/resources/d05bfad4-e696-11e9-b125-0242ac130002?format=json"
count = 0
with urllib.request.urlopen(mnmnt) as url:
    data = json.loads(url.read().decode())
filename = str(data['displayname'])
filename = filename[-8:]
print(filename)
wbImage = xlsxwriter.Workbook("C:/AshishFromDell/project/nhdp/experimentations/" + filename + ".xlsx")
wsImage = wbImage.add_worksheet()
row = 0
wsImage.write(row, 0, "No.")
wsImage.write(row, 1, "Category")
wsImage.write(row, 2, "File Name")
wsImage.write(row, 3, "Image Captions")
row +=1
for tiles in data['tiles']:
    if "'type': 'image/" in str(tiles.get('data')):


        jsonstr = str(tiles.get('data')).replace("'", '"')
        jsonstr = jsonstr.replace('href="', "href='")
        jsonstr = jsonstr.replace('" target', "' target")
        jsonstr = jsonstr.replace('"_blank"', "'_blank'")
        jsonstr = jsonstr.replace('"_top"', "'_top'")
        jsonstr = jsonstr.replace("&nbsp;", " ")
        jsonstr = jsonstr.replace("</p>", "")
        jsonstr = jsonstr.replace("<p>", "")
        #jsonstr = jsonstr.replace("</em>", "")
        #jsonstr = jsonstr.replace("<em>", "")
        jsonstr = jsonstr.replace("</strong>", "")
        jsonstr = jsonstr.replace("<strong>", "")
        jsonstr = jsonstr.replace("&#39;", "'")
        #print(jsonstr)
        pos = jsonstr.find("[{")
        reptext =jsonstr[pos-39:pos-3]
        jsonstr = jsonstr.replace(reptext, "imagedata")
        jsonrawdata = eval(jsonstr)
        #print(jsonrawdata)

        count +=1
        #print(count)
        
        try:
            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Primary Image")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['2ed5777e-9323-11e9-bee1-0242ac120006']))
                print(count, "Primary Image", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['2ed5777e-9323-11e9-bee1-0242ac120006'])
                row += 1
        except KeyError:
            pass
        try:
            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Image after 2015")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['2a27ac74-9323-11e9-84e4-0242ac120006']))
                print(count, "Image after 2015", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['2a27ac74-9323-11e9-84e4-0242ac120006'])
                row += 1
        except KeyError:
            pass

        try:
            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Social & religious activities")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['fb0a532e-b8f7-11e9-b8a9-0242ac120007']))
                print(count, "Social & religious activities", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['fb0a532e-b8f7-11e9-b8a9-0242ac120007'])
                row += 1
        except KeyError:
            pass

        try:
            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Maps, Plans & Drawings")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['0266d2a6-9ee9-11e9-98a0-0242ac120006']))
                print(count, "Map, Plans & Drawings", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['0266d2a6-9ee9-11e9-98a0-0242ac120006'])
                row += 1
        except KeyError:
            pass

        try:

            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Image before 2015")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['2ab25f4a-9323-11e9-8381-0242ac120006']))
                print(count, "Image before 2015", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['2ab25f4a-9323-11e9-8381-0242ac120006'])
                row += 1
        except KeyError:
            pass

        try:

            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Additional object images")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['5b384156-b8f9-11e9-a5f7-0242ac120007']))
                print(count, "Additional object images", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['5b384156-b8f9-11e9-a5f7-0242ac120007'])
                row += 1
        except KeyError:
            pass
        try:

            for i in range(0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Objects")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['4b84aef8-9eea-11e9-8b93-0242ac120006']))
                print(count, "Objects", jsonrawdata['imagedata'][i]['name'],
                    jsonrawdata['4b84aef8-9eea-11e9-8b93-0242ac120006'])
                row += 1
        except KeyError:
            pass

        try:

            for i in range (0, len(jsonrawdata['imagedata'])):
                wsImage.write(row, 0, count)
                wsImage.write(row, 1, "Historical activities")
                wsImage.write(row, 2, str(jsonrawdata['imagedata'][i]['name']))
                wsImage.write(row, 3, str(jsonrawdata['8cdd76fc-c332-11e9-af2c-0242ac140003']))
                print(count, "Historical activities", jsonrawdata['imagedata'][i]['name'],
                      jsonrawdata['8cdd76fc-c332-11e9-af2c-0242ac140003'])
                row +=1
        except KeyError:
            pass
#wbImage.getCells().deleteRows(row, 1, True)

wbImage.close()