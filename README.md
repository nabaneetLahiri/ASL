# American-Sign-Languge-Recognition
![asl_demo](https://user-images.githubusercontent.com/42116611/109388110-1783cb80-792b-11eb-9dc9-1c477136e245.gif)

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
```python
    conda activate asl 
    python create.py
 ```

## [Training](https://github.com/nabaneetLahiri/American-Sign-Languge-Recognition/blob/main/train.ipynb)
Upload the data set and the train.ipynb file on ur drive. Things to be noted
- Images of J and Z should be in a folder named MotionSigns in ur drive 
- Rest of the images should be in a folder named StationarySigns in ur drive
- Both of the above folder should contain a folder named ^ with images of blank background

#### Run the file in google colab 
Two models are to be made:
- First model is for the sationary signs ![step1](https://user-images.githubusercontent.com/42116611/109387193-e9e85380-7925-11eb-89d1-7644426cf2f5.PNG) change the name of model to keras.StationaryModel
- Second model is for motion signs ![step2](https://user-images.githubusercontent.com/42116611/109387218-1bf9b580-7926-11eb-98e5-2922cf331359.PNG) change the name of the model to keras.MotionModel

## [Hand Sign Detection](https://github.com/nabaneetLahiri/American-Sign-Languge-Recognition/blob/main/Run.py)
Download the models from ur drive and put in the same folder with run.py. 
```python
    conda activate asl 
    python run.py
 ```
The pretrained models are given here 
[keras.MotionModel](https://drive.google.com/file/d/1-iP2KnLVodcp8TqokZjS5NMQnB2x2Eey/view?usp=sharing), 
[keras.StationaryModel](https://drive.google.com/file/d/1i9SeORCZlnsBfNzWy_TIGNwuc-6Ni5zA/view?usp=sharing).  
Run the run.py file put ur hand in the box provided and the sign will be detected.
![a](https://user-images.githubusercontent.com/42116611/109385459-07172500-791a-11eb-9d77-a1ded088efa2.PNG)
Press space bar for space, backspace to delete a character and enter to read the sentence out loud

<!--
## Results
![a](https://user-images.githubusercontent.com/42116611/109385459-07172500-791a-11eb-9d77-a1ded088efa2.PNG)
![b](https://user-images.githubusercontent.com/42116611/109385460-08e0e880-791a-11eb-8983-9db971849ef1.PNG)
![c](https://user-images.githubusercontent.com/42116611/109385461-09797f00-791a-11eb-9ef7-f9aa0872f2f7.PNG)
-->
