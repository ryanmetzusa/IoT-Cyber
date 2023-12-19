# IoT-Cyber

In this project, I found a kaggle dataset for cyber attacks on Internet of Things devices. The dataset was large, about 14 gb containing 70m+ observations. The dataset was unbalanced, so I had to clean and upscale/downscale before modeling. I modeled with randomforest and created a SHAP plot at the end for each classification's variable importance. The model had 93.5% accuracy, which could be improved. I used a modest grid search due to hardware limitation but can be optimized to be more robust depending on the time constraint and resources. I also exported the finished model but its too large to upload here. The model training was about 3 hours on a 8 core amd ryzen 7 7700X processor 32 gb ram machine.

The merge file is to merge all of the fragmented csv's into one csv. The juypter notebook is the script in chunks to split the processes for better understanding.

You can find the dataset here: 
https://www.kaggle.com/datasets/madhavmalhotra/unb-cic-iot-dataset/data

UPDATE: Created a chunking/merging python script for the pickle model file. You can find the chunked pieces for my model, just run the picklecombine python script to combine.
