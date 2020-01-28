import cv2
import math
import os

def encodeMessage(image, msg, fileName):


  
def decodeMessage(image):
    

if __name__== "__main__":
    while True:
        choice = input("Decode or encrypt? (d/e): ")
        while not(choice == 'd' or choice == 'e'):
            print("\n[ERROR] Invalid choice, please input 'd' or 'e'!")
            choice = input("\nDecode or encrypt? (d/e): ")
        print()
        if(choice == 'd'):
            for subdir, dirs, files in os.walk("./decrypt"):
                for file in files:
                    filepath = subdir + os.sep + file

                    if filepath.endswith(".png"):
                        print("Decoded message from [" + file + "]: " + decodeMessage(Image.open("./decrypt/" + file)))
            print("\nFinished Decoding images.")
        
        else:
            msg = input('Enter message to encode: ')

            for subdir, dirs, files in os.walk("./encrypt"):
                for file in files:
                    filepath = subdir + os.sep + file

                    if filepath.endswith(".png"):
                        try:
                            encodeMessage(Image.open("./encrypt/" + file), msg, file)
                            print("Encoded message into [" + file + "]")
                        except ValueError:
                            print("Message too long to encode in [" + file + "]")
            print("\nFinished Encoding images.")
