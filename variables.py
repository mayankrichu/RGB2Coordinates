

'''

pose_landmarks = All the possible 33 human body pose landmarks which are described in the mediapipe library

'''


pose_landmarks = ["noseX","noseY","noseZ", "left_eye_innerX","left_eye_innerY","left_eye_innerZ","left_eyeX","left_eyeY","left_eyeZ","left_eye_outerX","left_eye_outerY","left_eye_outerZ", "right_eye_inner",
                  "right_eye_innerX","right_eye_innerY","right_eye_innerZ","right_eyeX","right_eyeY","right_eyeZ", "right_eye_outerX", "right_eye_outerY", "right_eye_outerZ",
                  "left_earX","left_earY","left_earZ", "right_earX", "right_earY", "right_earZ", "mouth_leftX","mouth_leftY","mouth_leftZ", "mouth_rightX", "mouth_rightY", "mouth_rightZ",
                  "left_shoulderX","left_shoulderY","left_shoulderZ",
                  "right_shoulderX","right_shoulderY","right_shoulderZ", "left_elbowX", "left_elbowY", "left_elbowZ", "right_elbowX", "right_elbowY", "right_elbowZ",
                  "right_elbowX","right_elbowY","right_elbowZ", "left_wristX", "left_wristY", "left_wristZ", "right_wristX", "right_wristY", "right_wristZ", "left_pinkyX", "left_pinkyY", "left_pinkyZ",
                  "left_indexX","left_indexY","left_indexZ", "right_indexX", "right_indexY", "right_indexZ", "left_thumbX", "left_thumbY", "left_thumbZ",
                  "right_thumbX","right_thumbY","right_thumbZ", "left_hipX", "left_hipY", "left_hipZ", "right_hipX", "right_hipY", "right_hipZ", "left_kneeX", "left_kneeY", "left_kneeZ",
                  "right_kneeX","right_kneeY","right_kneeZ", "left_heelX", "left_heelY", "left_heelZ", "right_heelX", "right_heelY", "right_heelZ", "left_foot_indexX", "left_foot_indexY", "left_foot_indexZ",
                  "right_foot_indexX","right_foot_indexY","right_foot_indexZ"]


rgb_folder_location =  r'C:\Users\Schorsch\Downloads\RGB videos'


rgb_to_pose_coordinates_location = r'C:\Users\Schorsch\Downloads\RGBcoordinates'

def empty_coordinates():
    emptyrow = []
    for i in range(0, 99):
        emptyrow.append(0)
    return emptyrow
