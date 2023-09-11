import cv2
import numpy as np
import glob 

img=cv2.imread(r"C:\Users\manth\Downloads\JJJJJJJJJJJJ.png",0) #edit the address according to need in raw string only


Templs=glob.glob(r"Python\OPEN_CV\letter_detect\TimeNR\Large\*.png") #edit the address according to need in raw string only
Detected_Letters=[]
def template_listing(Templs):
    Templates=[]
    for i in Templs:
        Templates.append(i)
    return Templates 
Templates=template_listing(Templs)  

def resize_template(base_img,letter_template): 
    print(type(base_img))
    T=base_img.shape
    letter_template=cv2.resize(letter_template,(T[1],T[0]),interpolation=cv2.INTER_LINEAR)
    return letter_template
    # cv2.imshow("Template",template)
    # print(T)

def Main_Image_Cropping(img):
    img2=img.copy()
    edged=cv2.Canny(img2,30,200)
    cv2.imshow("Canny",edged)
    
    # Thresh holding 
    thresh,img_edges=cv2.threshold(img2,150,255,cv2.THRESH_BINARY)
    # print("THRESH ------>",img_edges)
    print("Thresholding Value ",thresh)
    cv2.imshow("Threshold",img_edges)

    # create canvas 
    blank=np.zeros(img2.shape,dtype="uint8")
    blank.fill(255)
    
    # get all contours
    contours_draw,hierarchy=cv2.findContours(img_edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    
    # cv2.drawContours(blank,contours_draw,-1,(0,0,0),2)
    x,y,w,h=cv2.boundingRect(contours_draw[0])
    topC=[x,y,x+w,y+h]
    img_edges=img_edges[y:y+h,x:x+w]
    cv2.imshow("x", img_edges)
    return img_edges
    return img_edges
    return img_edges



def filtering(img):    
    img2=img.copy()
    edged=cv2.Canny(img2,30,200)
    thresh,img_edges=cv2.threshold(img2,150,255,cv2.THRESH_BINARY)
    # print("THRESH ------>",img_edges)
    print("Thresholding Value ",thresh)
    cv2.imshow("Threshold",img_edges)
    return img_edges


# filtering(temp)
img=filtering(img)

# USing Bitwise And Operator 
def XOR_Operator(a,b):
    new=cv2.bitwise_xor(a,b)
    return new

def comparing(IMG):
    # no. of pixels
    white_pixels=np.sum(IMG==255)
    black_pixels=np.sum(IMG==0)
    percentage=(white_pixels/(white_pixels+black_pixels))*100
    print("Percentage of white colors",percentage)
    return percentage
        
def Extract_each_template():
    esk=64
    for j in Templates:
        esk+=1
        print("\nLetter ",chr(esk))
        each_template=cv2.imread(j,0)
        each_template=resize_template(img,each_template)
        each_template=filtering(each_template)
        Added_image=XOR_Operator(img,each_template)
        cv2.imshow("Bitwise XOR ",Added_image)
        Prc=comparing(Added_image)
        if Prc<=25:
            print("LETTER DETECTED !!")
            character=chr(esk)
            Detected_Letters.append(character)
        
        else:
            print("LETTER NOT DETECTED")

Extract_each_template()
print("Detected Letters -",Detected_Letters)
cv2.waitKey(0)
cv2.destroyAllWindows()
