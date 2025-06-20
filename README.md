
- [![coverage](https://codecov.io/gh/ConradKash/sunbird_tasks/graph/badge.svg?token=QUC2ACKSR7)](https://codecov.io/gh/ConradKash/sunbird_tasks)

- Fork this repository to create your own copy.
-  ([More info about forking a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo))
- Clone your repository to access it locally: `git clone https://github.com/<your-username>/model-test.git`. (Replace `<your-username>` with your Github username.)
- Replace the model file `model.pkl` with your model file
- then in the `model.py` replace the `True` if you used a pipeline
- Create a python virtual environment: `python -m venv venv`
- Activate the virtual environment: 
  - Linux/Mac: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate.bat`
- Install the required python packages: `pip install -r requirements.txt`
- Run the command `pytest`. 
- Run  `uvicorn app.main:app --relaod to start the API and run tests
