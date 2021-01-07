# Developing A New Plugin
You can start by creating a copy of this example plugin, and use it as a scaffold for your development.  
Start developing a new tool by creating a .py file under the appropriate tool subdirectory (detectors, modifiers, ect).  
There are examples of each tool type in this project under the appropriate directory. Make sure your tool extends the appropriate parent, and has both an \_\_init\_\_ method and the appropriate execution method (run for filters and modifiers, execute for enhancers, and detect_start and detect_end for detectors).  
Any parameters your plugin requires should be listed in the inputs property in addition to your \_\_init\_\_ method.
Once you've finished creating your tool's file, import it in \_\_main\_\_.py and register it under the correct category in the library class.  
Zip up your newly created plugin, and upload to the ROA application using the "upload plugin" in the dashboard under Onboarding > Plugins.