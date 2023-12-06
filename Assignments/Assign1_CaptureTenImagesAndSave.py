#import cv2 library
import cv2, time

# Open Web Cam
capture = cv2.VideoCapture(0)

# Itrate 11 times
for i in range(11):
    res, frame = capture.read() 

    # show live camera on screen
    cv2.imshow('liveCapture', frame)

    # This condition is to ignore first frame
    # bcz of dark frame
    if i == 0:
        continue

    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

    # Saving images
    saving_img = cv2.imwrite(f"capture_{i}.png", frame)
    if saving_img:
        print(f"capture_{i}.png is Saved Seccuessfully")
    else:
        print(f"Unable to save capture_{i}.png")

    # delay of one second
    time.sleep(1)

capture.release()
cv2.destroyAllWindows()
