#! python3
# ADADownload.py - downloads ADA files from the web

import datetime, calendar, time, os, shutil
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

print('Finished')
