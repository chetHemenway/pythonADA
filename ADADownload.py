#! python3
# ADADownload.py - downloads ADA files from the web

import datetime, calendar, time, os, shutil, pandas, openpyxl, re
from selenium import webdriver

# gets the current username to pull from the downloads folder
path = os.path.abspath('C:\\Users')
pathFolders = os.listdir(path)
for i in pathFolders:
    if i == 'chehem':
        userName = i
    elif i == 'kevqua':
        userName = i
    elif i == 'keleng':
        userName = i

# gets the date in year and converts to a string
year = datetime.datetime.today().year
lastYear = year - 1
year = str(year)
lastYear = str(lastYear)
# gets the previous month, we are 2 months behind
today = datetime.date.today()
twoMonths = today.month -2
monthName = calendar.month_abbr[twoMonths]
monthYear = year + '-' + '{:02d}'.format(twoMonths)

print('What is the email?')
emailUser = input()

print('What is the password?')
emailPassword = input()

#########DOWNLOAD
# chooses chrome as the browser
browser = webdriver.Chrome()
# goes to the ADA website
browser.get('http://b2b.ada-music.com/gateway/login.asp')
browser.maximize_window()
# Enters the username and password then clicks login
emailElem = browser.find_element_by_name('user_name')
emailElem.send_keys(emailUser)
time.sleep(2)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(emailPassword)
time.sleep(2)
loginButton = browser.find_element_by_id('submit1')
time.sleep(2)
loginButton.click()
# clicks on Financial Information
financialInfoElem = browser.find_element_by_link_text('Financial Information')
financialInfoElem.click()
time.sleep(5)
# switch the frame to download the files
browser.switch_to.frame(0)
time.sleep(2)
# download the files
downloadElem = browser.find_element_by_link_text('Concord_Music_Group_Download_' + monthName + '-' + year + '.xls').click()
time.sleep(15)



#########WIRELESS
# chooses chrome as the browser
browser = webdriver.Chrome()
# goes to the ADA website
browser.get('http://b2b.ada-music.com/gateway/login.asp')
browser.maximize_window()
# Enters the username and password then clicks login
emailElem = browser.find_element_by_name('user_name')
emailElem.send_keys(emailUser)
time.sleep(2)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(emailPassword)
time.sleep(2)
loginButton = browser.find_element_by_id('submit1')
time.sleep(2)
loginButton.click()
# clicks on Financial Information
financialInfoElem = browser.find_element_by_link_text('Financial Information')
financialInfoElem.click()
time.sleep(5)
browser.switch_to.frame(0)
# download the files
wirelessElem = browser.find_element_by_link_text('Concord_Music_Group_Wireless_' + monthName + '-' + year + '.xls').click()
time.sleep(15)



#########STREAM
# chooses chrome as the browser
browser = webdriver.Chrome()
# goes to the ADA website
browser.get('http://b2b.ada-music.com/gateway/login.asp')
browser.maximize_window()
# Enters the username and password then clicks login
emailElem = browser.find_element_by_name('user_name')
emailElem.send_keys(emailUser)
time.sleep(2)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(emailPassword)
time.sleep(2)
loginButton = browser.find_element_by_id('submit1')
time.sleep(2)
loginButton.click()
# clicks on Financial Information
financialInfoElem = browser.find_element_by_link_text('Financial Information')
financialInfoElem.click()
time.sleep(5)
browser.switch_to.frame(0)
# download the files
streamElem = browser.find_element_by_link_text('Concord_Music_Group_Stream_' + monthName + '-' + year + '.xls').click()
time.sleep(90)



