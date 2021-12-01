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
