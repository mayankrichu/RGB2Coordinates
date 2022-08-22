import cv2
import mediapipe as mp
import pandas as pd
from datetime import datetime
import numpy as np
import os
from variables import rgb_folder_location, pose_landmarks, rgb_to_pose_coordinates_location
from concurrent.futures import ThreadPoolExecutor

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose



'''
1. Using Mediapipe, fetch the coordinates of a RGB video and store it in a CSV file
2. The RGB videos are stored in a particular folder in different sub-directories according to the scenarios.
3. Look for all the files in different sub-directories
4. Run loop over the whole data and store it as  csv with relevant coordingates
5. Save the files in a new folder with _with_label suffix
6. Use Threading for processing the files using threading
'''






'''
Function to convert the rgb to coordinates
'''

def rgb_to_coordinates(file, file_location, rgb_to_pose_coordinates_location):

    cap = cv2.VideoCapture(file_location)
    index = 0
    pose_coordinates = []
    df_final = pd.DataFrame()
    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        model_complexity=2) as pose:
      while cap.isOpened():

        success, image = cap.read()
        # print("index", index)
        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          break
        index = index + 1
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        final_pose_coordinates = []
        #saving the pose to a csv file
        df = pd.DataFrame()
        try:
            landmark_coordinates = results.pose_world_landmarks.landmark
            for i in range(0, len(landmark_coordinates)):

                x_coordinates = landmark_coordinates[i].x
                y_coordinates = landmark_coordinates[i].y
                z_coordinates = landmark_coordinates[i].z
                pose_coordinates.extend([x_coordinates,y_coordinates,z_coordinates])
                #print(pose_coordinates)
                #print(i.splitlines())



            df = pd.DataFrame(pose_coordinates)
            df = df.transpose()
            print(df)
            pose_coordinates = []
        except:
            df = pd.DatatFrame(np.zeros(len(pose_landmarks)))

        df_final = df_final.append(df, ignore_index=True)
        #if cv2.waitKey(1) & 0xFF == 27:
         # break

    cap.release()
    #df_final = df_final.iloc[:, 1:]
    #df_final.columns = pose_landmarks
    file_path = rgb_to_pose_coordinates_location + '\\' + file
    extension = file_path.split(".")
    file_name  = extension[0] + ".csv"
    df_final.to_csv(file_name)

def rgb_coordinates_collector(file, file_location, rgb_to_pose_coordinates_location):
    print("main")

    with ThreadPoolExecutor(max_workers=10) as executor:  # using ThreadPoolExecutor with number of threads.
        x = executor.map(rgb_to_coordinates,file, file_location, rgb_to_pose_coordinates_location)   # mapping function fetch with session 100times and 100 urls
        executor.shutdown(wait=True)  # wait everything until x fetches every data
    print("batch completed")

if __name__ == '__main__':
    print(rgb_to_pose_coordinates_location)
    #using os.walk to get the folder and the files consisting in the folder
    # os.walk returns the tuple with three elements, (Main_Folder, SubFolder, Files)
    for it in os.walk(rgb_folder_location):
        files = it[2]
        for file in files:
            file_location = it[0] +'\\'+ file
            #print(file, file_location, rgb_to_pose_coordinates_location)
            try:
                rgb_to_coordinates(file= file, file_location= file_location, rgb_to_pose_coordinates_location = rgb_to_pose_coordinates_location )
            except:
                continue


'''
rgb_to_coordinates = running successfully
'''


