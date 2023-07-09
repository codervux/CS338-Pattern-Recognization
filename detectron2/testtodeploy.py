# from detectron2 import model_zoo
# c = model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml")

# print(c)
import pkg_resources,os
config_path = 'COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml'
c  = os.path.join("G:\BT_HK6_UIT\CS338 Nhan Dang\Doan\streamlit_pytorch_detectron2\detectron2\configs", config_path)

print(c)