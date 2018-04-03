# EasyDoc
Some code to extract documentation from a .py file and write it to .txt

Gives one .txt file with the documentation of functions and one .txt file with the documentation
of classes and functions of the classes.

Assumes all indents are 4 spaces. 

The .txt files are written in the same directory as the python file


Notes:
Assumes that it is going to be posted to a github wiki and does some formating
Returns a list of functions and the doc in a .txt file. 

There are a few limitiations:
Only functions that are not indented are found. 
Only reads doc witch start and end with ''' (does not read """)
For classes it only looks for functions that are indented once. 


Example:
A file called 'example.py' containing the following two functions and 1 class. 

Use the docsToText function in easyDoc

>>> filename = 'example.py'
>>> docsToText(filename)

Returns: 2 .txt files

exampleFuncDoc.txt
exampleClassDoc.txt


exampleFuncDoc.txt -> Contains

# example functions
**List of functions**
* [pixelsToAngle](#pixelstoanglepixscreendistscreenwscreenxy)<br/>
* [pixelsToAngleWH](#pixelstoanglewhpixscreendistscreenwhscreenxy)<br/>


#### pixelsToAngle(pix,screenDist,screenW,screenXY):

    '''
    Calculate the visual angle on the screen in degrees given a number of 
    pixels. Calculates the distance based on the width of
    the screen. If the pixels are not square, a separate conversion needs
    to be done with the height of the screen.\n
    "pixelsToAngleWH" returns visual degrees for width and height. 
    
    Parameters
    ----------
    pix : float or int
        The pixels to convert in number of pixels
    screenDist : float or int
        Viewing distance in cm
    screenW : float or int
        The width of the screen in cm
    screenXY : tuple, ints
        The resolution of the screen (width - x, height - y), pixels
        
    Returns
    -------
    angle : float
        The angle which spans the given number of pixels, horizontally
    
    Examples
    --------
    >>> deg = pixelsToAngle(55, 75, 47.5, (1920,1080))
    >>> deg
    1.0394522117965745

    '''



#### pixelsToAngleWH(pix,screenDist,screenWH,screenXY):

    '''
    Calculate the visual angle on the screen in degrees given a number of 
    pixels.
    
    Parameters
    ----------
    pix : tuple, floats or ints
        The pixels to convert in nr of pixels. (horizontal, vertical) 
    screenDist : float or int
        Viewing distance in cm
    screenWH : tuple, floats or ints
        The width and height of the screen in cm (width, height)
    screenXY : tuple, ints
        The resolution of the screen (width - x, height - y), pixels
        
    Returns
    -------
    degW : float
        The number of pixels which corresponds to the visual degree in angle,
        horizontally (width)
    degH : float
        The number of pixels which corresponds to the visual degree in angle,
        vertically (height)
    
    Examples
    --------
    >>> degW, degH = pixelsToAngleWH((55, 55), 75, (47.5, 30), (1920,1080))
    >>> degW
    1.0394522117965745
    >> degH
    1.1670958930600797
    
    '''




exampleClassDoc.txt -> Contains

# example classes
**List of Classes and class functions**
* [sendPortCode](#sendportcode)<br/>
    * [sendCode](#selfsendcodeselfcode)<br/>
    * [sendCodeAndReset](#selfsendcodeandresetselfcoderesetinterval0)<br/>
    * [setSettings](#selfsetsettingsselfresetvalue0resetinterval0001port0x378)<br/>




# sendPortCode
### sendPortCode

    '''
    Class for sending port codes:
        Automatically goes to dummy mode if no parallel port

    Requires dlportio.dll !!!

    Never send codes directly after one another, they will be skipped!!
    Wait for the resetInterval + 2ms between codes
    
    Is automatically initiated when using the psychoLink eyetracking class.
    Initiates to: tracker.PPort

    '''



#### self.sendCode(self,code):

    '''
    Set the parallel port code. 
    Prints to console if it is unable to connect with the parallel port
    
    Parameters
    ----------
    code : int, 0-255
        The value to set the parallel port
        
    Examples
    --------
    Initiates and sends code (output is dummy mode)
    >>> PPort = sendPortCode()
    >>> PPort.sendCode(200)
    portCode: 200
    '''



#### self.sendCodeAndReset(self,code,resetInterval=0):

    '''
    Set the parallel port code. Then waits for a set time and then 
    finaly resets the parallelport.
    
    Prints to console if it is unable to connect with the parallel port
    
    Parameters
    ----------
    code : int, 0-255
        The value to set the parallel port
    resetInterval : float or int, positive
        If set to 0, then the resetinterval set in "setSettings" is used.
        If not 0, waits for the given float or int in seconds
    
    Examples
    --------
    Initiates and sends code (output is dummy mode)\n
    Resets the portcode after approx 10ms
    >>> PPort = sendPortCode()
    >>> PPort.sendCodeAndReset(200, 0.01)
    portCode: 200
    portreset: 0
    PortOpen for 9.99999046326ms
    '''



#### self.setSettings(self,resetValue=0,resetInterval=0.001,port=0x378):

    '''
    Sets the settings for sendPort code class
    
    Parameters
    ----------
    resetValue : int: 0-255
        The value to which the parallel port will be reset when using
        "sendCodeAndReset"
    resetInterval : float, positive
        The time to block code execution after setting the parallel port 
        before resetting the parallel port, when using "sendCodeAndReset".
        Time interval is in seconds
    port : hexadecimal
        The parallel port address
    
    Examples
    --------
    Initiate the class and set the resetvalue to 10 and wait time to 
    10ms
    >>> PPort = sendPortCode()
    >>> PPort.setSettings(10, 0.01, 0x378)
    '''







