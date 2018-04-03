# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 11:20:59 2018

@author: User1
"""
import numpy as np
import time
from psychopy import core

def pixelsToAngle(pix, screenDist, screenW, screenXY):
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
    pixSize     = screenW / float(screenXY[0])
    cmOnScreen  = (pix/2.0) * pixSize
    angle       = np.rad2deg(np.arctan(cmOnScreen / screenDist))*2.0

    return angle

def pixelsToAngleWH(pix, screenDist, screenWH, screenXY):
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
    pixSizeW = screenWH[0] / float(screenXY[0])
    pixSizeH = screenWH[1] / float(screenXY[1])
    cmOnScreenW = (pix[0]/2.0) * pixSizeW
    cmOnScreenH = (pix[1]/2.0) * pixSizeH
    angleW = np.rad2deg(np.arctan(cmOnScreenW / screenDist))*2.0
    angleH = np.rad2deg(np.arctan(cmOnScreenH / screenDist))*2.0
                       
    return angleW, angleH



class sendPortCode():
    '''
    Class for sending port codes:
        Automatically goes to dummy mode if no parallel port

    Requires dlportio.dll !!!

    Never send codes directly after one another, they will be skipped!!
    Wait for the resetInterval + 2ms between codes
    
    Is automatically initiated when using the psychoLink eyetracking class.
    Initiates to: tracker.PPort

    '''
    def __init__(self):
        self.setSettings()
        try:
            from ctypes import windll
            self.io             = windll.dlportio
            self.dummy          = False
            print '\nThe parallel port was initiated!'
            print 'Sending port codes!\n'
        except:
            print '\nThe parallel port couldn\'t be opened'
            print 'Set to dummy mode!\n'
            self.dummy          = True
            self.io             = False

    def setSettings(self, resetValue=0, resetInterval = 0.001, port = 0x378):
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
        self.resetValue     = resetValue
        self.resetInterval  = resetInterval
        self.port           = port
        
    def sendCodeAndReset(self, code, resetInterval = 0):
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
        if resetInterval == 0:
            waitTime = self.resetInterval
        else:
            waitTime = resetInterval
        if code != self.resetValue:
            # Send port to console
            if self.dummy == True:
                print 'portCode: ' + str(code)
                portSend = time.time()
                core.wait(waitTime, hogCPUperiod=waitTime)
                portReset = time.time()
                print 'portreset: ' + str(self.resetValue)
                print 'PortOpen for ' + str((portReset - portSend)*1000) + 'ms'

            # Actually send port codes
            elif self.dummy == False:
                # Send port code
                try:
                    self.io.DlPortWritePortUchar(self.port, int(code))
                except:
                    print 'Failed to send trigger!'
                # wait for a set time
                core.wait(waitTime, hogCPUperiod=waitTime)
                # Reset the port
                try:
                    self.io.DlPortWritePortUchar(self.port, int(self.resetValue))
                except:
                    print 'Failed to reset trigger!'

    def sendCode(self, code):
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
        # Send port to console
        if self.dummy == True:
            print 'portCode: ' + str(int(code))

        # Actually send port codes
        elif self.dummy == False:
            # Send port code
            try:
                self.io.DlPortWritePortUchar(self.port, int(code))
            except:
                print 'Failed to send trigger!'