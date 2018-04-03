# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:49:22 2018

@author: User1
"""
from collections import OrderedDict
import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def docsToDicts(filename):
    with open(filename) as l:
        lines = l.readlines()
            
    # search strings
    tab = '    '
    docS = "'''"
    
    # Class info
    classes = OrderedDict()
    className = ''
    
    # Function info
    funcs =  OrderedDict()
    funcName = ''
    
    # Flags
    inClass = False
    inFunc = False
    inClassFunc = False
    sIdx = 0
    
    for idx, l in enumerate(lines):
        if not inClass and not inFunc and not inClassFunc:
            if 'class' in l[0:5]:
                if docS in lines[idx+1]:
                    splitClass = l.split()[1]
                    className = splitClass[:splitClass.find('(')]
                    classes[className] = [[]]
                    inClass = True
                    sIdx = idx+1
    
            if 'def ' in l[:4]:
                if docS in lines[idx+1]:
                    splitFunc = l.split()[1:]
                    funcName = ''.join(splitFunc)
                    funcs[funcName] = []
                    inFunc = True
                    sIdx = idx+1
            
            if 'def ' in l[len(tab):len(tab)+4]:

                splitFunc = l.split()[1:]
                funcName = ''.join(splitFunc)
                if '__' not in funcName and docS in lines[idx+1]:
                    funcName = funcName
                    classes[classes.keys()[-1]].append([])
                    classes[classes.keys()[-1]][-1].append(funcName)
                    inClassFunc = True
                    sIdx = idx+1
                
        else:
            if inClass:
                classes[className][0].append(l)
                if docS in l and idx != sIdx:
                    className = '' 
                    inClass = False
            if inFunc:
                funcs[funcName].append(l)
                if docS in l and idx != sIdx:
                    inFunc = False
                    funcName = ''
            if inClassFunc:
                classes[classes.keys()[-1]][-1].append(l[4:])
                if docS in l and idx != sIdx:
                    inClassFunc = False
                    funcName = ''
            
    return funcs, classes

def writeFuncDoc(funcs, fileName):
    moduleName = path_leaf(fileName)[:-3]
    outName = fileName[:-3]+'FuncDoc.txt'
    with open(outName, 'w') as f:
        exclude = '.( )=:,[]'
        f.write('# '+moduleName+' functions\n')
        f.write('**List of functions**\n')   
        funcListName = sorted(funcs.keys())
        for funcName in funcListName:
            func = funcName[:funcName.find('(')]
            line = '* ['+func+'](#'
            fLink = funcName.lower()
            fLink = ''.join( c for c in fLink if  c not in exclude)
            line += fLink + ')<br/>\n'
            f.write(line)
            
        f.write('\n\n')
        for funcName in funcListName:
            funcDoc = funcs[funcName]
            f.write('#### '+funcName+'\n\n')
            for doc in funcDoc:
                f.write(doc)
            f.write('\n\n\n')

def writeClassDoc(classes, fileName):
    moduleName = path_leaf(fileName)[:-3]
    outName = fileName[:-3]+'ClassDoc.txt'
    with open(outName, 'w') as f:
        exclude = ".( )=:,[]'"
        f.write('# '+moduleName+' classes\n')
        f.write('**List of Classes and class functions**\n')  
        classNames = sorted(classes.keys())
        for className in classNames:
            classDoc =  classes[className]
            if className.find('(') > -1:
                classN = className[:className.find('(')]
            else:
                classN = className
            line = '* ['+classN+'](#'
            cLink = classN.lower()
            cLink = ''.join( c for c in cLink if  c not in exclude)
            line += cLink + ')<br/>\n'
            f.write(line)
            
            # If functions in the classes with documentation
            if len(classDoc) > 1:
                subFuncsDoc = sorted(classDoc[1:])
                for subFunc in subFuncsDoc:
                    subFuncN = subFunc[0]
                    classN = subFuncN[:subFuncN.find('(')]
                    line = '    * ['+classN+'](#'
                    subFuncN = subFuncN.lower()
                    subFuncN = ''.join( c for c in subFuncN if  c not in exclude)
                    line += 'self'+subFuncN + ')<br/>\n'
                    f.write(line)   
                    
        f.write('\n\n')
        for className in classNames:
            classDoc =  classes[className]    
            # Write the main class doc
            f.write('\n\n# '+ className+'\n')
            f.write('### '+className+'\n\n')
            for doc in classDoc[0]:
                f.write(doc)
            f.write('\n\n\n')
            # If we functions in the classes with documentation
            if len(classDoc) > 1:
                subFuncsDoc = sorted(classDoc[1:])
                for subFunc in subFuncsDoc:
                    subFuncName = 'self.'+subFunc[0]
                    subFuncDoc = subFunc[1:]
                    f.write('#### '+subFuncName+'\n\n')
                    for doc in subFuncDoc:
                        f.write(doc)
                    f.write('\n\n\n')
                    
def docsToText(fileName):
    funcDoc, classDoc = docsToDicts(fileName)
    writeFuncDoc(funcDoc, fileName)
    writeClassDoc(classDoc, fileName)

fileName = 'example.py'
docsToText(fileName)
















