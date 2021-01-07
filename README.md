# Developing A New Plugin
You can start by creating a copy of this example plugin, and use it as a scaffold for your development.  
To develop a new tool, create a .py file under the appropriate tool subdirectory (detectors, modifiers, ect).  
There are examples of each tool type in this project under the appropriate directory.  
Make sure your tool extends the appropriate parent, and has both an `__init__` method and the appropriate execution method:
- `run` for filters and modifiers
- `execute` for enhancers
- `detect_start` and `detect_end` for detectors.

Any parameters your tool requires should be listed in the inputs property in addition to your `__init__` method.
Once you've finished creating your tool's file, import it in `__main__.py` and register it under the correct category in the library class.  
When you've created and registered all of your plugin's tools, zip up the plugin directory, and upload to the ROA application using the "upload plugin" button in the dashboard under Onboarding > Plugins.