#########INTERNATIONAL
# chooses chrome as the browser
browser = webdriver.Chrome()
# goes to the ADA website
browser.get('http://b2b.ada-music.com/gateway/login.asp')
browser.maximize_window()
# Enters the username and password then clicks login
emailElem = browser.find_element_by_name('user_name')
emailElem.send_keys(emailUser)
time.sleep(2)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(emailPassword)
time.sleep(2)
loginButton = browser.find_element_by_id('submit1')
time.sleep(2)
loginButton.click()
# clicks on Financial Information
financialInfoElem = browser.find_element_by_link_text('Financial Information')
financialInfoElem.click()
time.sleep(5)
# switch the frame to download the files
browser.switch_to.frame(0)
# download the files
internationalElem = browser.find_element_by_link_text('Concord_Music_Group_International_' + monthName + '-' + year + '.xls').click()
time.sleep(180)


# go to the filepath and see what all years are listed
adaSourcePath = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone')
adaSouceFiles = os.listdir(adaSourcePath)

# find out if the year was there
if year in adaSouceFiles:
    yearADASource = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone' + year)
    yearADASourceFiles = os.listdir(yearADASource)
    workingYear = year
elif lastYear in adaSouceFiles:
    yearADASource = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone' + lastYear)
    yearADASourceFiles = os.listdir(yearADASource)
    workingYear = lastYear
