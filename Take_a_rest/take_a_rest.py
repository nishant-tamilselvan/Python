# Take a rest Application
import webbrowser  # To use web browser functionalities.
import time        # To work with system time.

while true:
    time.sleep(60) # will sleep for given sec 60 = 1min
    #open the default browser and then open a new tab and run the given link
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=F1ZT8XyxyH4")
