#!/usr/bin/env python3
"""MDalavai | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

import shutil
import os

def main():

   # move into the working directory. -- It's like using 'cd ~/mycode/5g_research/'
   os.chdir("/home/student/mycode/")


   # copy the file a to b -- It's like using 'cp filea fileb'
   shutil.copy("5g_research/sdn_network.txt","5g_research/sdn_network.txt.copy")

   # copy the entire directoryA to directoryB
   os.system("rm -rf /home/student/mycode/5g_research_backup/")
   shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
