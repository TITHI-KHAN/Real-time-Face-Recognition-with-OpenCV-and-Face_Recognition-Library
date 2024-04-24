# Real-time Face Recognition with OpenCV and Face_Recognition Library

## To run the code, please either use "Visual Studio" or "Jupyter Notebook from Anaconda Navigator".

### Thank you.

<br>

## Code Explanation:

1. **Importing Libraries**: The code starts by importing the necessary libraries: `cv2` for OpenCV, `face_recognition` for face recognition tasks, and `numpy` for numerical operations.

2. **Initializing Variables**: Two lists `known_face_encodings` and `known_face_names` are initialized. These will store the face encodings and corresponding names of the people whose faces we want to recognize.

3. **Loading Sample Pictures**: Sample images of known persons are loaded using `face_recognition.load_image_file()`. Their face encodings are calculated using `face_recognition.face_encodings()` and stored in variables like `person_1_face_encoding`, `person_2_face_encoding`, etc.

4. **Setting Up Video Capture**: OpenCV's `VideoCapture()` is used to capture video from the default camera (index 0). The capture is stored in `video_capture`.

5. **Processing Frames in a Loop**: The code enters a while loop to continuously capture frames from the video feed.

6. **Resizing Frames**: Each frame is resized to 1/4 of its original size to speed up face detection using `cv2.resize()`.

7. **Converting Color Format**: The color format of the resized frame is converted from BGR to RGB using NumPy slicing (`rgb_small_frame = small_frame[:, :, ::-1]`) as `face_recognition` library expects RGB format.

8. **Face Detection and Recognition**: Inside the loop, face locations are detected using `face_recognition.face_locations()` and face encodings using `face_recognition.face_encodings()`. Then, for each face detected, the code compares its encoding with the known face encodings and assigns a name accordingly.

9. **Drawing Boxes and Labels**: Detected faces are boxed and labeled with names on the original frame using OpenCV's drawing functions (`cv2.rectangle()` and `cv2.putText()`).

10. **Displaying the Result**: The processed frame with boxes and labels is displayed using `cv2.imshow()`.

11. **Quitting the Program**: The program exits the loop if the 'q' key is pressed. It releases the video capture and destroys all OpenCV windows.

## Some key points about the provided code:

1. **Face Detection**: The code utilizes the `face_recognition` library to detect faces in real-time video frames. This is done using the `face_recognition.face_locations()` function, which returns the coordinates of bounding boxes around detected faces.

2. **Face Encoding**: After detecting faces, the code extracts facial features and encodes them into a numerical representation using the `face_recognition.face_encodings()` function. This encoding is unique to each face and is used for comparison during recognition.

3. **Face Recognition**: The encoded face features are compared against a database of known face encodings (`known_face_encodings`) using the `face_recognition.compare_faces()` function. This determines whether a detected face matches any of the known faces.

4. **Labeling Detected Faces**: Once a match is found, the corresponding name is retrieved from the `known_face_names` list and displayed alongside the detected face using OpenCV's drawing functions (`cv2.rectangle()` and `cv2.putText()`).

5. **Real-time Processing**: The code continuously captures frames from the video feed in a loop and processes each frame for face detection and recognition. This allows for real-time face recognition in a live video stream.

6. **User Interaction**: The program allows the user to quit the application by pressing the 'q' key, which releases the video capture and closes all OpenCV windows.

7. **Efficient Processing**: To improve performance, the frames are resized to a smaller size before face detection and recognition. This reduces computational load while still maintaining accuracy in face recognition.

8. **Modularity**: The code is modular, making it easy to add more known faces by loading additional images and encoding their faces. This allows for scalability in recognizing multiple individuals.

Overall, this code provides a basic framework for real-time face recognition using OpenCV and the `face_recognition` library, suitable for applications such as access control, surveillance, or personalized user interactions.
