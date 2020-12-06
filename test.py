import numpy as np
import cv2

de = cv2.imread('data/decryption.jpg')
en = cv2.imread('data/encryption.png')


place_List = []

for i in range(de.shape[0]):
    for j in range(de.shape[1]):
        if not (de[i][j] == en[i][j]).all():
            place_List.append(list(en[i][j]))


print(place_List)
print(len(place_List))
print(en.shape[0]*en.shape[1])
# print(en[108, 257])
# print(de[108, 257])

word = bytes([place_List[3][0]]) + bytes([place_List[3][1]]) +bytes([place_List[3][2]])
print()
print(word.decode('utf-8'))