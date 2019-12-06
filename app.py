from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#pipenv or pip3 install watchdog first in order for it to work 

import os
import json
import time


class CurrentHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = 'Place the path on current forlder of the files you want to move'
folder_destination = 'Destination folder for the move files'
event_handler = CurrentHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
