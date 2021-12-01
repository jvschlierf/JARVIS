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
  4. Git clone our repo. Compile darknet using the `Makefile` *provided by us*.
  5. Go to Roboflow and download the re-annotated test set with the Darknet Yolo format and move to `darknet/data/test`.
  6. Move the files **obj.names** & **obj.data** to `darknet/data/` and the file **yolo-obj.cfg** to `darknet/cfg`. 
  7. In the darknet folder, run `./darknet detector test data/obj.data cfg/yolo-obj.cfg ../yolo4_trained.weights -dont_show -ext_output < data/test.txt > result.txt`
  8. In the Darknet folder, run `python results_evaluation/pred_to_CSV.py "../darknet/result.txt"`.
  9. In the Darknet folder, run `python results_evaluation/GT_to_csv.py "annotations/* .txt"`.
  10. Follow the Jupyter notebook **Darknet results** to verify the results.
