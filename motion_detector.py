import cv2, time, pandas
from datetime import datetime   # import datetime class from datetime library...


first_frame=None # == nothing...prevents from getting 'variable not defined error...'
# a list of statuses of when motion is detected...0 for no motion detected and 1 for when motion is detected...
status_list=[None,None]
times=[]
# a dataframe object for logging times an object entered detection area...
df=pandas.DataFrame(columns=["Start","End"])

# method that triggers a video capture object...the camera in this case...
video=cv2.VideoCapture(0) # numbers are for cameras...0 is for internal cam...you can pass video too like "movie.mp4"...

while True:
    check, frame = video.read()
    status=0 # to keep track of when an object enters the frame or not...(the object being motion detected)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                               # parameters of the bluriness (notice its a tuple)--->(21,21),0) plus the parameter for standard deviation....
    gray=cv2.GaussianBlur(gray,(21,21),0) # increases the accuracy by exaggerating the differences, and removing noise as well, when comparing the difference
    #between the first_frame and the delta frame (proceeding frames)...
    # in order to detect motion in the proceeding frames...

    if first_frame is None:
        first_frame=gray
        continue # continue to the beginning of the loop again...from this point...
        # thus neverminding the code below...
    # delta_frame is the object being detected, coming into focus...
    delta_frame=cv2.absdiff(first_frame,gray) # comparing difference between firstframe and current frame...this results in yet another image...
                    # threshold() returns a tuple with two values...first value at index[0] is needed when using other threshold methods...
                    # the first item of the tuple suggests a value for the threhold...like 30 etc... for THRESH_BINARY method you just need the 2nd item of the tuple...
                    # which is the actual frame that is returned...delta_frame in this case...
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]   # threshold of 30 and color 255 or white to denote a motion detected object in focus...
                                                # number of iterations through the image to remove the black holes...the more iterations the smoother the image will be...
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) # no kernel array being used so we pass the None value as 2nd parameter...

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # use the copy of the thresh_frame so you don't modify the original thresh_frame object...
                                                    # cv2.RETR_EXTERNAL: this method draws the external contours of the objects you will be finding in the image...
                                                    # cv2.CHAIN_APPROX_SIMPLE: method cv2 will apply for retrieving the contours...

    for contour in cnts: # variable of contours (cnts)
        if cv2.contourArea(contour) < 10000: # if less than 10000 pixels...100x100 pixels window... (10,000 pixels)
            continue                            # greater than 10,000 pixels denotes an object has been detected thus change status to status=1
        status=1 # to keep track of when an object enters the frame or not...(the object being motion detected) status=1 denotes object has been detected...


        # code below draws a rectangle...
        (x, y, w, h)=cv2.boundingRect(contour) # if area of contour is greater or equal to 1000 pixels draw a rectangle onto the current frame...
        #             passing the color frame...  color of rectangle is (green), 3 for the width...
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3) # coordinates of the rectangle... upper left and lower right... drawing a rectangle on the color frame based on the
        # contours computed...

    # a list of statuses of when motion is detected...0 for no motion detected and 1 for when motion is detected...
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:    # object entered detection...     # check last two entries with [-1] and [-2]
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:    # when object stepped out of detection...ss
        times.append(datetime.now())

    # wait before turning off camera..
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Fr    ame",frame)

    #cv2.imshow("Capturing Marty",frame)
    key=cv2.waitKey(1) # if you pass 0, then any key pressed will stop the while loop or the script...
    #print("Gray Frame pixel data: below...")
    #print(gray)
    #print("Delta Frame pixel data: below...")
    #print(delta_frame)

    if key==ord('q'):
        if status==1:
            print(str(times.append(datetime.now())) + "Last time stamp fired...")
        print("Q was pressed...program stopped...")
        break
    #print(status)
print(status_list)
print(times)
                                 # 2 per iteration of the forloop...
for i in range(0, len(times),2): # use 2 because there is start and end times which will go in one row...hence the number 2 for two pieces of data in one row...
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)


df.to_csv("Times.csv")
# releases the camera...mes
video.release()
cv2.destroyAllWindows