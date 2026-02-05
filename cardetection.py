import cv2
import imutils  # To Resize

# Path to the Cascade Classifier XML (fixed path issues)
cascade_src = r'C:\Users\padma\OneDrive\Documents\cars.xml'  # Use raw string to avoid escape issues

# Load the Cascade Classifier
car_cascade = cv2.CascadeClassifier(cascade_src)

# Check if the classifier was loaded correctly
if car_cascade.empty():
    print("Error: Cascade file not loaded. Make sure the path to 'cars.xml' is correct.")
    exit()

# Set up the camera (try changing the index if the wrong camera is selected)
cam = cv2.VideoCapture(0)  # Use 0 if 1 doesn't work

# Check if the camera is opened
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read frame from the camera
    _, img = cam.read()
    
    # Ensure the frame was captured correctly
    if not _:
        print("Error: Could not read frame.")
        break

    # Resize the image to a manageable width (keeping the aspect ratio)
    img = imutils.resize(img, width=1000)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect cars in the image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the result in a window
    cv2.imshow("Frame", img)

    # Get the number of detected cars
    n = len(cars)
    print("----------------------------------------------------------")
    print("North:%d" % (n))

    # Traffic control based on the number of cars detected
    if n >= 8:
        print("North More Traffic, Please on the RED Signal")
    else:
        print("No traffic")

    # Wait for the ESC key (27) to break the loop
    if cv2.waitKey(33) == 27:
        break

# Release the camera and close the OpenCV window
cam.release()
cv2.destroyAllWindows()
