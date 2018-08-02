# ADAS_Detection
ADAS(Advanced Driver Assistance System)

1. data set : https://pjreddie.com/projects/pascal-voc-dataset-mirror/ 에서 VOC2007, VOC2007TEST, VOC2012 download
그 후, ADAS_train/dataset 안에 VOCROOT 폴더 생성 후 3개의 데이터 파일 넣기.

2. https://drive.google.com/drive/folders/184srhbt8_uvLKeWW_Yo8Mc5wTyc0lJT7 에서 5개의 파일 download, 그 후, ADAS_train/model 안에 넣기.

3. train_eval/main.py 파일을 Anaconda or Windows prompt 에서 경로 맞춘 후 실행.
EX) python main.py video car.mp4 car_output.mp4

4. ADAS_eval/make_pytube.py : 원하는 동영상을 YOUTUBE 에서 찾아서 주소 입력 후, .mp4 형식으로 저장 가능.

5.
