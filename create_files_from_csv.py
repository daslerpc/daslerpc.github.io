import csv
import os.path
from shutil import copyfile


#Py_version = 'Python_2'
Py_version = 'Python_3'

def writeDataTag( tag_name, tag_data, special_type='None' ):
        if special_type == 'category':
                project_file.write(tag_name + ': \n')
        elif not tag_data == '""' and not tag_data == '':
                if special_type == 'subcategory':
                        tag_name = '  ' + tag_name
                project_file.write(tag_name + ': ' + tag_data + '\n')
                
def writeProjectHeader(data_row):
        image_filename = file_name+'.png'
        image_directory = './images/'+collection+'/'
        
        if not os.path.exists(image_directory):
                os.makedirs(image_directory)
            
        if not os.path.isfile(image_directory+image_filename):
                copyfile('./images/cs_umd_logo.png', '.'+image_filename)
                
        writeDataTag('title', '"' + data_row[0] + '"')
        writeDataTag('excerpt', '"' + data_row[1] + '"')
        writeDataTag('collection', data_row[3])
        writeDataTag('subcategory', data_row[4])
        writeDataTag('header','', 'category')
        writeDataTag('teaser', collection+'/'+image_filename, 'subcategory')
        writeDataTag('type', '"' + data_row[5] + '"')
        writeDataTag('date', data_row[6])
        writeDataTag('venue', '"' + data_row[7] + '"')
        writeDataTag('location', '"' + data_row[8] + '"')
        writeDataTag('permalink', '/' + collection + '/' + file_name)
        
        if data_row[3] == 'publications' or data_row[4] == 'statement':
                writeDataTag('paperurl', '"http://daslerpc.github.io/files/' + file_name + '.pdf"')
                
        writeDataTag('citation', '"' + data_row[9] + '"')


##################
##     Main     ##
##################
        
with open('project_list.csv', 'rU') as csvfile:
    csv_reader = csv.reader(csvfile, dialect='excel')
    
    # Skip the header row
    if Py_version == "Python_2":
            csv_reader.next()  # This is for Python 2
    elif Py_version == "Python_3":
            next( csv_reader ) # This is for Python 3
    else:
            raise ValueError('Python version ill-defined.')
    
    for row in csv_reader:
        file_name = row[2]
        collection = row[3]
        date = row[6]

        if not date == '':
                file_name = date + '_' + file_name

        filepath = '_' + collection + '/' + file_name + '.md'
        
        project_file = open(filepath, 'w')

        project_file.write('---\n')
        writeProjectHeader(row)
        project_file.write('---\n')
        project_file.write('\n')
        project_file.write("PAGE_TEMPLATE_GOES_HERE\n")
        project_file.close()

    csvfile.close()

print("All done!")
        
