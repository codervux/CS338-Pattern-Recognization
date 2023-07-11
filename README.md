# streamlit_pytorch_detectron2
Streamlit an open source library used to make data apps really easily. In this I am trying to deploy a detectron2 pytorch model through streamlit


1. Download model_final.pth from GitRelease (https://github.com/codervux/CS338-Pattern-Recognization/releases/tag/DiffusionDet_Streamlit_v1.0.0)
2. go to \streamlit_pytorch_detectron2\detectron2. Then create 2 folder: inputs_demo, outputs_demo.
3. move model_final.pth to \streamlit_pytorch_detectron2\detectron2\output\

- go to detectron2 folder, run file deploy_bruh.py
streamlit run deploy_bruh.py

