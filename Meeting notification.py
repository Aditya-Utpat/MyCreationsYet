import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom
from datetime import datetime
import time
from os import system
app = 'C:\\Users\\aditya\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe'
day = datetime.now().strftime('%w')
file = open('week.txt').read()
if file == 'ab':
    meet = '"E:\\2. ADITYA\\Google Meet - Saroj maam.lnk"'
elif file == 'cd':
    meet = '"E:\\2. ADITYA\\Google meet Manjusha Maam.lnk"'
else:
    quit()
if day == '1':
    day = 'Monday'
elif day == '2':
    day= 'Tuesday'
elif day == '3':
    day = 'Wednesday'
#create notifier
nManager = notifications.ToastNotificationManager
notifier = nManager.create_toast_notifier(app)

#define your notification as string
tString = """
  <toast>
    <visual>
      <binding template='ToastGeneric'>
        <text>Scholarship Class</text>
        <text>"""+day+""" Class</text>
        <text>Meet will start in 5 seconds.</text>
      </binding>
    </visual>
    <actions>
      <action
        content="Okay"
        arguments="action="/>
    </actions>
  </toast>
"""

#convert notification to an XmlDocument
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)

#display notification
notifier.show(notifications.ToastNotification(xDoc))
time.sleep(5)
system(meet)