elif year not in adaSouceFiles and lastYear not in adaSouceFiles:
    os.mkdir(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone' + year)
    sourcePathNew = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone')
    sourcePathNewFiles = os.listdir(sourcePathNew)
    if year in sourcePathNewFiles:
        yearADASource = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone' + year)
        yearADASourceFiles = os.listdir(yearADASource)
        workingYear = year

workingMonthYear = workingYear + '-' + '{:02d}'.format(twoMonths)

# create the destination folders
if workingMonthYear not in yearADASourceFiles:
    os.mkdir(yearADASource + '\\' + workingMonthYear)
    newPath = os.path.abspath(yearGoogleSource + '\\' + workingMonthYear)
    print(newPath + ' was created, for this year, ' + workingYear + ' and month: ' + workingMonthYear)
elif workingMonthYear in yearADASourceFiles:
    print('Month already created.')

#os.mkdir(r'\\cmgfs\Shared\Accounting\Consignment Sales\ADA - Parlophone\2019\\' + year + '-' + '{:02d}'.format(twoMonths))
os.mkdir(yearADASource + '\\' + workingMonthYear + '\\' + 'Concord')

# put files in folder
sourcePath = os.path.abspath('C:\\Users\\' + userName + '\Downloads')
sourceFiles = os.listdir(sourcePath)
destinationPath = os.path.abspath((yearADASource + '\\' + workingMonthYear + '\\' + 'Concord'))

for file in sourceFiles:
    if file.startswith('Concord_Music_Group_'):
        shutil.move(os.path.join(sourcePath, file), os.path.join(destinationPath, file))

print('Finished migrating the files.')

# gets the date in year and converts to a string
year = datetime.datetime.today().year
year = str(year)
# gets the previous month, we are 2 months behind
today = datetime.date.today()

#change this shit 
twoMonths = today.month-3
monthName = calendar.month_abbr[twoMonths]
print('Dates received.')

print('Creating FileDate.')
filedate = '{:02d}'.format(twoMonths) + '-' + '15' + '-' + year
print('FileDate created.')


destinationPath = os.path.abspath('C:\\Users\chehem\Downloads')

# get a list of all the files
#fileList = os.listdir(destinationPath)
print('Getting list of files')
fileList = os.listdir('C:\\Users\chehem\Downloads')

# create the file names to go through each file
startFileName = 'Concord_Music_Group_'
download = 'Download_' + monthName + '-' + year + '-GOOD.xlsx'
stream = 'Stream_' + monthName + '-' + year + '-GOOD.xlsx'
wireless = 'Wireless_' + monthName + '-' + year + '-GOOD.xlsx'
print('Filenames created.')

# combine that shit
downloadPull = startFileName + download
streamPull = startFileName + stream
wirelessPull = startFileName + wireless

# set a variable for each file
for file in fileList:
    if file == downloadPull:
        downloadFile = file
    elif file == streamPull:
        streamFile = file
    elif file == wirelessPull:
        wirelessFile = file
print('Assigning filenames')

# set the filenames
downloadFilename = downloadFile[:-10].strip()
streamFilename = streamFile[:-10].strip()
wirelessFilename = wirelessFile[:-10].strip()


######################Download######################
print('Formatting Download file.')
df = pandas.read_excel(os.path.join(destinationPath, downloadFile))

df['filedate'] = filedate
df['filename'] = downloadFilename

del(df['FIRST_REL_TITLE'])
del(df['LABEL_GROUP_CODE'])
del(df['LABEL_GROUP'])
del(df['EXTENDED_FAMILY'])
del(df['ACTIVE_LABEL'])
del(df['ACTIVE_ADA_LABEL'])
del(df['PRICE_GRADE'])

upcList = []
for upc in df['FIRST_REL_UPC']:
	upc = str(upc)
	upcList.append(upc)
cleanUPC = []
for i in upcList:
	upcCleaner = re.sub('E+', '', i)
	cleanUPC.append(upcCleaner)
df['newUPC'] = cleanUPC
del(df['FIRST_REL_UPC'])

df.to_excel(os.path.join(destinationPath, year + '{:02d}'.format(twoMonths) + downloadFilename + 'FormattedDigitalDomestic.xlsx'),index = False)

print('Donwnload File Formatted')

######################Wireless######################
print('Formatting Wireless file.')
df1 = pandas.read_excel(os.path.join(destinationPath, wirelessFile))

#df1['retail_price'] = ''
df1['filedate'] = filedate
df1['filename'] = wirelessFilename

del(df1['FIRST_REL_TITLE'])
del(df1['LABEL_GROUP_CODE'])
del(df1['LABEL_GROUP'])
del(df1['EXTENDED_FAMILY'])
del(df1['ACTIVE_LABEL'])
del(df1['ACTIVE_ADA_LABEL'])
del(df1['PRICE_GRADE'])

upcList = []
for upc in df1['FIRST_REL_UPC']:
	upc = str(upc)
	upcList.append(upc)
cleanUPC = []
for i in upcList:
	upcCleaner = re.sub('E+', '', i)
	cleanUPC.append(upcCleaner)
df1['newUPC'] = cleanUPC
del(df1['FIRST_REL_UPC'])

df1.to_excel(os.path.join(destinationPath, year + '{:02d}'.format(twoMonths) + wirelessFilename + 'FormattedDigitalDomestic.xlsx'),index = False)

print('Wireless File Formatted')

#######################Stream#######################
print('Formatting Streaming file.')
df2 = pandas.read_excel(os.path.join(destinationPath, streamFile))

#df2['retail_price'] = ''
df2['filedate'] = filedate
df2['filename'] = streamFilename

del(df2['FIRST_REL_TITLE'])
del(df2['LABEL_GROUP_CODE'])
del(df2['LABEL_GROUP'])
del(df2['EXTENDED_FAMILY'])
del(df2['ACTIVE_LABEL'])
del(df2['ACTIVE_ADA_LABEL'])
del(df2['PRICE_GRADE'])

upcList = []
for upc in df2['FIRST_REL_UPC']:
	upc = str(upc)
	upcList.append(upc)
cleanUPC = []
for i in upcList:
	upcCleaner = re.sub('E+', '', i)
	cleanUPC.append(upcCleaner)
df2['newUPC'] = cleanUPC
del(df2['FIRST_REL_UPC'])

df2.to_excel(os.path.join(destinationPath, year + '{:02d}'.format(twoMonths) + streamFilename + 'FormattedDigitalDomestic.xlsx'),index = False)

print('Stream File Formatted')

#######################Combine that shit#######################
print('Combining all the files to one Import File.')
# creat an empty dataframe
formattedDF = pandas.DataFrame()

formattedDF = pandas.concat([df, df1, df2], sort=False)

formattedDF.to_excel(os.path.join(destinationPath, year + '-' +'{:02d}'.format(twoMonths) + 'ADADigitalImport.xlsx'),index = False)

print('Formatted and combined.')
totalRows = formattedDF['filedate'].count()
totalRows = str(totalRows)
salesTotal = formattedDF['MONTHLY_TOTAL_SALE'].sum()
salesTotal = str(salesTotal)
print('There are ' + totalRows + ' rows.')
print('Total sales for this month are ' + salesTotal + '.')

print('Now changing column names.')
df = pandas.read_excel(os.path.join(destinationPath, year + '-' +'{:02d}'.format(twoMonths) + 'ADADigitalImport.xlsx'))

df = df.rename(columns = {
                            'LABEL_CODE':'WEA_LABELCODE'
                            ,'MEDIA_CODE':'MEDIA_CD'
                            ,'DSP_NAME':'PROVIDER'
                            ,'PRODUCT_IDENTIFIER':'ROYALTY_PRODUCT_IDENTIFIER'
                            ,'PRODUCT_ID_TYPE_CODE':'ROYALTY_PRODUCT_ID_TYPE_CD'
                            ,'ARTIST':'ARTIST'
                            ,'TITLE':'TITLE'
                            ,'PPD_PRICE':'TOTAL_RETAIL_PRICE'
                            ,'MONTHLY_UNITS':'UNITS'
                            ,'MONTHLY_TOTAL_SALE':'NET_AMOUNT'
                            ,'DISTRIBUTION_MEDIUM_CD':'REPORTED_DISTRIBUTION_MEDIUM'
                            ,'TERRITORY_CD':'INCOME_OWN_DOMESTIC_TERRITORY'
                            ,'LABEL':'LABEL'
                            ,'TRANSACTION_DATE':'salesdate'
                            ,'RETAILER_NAME':'RETAILER'
                            ,'RETAIL_PRICE':'RETAIL_PRICE'
                            ,'filedate':'FileDate'
                            ,'filename':'filename'
                            ,'newUPC':'FIRST_REL_UPC'
                     }
             )                       


df['WEA_LABELCODE'] = df['WEA_LABELCODE'].astype(str)
df['MEDIA_CD'] = df['MEDIA_CD'].astype(str)
df['PROVIDER'] = df['PROVIDER'].astype(str)
df['ROYALTY_PRODUCT_IDENTIFIER'] = df['ROYALTY_PRODUCT_IDENTIFIER'].astype(str)
df['ROYALTY_PRODUCT_ID_TYPE_CD'] = df['ROYALTY_PRODUCT_ID_TYPE_CD'].astype(str)
df['ARTIST'] = df['ARTIST'].astype(str)
df['TITLE'] = df['TITLE'].astype(str)
df['TOTAL_RETAIL_PRICE'] = df['TOTAL_RETAIL_PRICE'].astype(float)
df['UNITS'] = df['UNITS'].astype(float)
df['NET_AMOUNT'] = df['NET_AMOUNT'].astype(float)
df['REPORTED_DISTRIBUTION_MEDIUM'] = df['REPORTED_DISTRIBUTION_MEDIUM'].astype(str)
df['INCOME_OWN_DOMESTIC_TERRITORY'] = df['INCOME_OWN_DOMESTIC_TERRITORY'].astype(str)
df['LABEL'] = df['LABEL'].astype(str)
df['RETAILER'] = df['RETAILER'].astype(str)
df['RETAIL_PRICE'] = df['RETAIL_PRICE'].astype(float)
df['filename'] = df['filename'].astype(str)
df['FIRST_REL_UPC'] = df['FIRST_REL_UPC'].astype(str)


df.to_excel(os.path.join(destinationPath, year + '-' +'{:02d}'.format(twoMonths) + 'ADADigitalImport.xlsx'), index=False)

newTotalRows = df['FileDate'].count()
newTotalRows = str(totalRows)
newSalesTotal = df['NET_AMOUNT'].sum()
newSalesTotal = str(newSalesTotal)
print('There are ' + newTotalRows + ' rows that were confirmed.')
print('Total sales for this month are ' + newSalesTotal + ' that were confirmed.')


print('Ready for import.')

