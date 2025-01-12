import cv2
import dlib
import numpy as np
from imutils import face_utils

# Initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def swap_faces(image1_path, image2_path, output_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1 is None or image2 is None:
        print("Error: One of the images could not be read.")
        return

    # Detect faces in the images
    rects1 = detector(image1, 1)
    rects2 = detector(image2, 1)

    if len(rects1) == 0 or len(rects2) == 0:
        print("No faces detected in one or both images.")
        return

    # Get the facial landmarks
    shape1 = predictor(image1, rects1[0])
    shape2 = predictor(image2, rects2[0])

    shape1 = face_utils.shape_to_np(shape1)
    shape2 = face_utils.shape_to_np(shape2)

    # Apply face swapping
    face1 = image1[rects1[0].top():rects1[0].bottom(), rects1[0].left():rects1[0].right()]
    face2 = image2[rects2[0].top():rects2[0].bottom(), rects2[0].left():rects2[0].right()]

    face2_resized = cv2.resize(face2, (face1.shape[1], face1.shape[0]))

    # Replace face1 with face2 in image1
    image1[rects1[0].top():rects1[0].bottom(), rects1[0].left():rects1[0].right()] = face2_resized

    # Save the output image
    cv2.imwrite(output_path, image1)
    print(f"Swapped face saved to {output_path}")

# Example usage (comment this out when integrating into Django)
# swap_faces('image1.jpg', 'image2.jpg', 'output.jpg')