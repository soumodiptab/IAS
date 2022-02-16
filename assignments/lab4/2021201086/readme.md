# Assignment 4:
```bash
.
├── gender_submission.csv (dataset file) <--needed for accuracy testing
├── mobileApp.py
├── model.ipynb
├── model.pickle (gen)
├── readme.md
├── server.py
├── test.csv (dataset file) <--needed for acccuracy testing
└── train.csv (dataset file) <--needed for training
```
### CSV file format
* should be same format as `test.csv`
### Instructions to run:
1. Run `model.ipynb` to generate files `model.pickle` which is required by `server.py` to make the predictions.
2. Run `server.py` as a flask application
3. Run `mobileApp.py`, operates in batch mode specify the csv file.
### Description:
* Role 1 (AI model developer): 
Takes data and trains the model, develop a service around the model -- `model.ipynb`+`server.py`
* Role 2 (End App developer): 
This End App uses the model trained by Role 1. -- `server.py`+`mobileApp.py`
* Role 3 (Deployer): 
Deploy the service made by role 1 into the AI production platform.
* Role 4 (AI production platform)
Only the AI service is deployed here. (We do not care about deployment of mobile
app)
* Role 5 (End user)
Accesses the mobile app. -- `mobileApp.py`
### Full working:
1. First we work on the `model.ipynb` and train the model, after tuning hyper parameters, save the model using `pickle`.
   1. `model.ipynb` needs `train.csv` to train the model and `test.csv` to check if model works fine.
2. We then build a service around the model by loading it in `server.py`. 
3. The service is a REST api supplied with a dataframe and it returns the predicted values for the titanic survival.
4. The REST api is called from our file called `mobileApp.py` where we take the input from either batch mode using a csv
   1. The Batch input is given using a csv file, a sample is available in the folder: `test.csv`.