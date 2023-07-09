import streamlit as st
import cv2
import os


def main():
    new_title = '<p style="font-size: 42px;">Welcome to my Object Detection App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)

    read_me = st.markdown("""
    This project was built using Streamlit and OpenCV 
    to demonstrate DiffusionDet Object detection in both videos(pre-recorded)
    and images.
    
    
    This DiffusionDet object Detection project can detect pedestrian and rider(i.e classes)
    in either a video or image. """
    )
    st.sidebar.title("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("About","Object Detection(Image)","Object Detection(Video)"))

    if choice == "Object Detection(Image)":
        #st.subheader("Object Detection")
        read_me_0.empty()
        read_me.empty()
        #st.title('Object Detection')
        object_detection_image()


    elif choice == "About":
        print() 

def object_detection_image():
    st.title('Object Detection for Images')
    st.subheader("""
    This object detection project takes in an image and outputs the image with bounding boxes created around the objects in the image
    """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])

    if file != None:
        st.write("Uploaded test {}".format(file.name))

        #save image just uploaded into this computer

        inputpath = os.path.join("inputs_demo",file.name)
        outpath = os.path.join("outputs_demo",file.name)
        print(outpath)
        with open(inputpath, "wb") as f:
            f.write(file.getbuffer())
        
            
        os.system("python demo.py --config-file output/config.yaml --input " + inputpath + " --output "+ outpath)
        print("DONE")
        st.image(outpath, "Pedestrian Detection Result")
if __name__ == '__main__':
		main()