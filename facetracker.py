import cv2
import threading

# Initialize the face detection classifier
face_cap = cv2.CascadeClassifier("C:/Users/jangr/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

# Global variable to control the loop
running = True

def listen_for_exit():
    global running
    while running:
        user_input = input()  # This listens for terminal input
        if user_input.lower() == "exit":  # If 'exit' is typed, stop the loop
            running = False

# Start the terminal input listening in a separate thread
input_thread = threading.Thread(target=listen_for_exit)
input_thread.start()

# Main loop for capturing and displaying the video feed
while running:
    ret, video_data = video_cap.read()
    if not ret:
        break

    # Convert image to RGB
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)

    # Detect faces in the video frame
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the video feed
    cv2.imshow('Video Live', video_data)

    # Check if 'exit' command was given or if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close OpenCV windows
video_cap.release()
cv2.destroyAllWindows()
