""" 
-----------------------------
  CODE FOR PURGING FOLDERS
  [CWHQ] 
-----------------------------
"""


import os
import shutil

all_projects = os.listdir("/mnt/student")
print(all_projects)

for project in all_projects:
    if os.path.isdir(project):
        shutil.rmtree(project)
