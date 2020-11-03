import os
import time

f = open('date.txt', 'wb')
details = time.strftime('%d %B %Y, %H:%M:%S')
f.write(details.encode('utf-8', 'ignore'))
f.close()
print (details)
os.system('git add .')
os.system("git commit -am 'auto-commit'")
time.sleep(5)
os.system('git push origin master')