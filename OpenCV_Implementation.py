
# coding: utf-8

# In[102]:


import cv2
import os
os.chdir('C:\\Users\\agadiya\\Desktop\\PythonLearn\\opencv')


# In[103]:


img= cv2.imread("galaxy.jpg",1)


# In[104]:


type(img)


# In[105]:


print(img)


# In[106]:


img.shape


# In[107]:


resized_img= cv2.resize(img,(1000,500))


# In[108]:


cv2.imshow("galaxy.jpg",resized_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()


# In[109]:


# Face detection begins here


# In[110]:


import cv2
os.chdir('C:\\Users\\agadiya\\Desktop\\PythonLearn\\opencv\\Files')
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade


# In[111]:


img=cv2.imread("IMG_A.jpg")


# In[112]:


cv2.imshow("IMG_A.jpg",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()


# In[113]:


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces_gray=face_cascade.detectMultiScale(gray_img,scaleFactor=1.07,minNeighbors=2)


# In[114]:


print(faces_gray)


# In[115]:


faces_original=face_cascade.detectMultiScale(img,scaleFactor=1.03,minNeighbors=3)


# In[116]:


print(faces_original)


# In[117]:


#Adding the rectangle in the image

for x,y,w,h in faces_original:
    img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)

cv2.imshow("Akash.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Capturing a video

# In[66]:


import time, cv2
video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    print(check)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #time.sleep(3)
    cv2.imshow("Capturing", gray)
    key= cv2.waitKey(2000)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

