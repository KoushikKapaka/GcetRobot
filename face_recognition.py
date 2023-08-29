
import face_recognition
import cv2
import numpy as np
#import pyttsx3
import pickle
import time
import serial

arduino = serial.Serial(
port = '/dev/ttyACM0',
baudrate = 9600,
bytesize = serial.EIGHTBITS, 
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE, 
timeout = 5,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2
)

video_capture = cv2.VideoCapture(0)

# Load a second sample picture and learn how to recognize it.
#engine = pyttsx3.init()

# Create arrays of known face encodings and their names
known_face_encodings =[]
known_face_names = []

#loading the data from the pickle file 
dbfile = open('/home/bot/Desktop/practice.py/data_pickle', 'rb')	
db = pickle.load(dbfile)
#db is the data base with known names and encodings

known_face_encodings=db['data']['encoding']
known_face_names=db['data']['names']
#print(known_face_encodings)
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
l=[False]*len(known_face_names)
#print(known_face_names)
#time.sleep(10)
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame=cv2.flip(frame,1)
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s
            #print(face_encoding.shape)
            #face_encoding=face_encoding.reshape(128,)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
            name = "Unknown"
            # print(matches)

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                #print(min(face_distances),best_match_index)
                name = known_face_names[best_match_index]
            
            
            face_names.append(name)
		

    process_this_frame = not process_this_frame

    
    # Display the results
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 255), 1)
        if(name=="Unknown"):
        #     time.sleep(10)
              arduino.write("ANGRY".encode('utf-8'))
        #     print("who are you?")
        #     s=input()
        #     name=s
        #     known_face_encodings.append(face_encoding)
        #     known_face_names.append(s)
        #     l.append(False)
        #     face_names.pop()
        #     face_names.append(name)
        # else:
        #     arduino.write("something".encode('utf-8'))
        # if(not l[known_face_names.index(name)]):
        #     #engine.say("Hello ")
        #     print(name)
        #     l[known_face_names.index(name)]=True
            
        #     # engine.runAndWait()

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        data = {'names' : known_face_names,"encoding":known_face_encodings}
        db = {}
        db['data']=data
        dbfile = open('/home/bot/Desktop/practice.py/data_pickle', 'wb')
        pickle.dump(db,dbfile)
        dbfile.close()        
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
