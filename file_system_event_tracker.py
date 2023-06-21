import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/ANSH/Downloads"

# Event handler class
class FileEventHandler(FileSystemEventHandler) :
    def on_created(self, event):
        print(f"Hey, {event.src_path}has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

# Initialize File Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

#Schedule The Observer 
observer.schedule(event_handler, from_dir, recursive=True)

# Start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()