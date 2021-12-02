# J.A.R.V.I.S.
This is a repo for the Computer Vision project, which is a part of the DSBA 2020-2022.

# Darknet (Yolov4) results


| Label        | Avg. IOU           |
| ------------- |:-------------:| 
| Adidas     | 0.802068 |
| Apple Inc-     | 0.701490   |  
| Coca-Cola | 0.783254    | 
| Emirates     | 0.728129 |
| Hard Rock Cafe	    | 0.727069      |  
| Mercedes-Benz | 0.757376   | 
| NFL     | 0.772498 |
| Nike    | 0.661942      |  
| Pepsi | 0.816151      | 
| Puma | 0.737169     | 
| Starbucks     | 0.829903 |
| The North Face    | 0.766542    |  
| Toyota | 0.784606      | 
| Under Armour	 | 0.668946      |


In order to reproduce the results from Darknet Yolov4, please:
  1. Create a folder to test our results.
  2. Download the trained weights **yolo4_trained.weights** from [Google Drive](https://drive.google.com/file/d/1j6MNI5Su-lYhSZBVPOB2241G25dII89t/view?usp=sharing).
  3. Git clone darknet from https://github.com/AlexeyAB/darknet
  4. Git clone our repo. Compile darknet using the `Makefile` *provided by us* at `JARVIS/Darknet_Jarvis/setup/Makefile`. (You will need to replace the original Makefile by AlexeyAB with ours.)
  5. Go to Roboflow and download the re-annotated test set with the YOLO Darknet format into `darknet/data`. This will create a folder named `test`, which has the images and their labels, which we compare our predictions against. 
  6. From the darknet folder, run `./darknet detector test ../JARVIS/Darknet_Jarvis/setup/obj.data ../JARVIS/Darknet_Jarvis/setup/yolo-obj.cfg ../yolo4_trained.weights -dont_show -ext_output < ../JARVIS/Darknet_Jarvis/setup/test.txt > result.txt`
  7. In the Darknet_Jarvis folder, run `python results_evaluation/pred_to_CSV.py "../../darknet/result.txt"`.
  8. In the Darknet_Jarvis folder, run `python results_evaluation/GT_to_csv.py "../../darknet/data/test/* .txt"`.
  9. Follow the Jupyter notebook **Darknet results** to verify the results.



# Pytorch (Yolov5) results
**version L**

| Label        | Avg. IOU           |
| ------------- |:-------------:| 
| Adidas     | 0.871891 |
| Apple Inc-     | 0.840646   |  
| Coca-Cola | 0.893000    | 
| Emirates     | 0.858639 |
| Hard Rock Cafe	    | 0.843841      |  
| Mercedes-Benz | 0.841095   | 
| NFL     | 0.873054 |
| Nike    | 0.827050      |  
| Pepsi |0.902139      | 
| Puma | 0.861367     | 
| Starbucks     | 0.889383|
| The North Face    | 0.850859    |  
| Toyota | 0.854315      | 
| Under Armour	 | 0.808131      |


**version X**

| Label        | Avg. IOU           |
| ------------- |:-------------:| 
| Adidas     | 0.871891 |
| Apple Inc-     | 0.840646   |  
| Coca-Cola | 0.893000   | 
| Emirates     | 0.858639 |
| Hard Rock Cafe	    | 0.843841      |  
| Mercedes-Benz | 0.841095  | 
| NFL     | 0.873054 |
| Nike    | 0.827050      |  
| Pepsi | 0.902139      | 
| Puma | 0.861367     | 
| Starbucks     | 0.889383 |
| The North Face    | 0.850859    |  
| Toyota | 0.854315      | 
| Under Armour	 | 0.808131      |


In order to reproduce the results from Pytorch Yolov5 L and X, please:
1. create a conda environment in your machine (with python 3.8)
  `conda create -n "name" python=3.8`
  `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`
2. clone the github repository of yolov5 and install requirements
  `git clone https://github.com/ultralytics/yolov5`
  `cd yolov5`
  `pip install -r requirements.txt`
3. inside yolov5 folder download the trained weights (choose version (l or x l is faster x is better) and adjust image size if different from roboflow) here:  [YOLO v5X](https://drive.google.com/file/d/1fkev4tWwzn6s1n7gFE_8lfn18LQabHg-/view?usp=sharing), [YOLO v5L](https://drive.google.com/file/d/1Zdo2mm_BsAcmlXuNS0PtMPkju66AmP17/view?usp=sharing)
  `python detect.py --weights yolov5l.pt --img 640` (the weights present are in the google folder)
  `python detect.py --weights yolov5x.pt --img 640`
4. insert your train, test, valid folder inside the yolov5 folder where each train, test, and valid contains subfolders of images and labels. Make sure that the subfolder of labels contains txt where the label is a number and not a string.
5. create a new .yaml file with data specification
6. To train:
`python train.py --img 640 --batch 12 --epochs 20 --data data/data.yaml --weights yolov5x.pt`
7. To test:
`python detect.py --source test_folder/test/images --weights wegihts_folder/best.pt --img 640 --save-txt --save-conf`

