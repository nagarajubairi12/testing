#impot statement
import arcpy
import csv
import sys
import os

#To allow overwritting the outputs change the overwrite option to true
arcpy.env.overWriteOutput = True

#the root directory - make this match your system

root_directory = 'C:\\Users\\Bairi nagaraju\\Desktop\\vscode and ArcPy\\'


#Setup the output feature class
print("Creating new feature class")

#Need to define a projection to display correctly
prj = root_directory + "wgs_84.prj"

#Createing the shape file using arcpy
output_FC = arcpy.CreateFeatureclass_management(root_directory, "PointFeature.shp", "POINT", "", "DISABLED", "DISABLED", prj)
print("Finished creating new feature class")

#The CSV file coming in the content will be written into the shapefile
file_in = root_directory + "311_Harvey_small.csv"

#defineing the fields from the csv that will be accessed
LAT_field = "LATITUDE"
LON_field = "LONGITUDE"
OVERDUE_field = "OVERDUE"
SR_Type_field = "SR TYPE"

#defining the fields in the shape file
fieldName_RecordId = "record_id"
fieldPrecision = 9
filedAlias = "refcode"
fieldName_Overdue = "overdue"
fieldnName_sr = "sr_type"
fieldLength = 255

#create fields in the new shape file
arcpy.AddField_management(output_FC, fieldName_RecordId, "LONG", fieldPrecision, field_alias = filedAlias, field_is_nullable = "NULLABLE")
arcpy.AddField_management(output_FC, fieldName_Overdue, "DOUBLE", field_length = fieldLength)
arcpy.AddField_management(output_FC, fieldnName_sr, "TEXT", field_length = fieldLength)

#opening the csv for reading the content
with open(file_in) as csvfile:
    #read the csv as a dict i.e key:value pairs
    current_data = csv.DictReader(csvfile)
    rowidval = 0
    #begin for loop for the csv dict object and access of the csv fields defind previously starting on line
    for row in current_data:
        #inspect the coordinate value
        print("Coord: " + row[LAT_field]+ ","+ row[LON_field])
        try:
            #the field in the shape file that where
            fields = [fieldName_RecordId, fieldName_Overdue, fieldnName_sr, 'SHAPE@XY']
            #a cursor is used to read/write data to the shape file
            #the code will access the shape file to beeing editing
            cursor = arcpy.da.InsertCursor(output_FC, fields)
            #conver the LAT and LONG from the csv into a list of float values
            XY = (float(row[LON_field]), float(row[LAT_field]))

            #writing a new row of data into the shape file using the contents of the csv that is currently in the loop
            #The order of the data being eriten has to be the same as the variable fields defined around line

            cursor.insertRow((rowidval, float(row[OVERDUE_field]), row[SR_Type_field], XY))
            #Increment the unique ID value By 1 to get ready for the next iteration of the loop
            rowidval +=1
        except Exception:
            #catch any errors that might happend
            e = sys.exc_info()[1]
            print(e.args[0])

#delete cursor object from memeory so that final shapefile can be accessed when the code is finished
del cursor
print("done")
