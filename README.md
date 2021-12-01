# J.A.R.V.I.S.
This is a repo for the Computer Vision project, which is a part of the DSBA 2020-2022.

# Darknet results
In order to reproduce the results from Darknet Yolov4, please:
  1. Go to Roboflow and download the re-annotated test set with the Darknet Yolo format.
  2. Download the trained weights **yolo4_trained.weights** from [Google Drive](https://drive.google.com/file/d/1j6MNI5Su-lYhSZBVPOB2241G25dII89t/view?usp=sharing)
  3. Having installed Darknet, git clone our repo. Move the downloaded images and weights to Darknet
  4. In the Darknet folder, run `./darknet detector test setup/obj.data setup/yolo-obj.cfg setup/yolo4_trained.weights -dont_show -ext_output < setup/test.txt > result.txt`
  5. In the Darknet folder, run `python results_evaluation/pred_to_CSV.py "result.txt"`
  6. In the Darknet folder, run `python results_evaluation/GT_to_csv.py "annotations/* .txt"`
  7. Follow the Jupyter notebook **Darknet results** to verify the results
