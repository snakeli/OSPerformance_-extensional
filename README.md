# OSPerformance_-extensional
For extending OS Performance test  
Move all the scripts to AOStargets directory 

# SendEmail.py
For monitoring test status and send Email  
You should modify the email_credentials.cfg obey to your own email account

# StartTest.py
For connect all the the test scripts  
Options:  
  -h, --help            				show this help message and exit  
  -d DEVICE_ID, --device_id=DEVICE_ID	device id get it by running 'adb devices'  
  --module=MODULE       				Test Module: applaunch,appmemory,boottime,diskusage,heavymemory,idlememory,jankiness,platformbenchmark
  
