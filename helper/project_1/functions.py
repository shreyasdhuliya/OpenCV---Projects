import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def show_image(img):
    plt.figure(figsize = (13,13))
    plt.imshow(img,cmap = "gray")

def import_image(image_path):
    '''
    Function takes in image path and returns image
    '''
    img = cv2.imread(image_path,0)
    return img


def adaptive_multiple(img):
    '''
    Performs adaptive thresholding
    
    returns
    -------
    list of images
    with various filter sizes
    '''
    h,w = img.shape
    images_adap_test = []
    count = 0
    for i in range(51,h,50):
        img_a = img.copy()
        images_adap_test.append(cv2.adaptiveThreshold(img_a,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,i,0))
        count = count + 1
    return images_adap_test,count



def show_create_weave(img_processed):
    
    '''
    Returns 20 rgb images for different values of thresholds in the 
    range [20,201] with interval of 20
    
    '''
    prev = "White"
    
    plt.figure(figsize = (10,10))
    plt.title('The Image used to create weave')
    plt.imshow(img_processed,cmap = "gray")
    
    h,w = img_processed.shape
    
    r_warf,g_warf,b_warf = input("WARF (r,g,b) format: eg.100 100 255:").split() 
    r_weft,g_weft,b_weft = input("WEFT (r,g,b) format: eg.100 100 255:").split() 
    
    width_of_weft = input("Enter Weft width(integer):")
    width_of_warf = input("Enter Warf width(integer):")
    
    print("number of warf:{} and weft:{}:".format(w//int(width_of_weft),h//int(width_of_warf)))
    
    width_of_weft = int(width_of_weft)
    width_of_warf = int(width_of_warf)
    
    #to avoid continuous weft
    list_  = [True,True,True,False,True,True,True]
    
    #list containing multiple weaves
    img_weaves = []
    
    #for different values of threshold
    for thresh in range (20,241,20):
        
        #create a copy of the image image
        img_p_copy = img_processed.copy()
        #create an empty image
        img_canvas = np.zeros([h,w,3], dtype = np.uint8)
        
        #weft
        for i in range(0,h,width_of_weft):
            #waft
            for j in range(0,w,width_of_warf): 

                #if average less than thresh put weft with probability:6/7
                if int(np.round(np.average(img_p_copy[i:i+width_of_weft,j:j+width_of_warf]),0)) < thresh:  #20,40,60,80,100,120,140,160,180,200
                    
                    if prev == 'White':
                        #put black
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_weft
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_weft
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_weft
                        prev = 'Black'
                    
                    else:
                        if random.choice(list_):
                            #weft 0
                            img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_weft
                            img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_weft
                            img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_weft
                            prev = 'Black'
                        else:
                            #warf 255
                            img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_warf
                            img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_warf
                            img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_warf
                            prev = 'White'

                # else put warf
                else: 
                    img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_warf
                    img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_warf
                    img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_warf
                    prev = 'White'

        for i in range(0,h, width_of_weft):
            img_canvas[i,0:w,0] = 255
            img_canvas[i,0:w,1] = 255
            img_canvas[i,0:w,2] = 255
        
        for i in range(0,w, width_of_warf):
            img_canvas[0:h,i,0] = 255
            img_canvas[0:h,i,1] = 255
            img_canvas[0:h,i,2] = 255
        
        img_weaves.append(img_canvas)
        
    #return List of images    
    cv2.imshow('thresh : 20',img_weaves[0])
    cv2.imshow('thresh : 40',img_weaves[1])
    cv2.imshow('thresh : 60',img_weaves[2])
    cv2.imshow('thresh : 80',img_weaves[3])
    cv2.imshow('thresh : 100',img_weaves[4])
    cv2.imshow('thresh : 120',img_weaves[5])
    cv2.imshow('thresh : 140',img_weaves[6])
    cv2.imshow('thresh : 160',img_weaves[7])
    cv2.imshow('thresh : 180',img_weaves[8])
    cv2.imshow('thresh : 200',img_weaves[9])
    cv2.imshow('thresh : 220',img_weaves[10])
    cv2.imshow('thresh : 240',img_weaves[11])
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def get_image():
    '''
    takes image path and shows image
    '''
    image_path = input("Enter the image path:")
    
    #original image saved in img
    img = import_image(image_path)
    # getting height and width
    h,w = img.shape
    #cancvas
    plt.figure(figsize = (10,10))
    #shows image with pixels in x,y
    plt.imshow(img,cmap ="gray")
    print("width of the image:",w," pixels")
    print("height of the image:",h," pixels")
    
    return img
    
def show_mul_adap(img):
    '''
    Show images with multiple 
    filter sizes
    
    input
    ------
    img: Gray scale image
    '''
    #getting images list
    img_test_adap,count = adaptive_multiple(img)

    fig = plt.figure(figsize = (36, 40)) 
    row = count//5
    #Ploting image using 
    filter_size = 51
    for i in range(len(img_test_adap)):
        ax = fig.add_subplot(row+1, 5, i + 1)
        ax.imshow(img_test_adap[i],cmap='gray')
        ax.set_title("filter size {}".format(filter_size),fontsize=27)  
        filter_size = filter_size + 50
        
def perform_adap(img):
    '''
    performs addaptive thresholding with filter size
    
    input
    ------
    img :gray scale image
    filter_siz: user input filter size
    
    returns
    -------
    threshold image
    '''
    filter_siz = input("Enter enter filter size(should be odd number):")
    img_a = img.copy()
    img_processed = cv2.adaptiveThreshold(img_a,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,int(filter_siz),4)
    #cancvas
    plt.figure(figsize = (10,10))
    #shows image with pixels in x,y
    plt.imshow(img_processed,cmap ="gray")
    
    return img_processed


def perform_morf_close(img_processed):
    
    img_p = img_processed.copy()
    choice = input("Enter the morph structuring element Press 1. RECT 2. ELLIPSE 3. CROSS(Integer input): ")
    dimen = input("Enter Dimenstion of the structuring element 3 -> (3,3) 5 -> (5,5):(ODD INTERGER ONLY):")
    if int(choice) == 1:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(int(dimen),int(dimen)))
    elif int(choice) == 2:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(int(dimen),int(dimen)))
    else:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(int(dimen),int(dimen)))

    img_p = cv2.morphologyEx(img_p, cv2.MORPH_CLOSE, kernel)
    show_image(img_p)
    
    return img_p
    
    
