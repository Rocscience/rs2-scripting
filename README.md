## Introduction 
This repo contains the reference manual for the rs2 scripting library. The rs2 scripting library is used to interact with the RS2 application through python.   

Release notes for the library are kept here:
https://www.rocscience.com/support/rs2/release-notes

Corresponding RS2 version can be downloaded here:
https://downloads.rocscience.com/RS2/rs211026f11s.zip

The library itself is hosted on PyPi here:
https://pypi.org/project/RS2Scripting/11.26.0/

### Goal
Each function exposed corresponds to an equivalent operation you could have done through the UI.  
Using this idea, the user should be able to edit models and get results without having to go through the UI at all.
Although only a limited set of functionality is exposed for now, some basic workflows should still be possible. For a list of the functionality we have so far, see [Exposed Functionality](#exposed-functionality).

### Python UI equivalents
Events and workflows done in the UI will have equivalents in the python library.  
Wherever a dialog is shown in the UI, there will be an equivalent class with methods that mimick the dialog's behavior.  
Wherever a warning or error dialog is displayed, an exception will be thrown, or a warning will be displayed in python instead.  
Wherever you can select and manipulate an entity, identifiers can be used in the library to get references to those entities in python and objects will be constructed to help you interface with them.  

### How it works
Each function in the library is a wrapper to make an api call to the Application.  
Objects retrieved through function calls will often not contain any data themselves, but will instead be proxies, allowing you to get information from the objects in the application.  
For this reason, debugging will sometimes be tricky, as not all data will always be available for you to inspect unless you get it and assign it to a variable yourself.  

### Warnings
References can be *invalidated* whenever the corresponding object in the application is destroyed or reloaded. You will need to watch out for expired referenecs and renew them when needed as it can cause crashes or incorrect results if not managed properly. Functions that invalidate objects will always be marked with a warning and will indicate which objects should be re-loaded. 

## Exposed Functionality
The current set of functionality exposed is limited. With this version of the library, you can:  
- Manage files through Open, Close, Save and Compute
- Modfy any Property value and stage factor, except for some user defined materials and statistical properties.
- Get any Mesh result, support result, SSR Critical SRF and query result.
- Add and remove queries (material, history, time)
  
## Getting Started

**Getting started guide**  
https://www.rocscience.com/help/rs2/tutorials/scripting/getting-started-with-rs2-python-scripting  
**First Tutorial**  
https://www.rocscience.com/help/rs2/tutorials/scripting/anchored-sheet-pile-wall
