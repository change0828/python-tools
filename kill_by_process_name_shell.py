import os
 
def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)
 
# kill_by_process_name_shell("iTunesHelper.exe")