def perform_create_weave(img_processed):
    
    '''
    creates weave, shows and
    saves image.
    '''
    prev = 'White'
    
    plt.figure(figsize = (10,10))
    plt.title('The Image used to create weave')
    plt.imshow(img_processed,cmap = "gray")
    
    h,w = img_processed.shape
    
    r_warf,g_warf,b_warf = input("WARF (r,g,b) format: eg.100 100 255:").split() 
    r_weft,g_weft,b_weft = input("WEFT (r,g,b) format: eg.100 100 255:").split() 
    
    width_of_weft = input("Enter Weft width(integer):")
    width_of_warf = input("Enter Warf width(integer):")
    
    print("number of warf:{} and weft:{}:".format(w//int(width_of_weft),h//int(width_of_warf)))
    
    width_of_weft = int(width_of_weft)
    width_of_warf = int(width_of_warf)
    
    #to avoid continuous weft
    list_  = [True,True,True,False,True,True,True]
    
    #for different values of threshold
    thresh = input("Enter thresh(integer) [0 -255]:")
    thresh = int(thresh)
        
    #create a copy of the image image
    img_p_copy = img_processed.copy()
        #create an empty image
    img_canvas = np.zeros([h,w,3], dtype = np.uint8)
        
        #weft
    for i in range(0,h,width_of_weft):
            #waft
        for j in range(0,w,width_of_warf): 

                #if average less than thresh put weft with probability:6/7
            if int(np.round(np.average(img_p_copy[i:i+width_of_weft,j:j+width_of_warf]),0)) < thresh:  #20,40,60,80,100,120,140,160,180,200
                
                if prev == 'White':
                    img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_weft
                    img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_weft
                    img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_weft
                    prev = 'Black'
                    
                else:
                    
                    if random.choice(list_):
                            #weft
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_weft
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_weft
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_weft
                        prev = 'Black'
                    else:
                            #warf
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_warf
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_warf
                        img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_warf
                        prev = 'White'

            # else put warf
            else:
                img_canvas[i:i+width_of_weft,j:j+width_of_warf,0] = r_warf
                img_canvas[i:i+width_of_weft,j:j+width_of_warf,1] = g_warf
                img_canvas[i:i+width_of_weft,j:j+width_of_warf,2] = b_warf
                prev = 'White'

    for i in range(0,h, width_of_weft):
        img_canvas[i,0:w,0] = 255
        img_canvas[i,0:w,1] = 255
        img_canvas[i,0:w,2] = 255
        
    for i in range(0,w, width_of_warf):
        img_canvas[0:h,i,0] = 255
        img_canvas[0:h,i,1] = 255
        img_canvas[0:h,i,2] = 255
        
    #return List of images    
    cv2.imshow('thresh ' + str(thresh),img_canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    image_name = input("Write the image name you want to save it as(example: weave_1)")
    image_name = image_name + '.png'
    
    cv2.imwrite(image_name,img_canvas)