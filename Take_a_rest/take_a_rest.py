# Take a rest Application
import webbrowser  # To use web browser functionalities.
import time        # To work with system time.
import pymsgbox    # To use Python message box functionality


pymsgbox.alert('The Take a rest application is started! .', 'Alert!')

total_breaks = 2
break_count = 1
# print the program start time
print ("The application was started at ", time.ctime())

# To run the program in loop
while (break_count <= total_breaks):
    time.sleep(60) # will sleep for given sec 60 = 1min
    #open the default browser and then open a new tab and run the given link
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=F1ZT8XyxyH4")
    # to print each break time
    print ("The break-", break_count ,"was started at", time.ctime())
    break_count += 1
