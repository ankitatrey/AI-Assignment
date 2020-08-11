import cv2

#creating a video capture object using the the default webcam.
video = cv2.VideoCapture(0)  

#using CascadeClassifier method to provide the program with the face features.
facecas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#a is a variable used to count the number of frame recorded.
a = 0
while True:
    a += 1

    #here check & frame are the two objects returned by the video
    #capture object. check returns 'TRUE' IF video was successfully 
    #otherwise return FALSE. AND frame is the recorded image by the webcam.
    check ,frame = video.read()
    

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detectMultiScale is the method used to search face co-ordinates
    faces = facecas.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    #draw the rectangle across the face in the frame
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,230,0), 3)

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1) 
    if key == ord('q'):
        break

print(a)  #print the number of frames captured.

video.release()  #release the video object.
cv2.destroyAllWindows()
