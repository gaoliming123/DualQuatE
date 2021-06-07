# Datasets
We use five common datasets: WN18, WN18RR, FB15k, FB15k-237, YAGO3-10. Because the total size of datasets is too big to upload. So we upload several examples of datasets in the folder data.
# Source codes
Our code is based on RotatE.
## Requirements
Required environment is shown in /source code/DualQuatE/requirements.txt. 2.2 Content
we upload our source codes of DualQuatE, DualQuatE-1 and DualQuatE-2. We implement our algorithms with func- tion DualQuatE in the file: /source code/DualQuatE/codes/model.py, /source code/DualQuatE-1/codes/model.py and /source code/DualQuat-2/codes/model.py respectively.
## Run
For example, if you want to test the result of model DualQuatE, you can run the following command in the directory source code/DualQuatE:
bash run.sh train DualQuatE YAGO3-10 0 0 512 128 200 24.0 1.0 0.001 100000 4
The log file will be saved in directory source code/DualQuatE/models
Note: you need to downlaod the datasets from the above link into the directory source code/DualQuatE/data fist. If you want to test DualQuatE-1 or DualQuatE-2, you need to copy the datasets to the corresponding directory, such as copy source code/DualQuatE/data to the directory source code/DualQuatE-1/.
## Best configs
There are the best config of our models.
DualQuatE:

YAGO3-10: bash run.sh train DualQuatE YAGO3-10 3 8 1024 200 300 26.0 1.0 0.0004 100000 1

wn18rr: bash run.sh train DualQuatE wn18rr 0 0 1024 128 100 6.0 0.5 0.0008 80000 8

FB15k-237: bash run.sh train DualQuatE FB15k-237 0 0 1024 256 200 9.0 1.0 0.0001 100000 16

wn18: bash run.sh train DualQuatE wn18 0 0 1024 128 100 12.0 0.5 0.0008 80000 8

FB15k: bash run.sh train DualQuatE FB15k 0 0 1024 32 500 24.0 1.0 0.0003 150000 8

DualQuatE-1:

YAGO3-10: bash run.sh train DualQuatE YAGO3-10 0 0 512 128 200 24.0 1.0 0.0006 100000 4

FB15k-237: bash run.sh train DualQuatE FB15k-237 0 0 1024 32 1000 9.0 1.0 0.00005 100000 8

wn18rr: bash run.sh train DualQuatE wn18rr 0 0 1024 128 200 6.0 0.5 0.0001 80000 8

wn18: bash run.sh train DualQuatE wn18 0 0 512 128 200 14.0 0.5 0.0005 80000 8

FB15k: bash run.sh train DualQuatE FB15k 0 0 1024 32 500 24.0 1.0 0.0003 150000 8

DualQuatE-2:
YAGO3-10: bash run.sh train DualQuatE YAGO3-10 0 0 1024 128 200 24.0 1.0 0.0005 100000 4

FB15k-237: bash run.sh train DualQuatE FB15k-237 0 0 1024 128 200 9.0 1.0 0.0001 100000 16 note: with L2 regularization 0.000001 for embeddings
1

wn18rr: bash run.sh train DualQuatE wn18rr 0 0 1024 128 100 6.0 0.5 0.0001 80000 8 note: with L2 regularization 0.000001 for embeddings

wn18: bash run.sh train DualQuatE wn18 0 0 1024 128 100 12.0 0.5 0.0008 80000 8 note: with L2 regularization 0.000001 for embeddings

FB15k: bash run.sh train DualQuatE FB15k 0 0 1024 128 200 24.0 1.0 0.0003 150000 16 note: with L2 regularization 0.000001 for embeddings
