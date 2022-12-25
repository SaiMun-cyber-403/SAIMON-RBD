import os,re,sys,platform
os.system('git pull')



bit = platform.architecture()[0]
if bit == '64bit':
    from saimon import ud
    ud()
elif bit == '32bit':
    from saimon import ud
    ud()