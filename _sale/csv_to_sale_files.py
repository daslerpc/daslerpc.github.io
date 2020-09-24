import csv
import os.path
import codecs
from shutil import copyfile

#Py_version = 'Python_2'
Py_version = 'Python_3'


#############
# Data Rows #
#############

def writeDataTag( tag_name, tag_data, special_type='None' ):
        if special_type == 'parent':
                project_file.write(tag_name + ': \n')
        elif not tag_data == '""' and not tag_data == '':
                if special_type == 'child':
                        tag_name = '  ' + tag_name
                project_file.write(tag_name + ': ' + tag_data + '\n')
                
def writeItemHeader(data_row):        
        if not os.path.exists('..' + image_directory):
                os.makedirs('..' + image_directory)
            
        if not os.path.isfile('..'+image_filename):
                copyfile('../assets/images/no-image-found.png', '..' + image_filename)
                
        writeDataTag('title', '"' + item_name + '"')
        writeDataTag('collection', "sale")
        writeDataTag('category', item_type)
        writeDataTag('classes', 'wide')
        writeDataTag('header','', 'parent')
        writeDataTag('teaser', image_filename, 'child')
             

##################
##     Main     ##
##################
        
with open('inventory.csv', 'rU') as csvfile:
    csv_reader = csv.reader(csvfile, dialect='excel')
    
    # Skip the header row
    if Py_version == "Python_2":
            csv_reader.next()  # This is for Python 2
    elif Py_version == "Python_3":
            next( csv_reader ) # This is for Python 3
    else:
            raise ValueError('Python version ill-defined.')
    
    for data_row in csv_reader:
            item_qty = data_row[0]
            item_name = data_row[1]
            item_status = data_row[2]
            item_type = data_row[3]
            item_do = data_row[4]
            item_price_each = data_row[10]
            item_bundle_price = data_row[11]            
            item_desc = data_row[12]
            item_notes = data_row[13]

            if item_price_each == '':
                    item_price_each = 'Preisvorschlag'
            else:
                    item_price_each = item_price_each + '€'
                        
                    
            item_clean_name = item_name.lower().replace(" ", "_")

            image_directory = '/assets/images/sale/'
            image_filename = image_directory + item_clean_name +'.png'
                
            if item_do == "Sell":

                project_file = codecs.open(item_clean_name + '.md', 'w',  "utf-8")

                project_file.write('---\n')
                writeItemHeader(data_row)
                project_file.write('---\n')        
                project_file.write('\n')
                project_file.write(item_desc + '\n')

                project_file.write('\n')
                project_file.write('<img src="' + image_filename + '" alt="' + item_name + '">\n')
                project_file.write('\n')

                if item_qty != '':
                        project_file.write('   **Quantität**: ' + item_qty + '  \n')
                        project_file.write('   **Preis pro Artikel**: ' + item_price_each + '  \n')
                        if item_bundle_price != '':
                                project_file.write('   **Preis zusammen**: ' + item_bundle_price + '€  \n')
                else:
<<<<<<< HEAD
<<<<<<< HEAD
                        project_file.write('**Preis**: ' + item_price_each + '\n')
=======
                        project_file.write('Preis: ' + item_price_each + '€\n')
>>>>>>> parent of e3a2479c... priceless euro symbol removal
=======
                        project_file.write('Preis: ' + item_price_each + '€\n')
>>>>>>> parent of e3a2479c... priceless euro symbol removal

                project_file.write('\n##### Beachten:\n')
                if item_notes != '':
                        project_file.write(item_notes)
                project_file.close()
        
    csvfile.close()

print("All done!")
        
