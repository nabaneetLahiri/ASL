# American-Sign-Languge-Recognition
## Prerequisite
- [Anaconda](https://www.anaconda.com/)
- Use the [requirements.txt](https://github.com/nabaneetLahiri/American-Sign-Languge-Recognition/blob/main/requirements.txt) to install required libraries
 ```python
    conda create --name asl --file requirements.txt
 ```

## [Creating data set](https://github.com/nabaneetLahiri/American-Sign-Languge-Recognition/blob/main/create.py)
Run create.py to create the dataset. The dataset will be created in C:\Dataset to change this change the path varibale in line 5 accordingly. 
Parameters given druing runtime are: 
- Starting index, from which number the file name will start(Give 1 as default). 
- Ending index, till which number the file name will end at.

## [Training](https://github.com/nabaneetLahiri/American-Sign-Languge-Recognition/blob/main/train.ipynb)
Upload the data set and the train.ipynb file on ur drive. Things to be noted
- Images of J and Z should be in a folder named MotionSigns in ur drive 
- Rest of the images should be in a folder named StationarySigns in ur drive
- both of the above folder should contain a folder named ^ with blank background

####Run the fle in google colab 





## Results
![a](https://user-images.githubusercontent.com/42116611/109385459-07172500-791a-11eb-9d77-a1ded088efa2.PNG)
![b](https://user-images.githubusercontent.com/42116611/109385460-08e0e880-791a-11eb-8983-9db971849ef1.PNG)
![c](https://user-images.githubusercontent.com/42116611/109385461-09797f00-791a-11eb-9ef7-f9aa0872f2f7.PNG)
