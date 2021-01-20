# openimagesv6 or coco
Download specific subset from Google Open Images V6 or Microsoft COCO datastes.

## Required file:
We will extract subclass image ids from this file.
```
$ wget https://storage.googleapis.com/openimages/v6/oidv6-train-images-with-labels-with-rotation.csv
$ wget https://storage.googleapis.com/openimages/2018_04/validation/validation-images-with-rotation.csv
$ wget https://storage.googleapis.com/openimages/2018_04/test/test-images-with-rotation.csv
```
Python script that downloads images from CVDF
```
$ wget https://raw.githubusercontent.com/openimages/dataset/master/downloader.py
```
## Get Image IDs
Create a text file containing all the image IDs that you're interested in downloading
```
$ python imgList.py -c <classes-name> -p <image-ids> -t <file-type>

optional arguments:
  -h , --help       show this help message and exit
  -c , --classes    classes name
  -p , --ids        path to image ids file
  -t , --type       file type e.g train/test/validation
```
Example:
To extract train image ids of Cattle,Sheep and Goat:
```
$ python imgList.py -c Cattle,Sheep,Goat -p oidv6-train-images-with-labels-with-rotation.csv -t train
```
## Start Downloading
```
$ python downloader.py <IMAGE_LIST_FILE> --download_folder <DOWNLOAD_FOLDER> --num_processes <number>

optional arguments:
  -h, --help           show this help message and exit
  --num_processes      Number of parallel processes to use (default is 5).
  --download_folder    Folder where to download the images.
  
  
  
  Example:
  python downloader.py train.txt --download_folder /home/lab/myfolder/ --num_processes 5
  python downloader.py test.txt --download_folder /home/lab/myfolder/ --num_processes 5
  python downloader.py validation.txt --download_folder /home/lab/myfolder/ --num_processes 5
```
