Hi ,This is Vijay Gopi Sankar.

The Repository represent the Skin Lesion Classification using Deep Learning.
from this research we can classify the type of skin lesion in which the image refer in web page itself.


Steps to Run

 For Google Colab:
1.Download the HAM10000 dataset  from the Harvard dataverse  website following the below link  

        https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T 

2. Extract the Folder and upload it to google drive to run it in Google colab
3.Now open the Google colab and run the code by mounting the colab with google drive by providing the file path of the data file.
4.Download the model which is saved in the google drive.
5.Now download the Flask folder and paste that downloaded model in the Flask folder  and run it using the VS code .
6. After running the VS code, copy the  link which is generated in the terminal and paste it in the browser. 
7. upload a image to get which type of skin lesion does it belong to and how accurate the image .


for jupyter:

Model Training:
*	Open the Jupyter Notebook in the notebooks/ directory.
*	Run all cells to preprocess the dataset, train the model, and save the trained weights (xception_model.h5).
 	 Web Deployment:
*	Navigate to the flask_app/ directory.
*	Start the Flask server,and run the following commands in the terminal
          bash
          Copy code
          python app.py
*	Open your browser and go to http://127.0.0.1:5000 to use the web application.

Due to large size of dataset and the saved model I didn't upload the files.So plz download the data set file from the above mentioned link in the Step of instructions to run the code..

If Any Query kindly mail me 

     vijaygopisankar2000@gmail.com
