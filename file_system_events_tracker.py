import os
import shutil
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class filemovementhandler(FileSystemEventHandler):
    def on_created(self,event):
        time.sleep(1)
        filename=os.path.basename(event.src_path)
        print(f"hey, {filename} has been created ....")
    def on_deleted(self,event):
        time.sleep(1)
        filename=os.path.basename(event.src_path)
        print(f"Oh, {filename} has been deleted ....")
    def on_modified(self,event):
        time.sleep(1)
        filename=os.path.basename(event.src_path)
        print(f"hey, {filename} has been modified ....")
    def on_moved(self,event):
        time.sleep(1)
        filename=os.path.basename(event.src_path)
        print(f"hey, {filename} has been moved ....")

from_dir=input("Enter the location where you wan to add the observer(like C:/User/users/downloads) - ")

eventhandler=filemovementhandler()
# initializing observer
observer=Observer()
# schedule the observer
observer.schedule(eventhandler,from_dir,recursive=True)
# start the observer
observer.start()
try:
    while True:
        time.sleep(10)
        print("Running")
except KeyboardInterrupt:
    print("stopping")
    observer.stop()