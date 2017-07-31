# This software records the mouse position and button click information

import pythoncom
import pyHook
import wx
import thread
import time


def MouseHook(threadName):
    # Start the com, loop forever
    pythoncom.PumpMessages()

def FrequencyControl(threadName):
    # determine the recording frequency
    while True:
        time.sleep(0.02) # 50 Hz
        global log_flag
        log_flag = True

def OnButtonClick(event):
    # set the toggle button activity
    if Button.GetValue():
        Button.SetLabel('End')
        hm.HookMouse()
    else:
        Button.SetLabel('Start')
        hm.UnhookMouse()

def OnMouseButtons(event):
    # called when mouse button events are received
    # print 'MessageName:', event.MessageName, 'Message:', event.Message
    # print 'Time:', event.Time
    # print 'WindowName:', event.WindowName, 'Window:', event.Window
    # print 'Position:', event.Position, 'Wheel:', event.Wheel
    # print '---'
    global time_stamp, current_time
    current_time = time.time()
    if event.Message == 513:
        file_object.write("{:.3f}".format(current_time - time_stamp) + " " + str(event.Position[0]) + " " + str(
            event.Position[1]) + " " + "1 \n")
        print "{:.3f}".format(current_time - time_stamp), event.Position[0], event.Position[1], 1
    if event.Message == 514:
        file_object.write("{:.3f}".format(current_time - time_stamp) + " " + str(event.Position[0]) + " " + str(
            event.Position[1]) + " " + "2 \n")
        print "{:.3f}".format(current_time - time_stamp), event.Position[0], event.Position[1], 2
    if event.Message == 516:
        file_object.write("{:.3f}".format(current_time - time_stamp) + " " + str(event.Position[0]) + " " + str(
            event.Position[1]) + " " + "3 \n")
        print "{:.3f}".format(current_time - time_stamp), event.Position[0], event.Position[1], 3
    if event.Message == 517:
        file_object.write("{:.3f}".format(current_time - time_stamp) + " " + str(event.Position[0]) + " " + str(
            event.Position[1]) + " " + "4 \n")
        print "{:.3f}".format(current_time - time_stamp), event.Position[0], event.Position[1], 4
    time_stamp = current_time
    return True

def OnMouseMove(event):
    # called when mouse move events are received
    global log_flag, time_stamp, current_time
    if log_flag:
        current_time = time.time()
        file_object.write("{:.3f}".format(current_time - time_stamp)+" "+str(event.Position[0])+" "+str(event.Position[1])+" "+"0 \n")
        print "{:.3f}".format(current_time - time_stamp), event.Position[0], event.Position[1], 0
        log_flag = False
        time_stamp = current_time
    # return True to pass the event to other handlers
    return True


# Global variables
log_flag = False
launch_time = time.time()
time_stamp = launch_time  # last time stamp
current_time = launch_time

# Open a file
file_object = open("data/log_"+str(int(launch_time))+".txt", "w")
file_object.write("# Message code: 0 - Mouse move, 1 - Left button down\n# 2 - Left button up, 3 - Right button down, 4 - Right button up\n#\n")
file_object.write("#("+str(launch_time)+") "+time.asctime(time.localtime(launch_time))+"\n")
file_object.write("#Time #X_pos #Y_pos #Message\n")
print "# Message code: 0 - Mouse move, 1 - Left button down\n# 2 - Left button up, 3 - Right button down, 4 - Right button up\n"
print "#("+str(launch_time)+") "+time.asctime(time.localtime(launch_time))
print "#Time #X_pos #Y_pos #Message"

# Create a hook manager
hm = pyHook.HookManager()
# watch for  mouse events
hm.MouseAllButtons = OnMouseButtons
hm.MouseMove = OnMouseMove

# Start the thread for mouse hook
thread.start_new_thread(MouseHook, ("",))
# Start the thread to control the frequency of logging
thread.start_new_thread(FrequencyControl, ("",))

# Create the GUI
app = wx.App()
window = wx.Frame(None, size=(170, 90), title="",
                  style=wx.BORDER_RAISED | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
panel = wx.Panel(window)
# Create two buttons
Button = wx.ToggleButton(panel, label='Start', pos=(21, 6), size=(120, 50))
# Bind the buttons to functions
Button.Bind(wx.EVT_TOGGLEBUTTON, OnButtonClick)
# Show the GUI
window.Show(True)
app.MainLoop()

