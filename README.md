# File_Management

#This problem is aimed to provide an automated solution for file management by exploring libraries, data structures, conditional and looping concepts.

#BY USING THIS SCRIPT WE CAN ORGANIZE THE FILES BY FOLLOWING METHODS:
category wise(Docs, Photos, Audio, Videos, etc),
extension wise(.mp3, .mp4, .mkv, etc),
nested folder structure (Year->Month->Week), etc.


STEP 1: IMPORTING MODULES OS AND SHUTIL
        #import os module which provides a protable way of using operating system 
        #import shutil module which helps in automating process of copying and removal of files or directory

STEP 2: CREATING USER DEFINED FUNCTIONS FOR THE ABOVE METHODS 
         for eg: TO ORGANIZE BY FILE CATEGORY MAKE UDF LIKE category()
         
STEP 3:GET PATH INPUTS SOURCE AND DESTINATON
        SOURCE PATH: THE CURRENT FOLDER HAVING 100S OF FILES
        DESTINATION PATH: THE FOLDER IN WHICH WE WANT TO MOVE FILES 
                          ->IF WE WANT TO GET ORGANIZED FILES IN THE SAME FOLDER THEN GIVE THE SAME PATH AS SOURCE PATH
                          
STEP 4: GET CHOICE FROM USER BY WHICH METHOD WANT TO ORGANIZE 
          IF CHOICE == 1 THEN CALL CATEGORY()
          IF CHOICE == 2 THEN CALL EXT()
          
STEP 5: IF ANY ERROR OCCURRED THE EXCEPT BLOCK WILL BE EXECUTED
