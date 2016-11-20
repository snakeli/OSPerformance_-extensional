# !/usr/bin/python
# -*-coding:utf-8-*-
import os
import time
import optparse

os_modules = ["applaunch", "appmemory", "boottime", "diskusage", "heavymemory", "idlememory", "jankiness", "platformbenchmark"]
module_folder = {"applaunch": "aosapplaunchprofile",
                 "appmemory": "aosappmemoryprofile",
                 "boottime": "aosboottimeprofile",
                 "diskusage": "aosdiskusageprofile",
                 "heavymemory": "aosheavymemprofile",
                 "idlememory": "aosidlememoryprofile",
                 "jankiness": "aosjankinessprofile",
                 "platformbenchmark": "aosplatformbenchmark"}

# get it from command line
optparser = optparse.OptionParser(usage="%prog [options] <devicei_d>")
optparser.add_option("-d", "--device_id", action="store", type="string", dest="device_id", default="", help="device id get it by running 'adb devices'")
optparser.add_option("--module", action="store", type="string", dest="module", default="", help="Test Module: applaunch,appmemory,boottime,diskusage,heavymemory,idlememory,jankiness,platformbenchmark")
(Options, args) = optparser.parse_args()
device_id = Options.device_id

modules = []
for tmp in Options.module.split(','):
    if tmp in os_modules:
        modules.append(tmp)
print "test_module: "
print modules

rootDir = os.path.split(os.path.realpath(__file__))[0] + os.sep
file_name = device_id + "_" + time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
target_file = rootDir + file_name

if not os.path.exists(target_file):
    try:
        os.mkdir(target_file)
    except Exception, ex:
        print "failed to create target directory, " + ex

logDir = rootDir + file_name + os.sep
print "Start test !"
for test_module in modules:
    print "Current Test Module: " + test_module
    script_name = module_folder[test_module]
    script_file = rootDir + script_name + os.sep + script_name + ".py"
    os.system('python %s -d %s -m 1 > %s' % (script_file, device_id, logDir+test_module))
    print "Finish %s test" % test_module
    time.sleep(60)







