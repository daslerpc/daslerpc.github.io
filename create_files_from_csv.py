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
        image_directory = '/assets/images/'+collection+'/'
        image_filename = image_directory + file_name+'.png'
        
        if not os.path.exists('.'+image_directory):
                os.makedirs('.'+image_directory)
            
        if not os.path.isfile('.'+image_filename):
                copyfile('./assets/images/cs_umd_logo.png', '.'+image_filename)
                
        writeDataTag('title', '"' + data_row[0] + '"')
        writeDataTag('collection', data_row[2])
        writeDataTag('subcategory', data_row[3])
        writeDataTag('header','', 'category')
        writeDataTag('teaser', image_filename, 'subcategory')
        writeDataTag('type', '"' + data_row[4] + '"')
        writeDataTag('date', data_row[5])
        writeDataTag('venue', '"' + data_row[6] + '"')
        writeDataTag('location', '"' + data_row[7] + '"')
        
        if data_row[2] == 'publications' or data_row[3] == 'statement':
                writeDataTag('paperurl', '"http://daslerpc.github.io/assets/papers/' + file_name + '.pdf"')
                
        writeDataTag('citation', '"' + data_row[8] + '"')


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
        file_name = row[1]
        collection = row[2]
        date = row[5]

        if not date == '':
                file_name = date + '_' + file_name

        filepath = '_' + collection + '/' + file_name
        
        project_file = open(filepath + '.md', 'w')

        project_file.write('---\n')
        writeProjectHeader(row)
        project_file.write('---\n')        
        project_file.write('\n')
                
        project_body = open(filepath + '.bod')
        project_file.write(project_body.read())

        project_file.close()
        
    csvfile.close()

print("All done!")
        
