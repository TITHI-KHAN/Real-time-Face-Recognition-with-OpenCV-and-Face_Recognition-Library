import cv2
import face_recognition
import numpy as np

# Load sample pictures and learn how to recognize them.
known_face_encodings = []
known_face_names = []

# Load a sample picture and learn how to recognize it.
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]

# Assuming you have more images, repeat the process as necessary...
# Example for a second person
image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]

known_face_encodings = [person_1_face_encoding, person_2_face_encoding]
known_face_names = ["Mejbah Ahammad", "Rashedul A Shakil"]  # Replace with actual names


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
