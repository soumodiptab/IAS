# Assignment 4:
```bash
.
├── gender_submission.csv (dataset file)
├── mobileApp.py
├── model.ipynb
├── model.pickle (gen)
├── passenger.csv (testing)
├── readme.md
├── server.py
├── test.csv (dataset file)
├── testing_data.csv (gen)
└── train.csv (dataset file)
```
### CSV file format
* Single row with passenger id's
* the first row must be col name with 'PassengerId'
### Instructions to run:
1. Run `model.ipynb` to generate files `model.pickle`,`testing_data.csv` which is required by `server.py` to make the indexes possible for passenger id's.
2. Run `server.py` as a flask application
3. Run `mobileApp.py`, operates in two modes
   1. in single mode any passenger id can be taken as input
   2. in batch mode specify the csv file and the column name.
### Description:
* Role 1 (AI model developer): 
Takes data and trains the model, develop a service around the model -- `model.inpynb`+`server.py`
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
1. First we work on the `model.py` and train the model, after tuning hyper parameters, save the model using `pickle`.
2. Some additional datasets are saved also for faster querying.
3. We then build a service around the model by loading it in `server.py`. 
4. The service is a REST api supplied with a list of passenger id's and it returns the predicted values for the titanic survival.
5. The REST api is called from our file called `mobileApp.py` where we take the input from either batch/console.
   1. The Batch input is given using a csv file, a sample is available in the folder: `passenger.csv`.