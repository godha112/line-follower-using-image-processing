# line-follower-using-image-processing
Line following robot using image processing


Usually image processing uses sensors such as IR sensors  to detect the lines. But in this project I have used image processing in live video feed to detect lines. 
From the picamera attched to the raspberry pi,  video is accessed divided into frames and  converted into an image to perform analysis. Firstly the RGB image is converetd 
into a greyscale image for easy processing and guassian filter is applied to reduce noise. Then the image is threholded to form a binary image and  the image is elated 
and dilated to further reduce noise and sharply detect the line. Then contour and contour area is used to detect the line. Upon detectionof contours the bot is made to
move according to the change in contours. Rpi is used as microcontroller for both image processing and also for providing actuation to the bot. 
Programming language used is python.
