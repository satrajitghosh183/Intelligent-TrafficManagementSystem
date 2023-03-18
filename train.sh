source /opt/intel/inteloneapi/setvars.sh  > /dev/null 2>&1
source activate pytorch
python yolov5/train.py --data dataDiff.yaml --cfg yolov5n.yaml --batch-size 32 --epochs 5 --name TrainModel