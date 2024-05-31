# Mystery Solver Application

The Mystery Solver application utilizes Bayesian networks to assist users in solving fictional mystery scenarios. Developed as a web application with Django, the project includes a Bayesian inference model designed to evaluate and process clues and evidence provided by users.

Key features of the application include:

1) Bayesian Inference Model: A robust Bayesian network engine that calculates the probabilities of guilty suspects based on the provided evidence.
2) Web Application Interface: Built with Django, the web app allows users to input clues and evidence seamlessly.
Database Integration: Mysterious data and user inputs are securely stored and managed within the web app's database.
3) Real-time Inference: Users receive immediate feedback on the likelihood of each suspect being the murderer based on their inputs.

This project provides an engaging platform for users to test their deductive reasoning and analytical skills through interactive mystery-solving.

## Steps to run the Model and Webapp

1) Install Python. The project was built with [python 3.11](https://www.python.org/downloads/release/python-3110/). All the installed libraries for the project are aligned with this version.

2) Get the code for the project. Use git clone or download the zip file of the code from GitHub.

3) Open the terminal or command prompt in the code directory and create a Python virtual environment in the code directory. 
```bash
python -m venv .venv
```
4) Activate the Virtual Environment now in the terminal or command prompt by running:
```bash
.venv\Scripts\activate
```

5) Now install all the dependencies to run the project.
```bash
pip install -r requirements.txt
```
All the dependencies will now be installed. Please don't close the terminal or command prompt for future usage.

6) To run the model file, open the code directory in VSCode. Open the bayesian_model_final.ipynb file. Select the virtual environment you created to run the file with. Install the Jupyter Notebook extension in VSCode if you don't have it installed.
   ![Screenshot (2312)](https://github.com/FarhanTahmid/Mystery-Solver-App/assets/62169118/fef2ed4c-a772-4a92-bef6-f600546e28e5)

8) To run the Web app, go to the terminal or command prompt where the virtual environment is active. Change the directory now to mystery_solver_webapp
```bash
cd mystery_solver_webapp
```

8) Run the following commands in the terminal or command prompt to start the Django server
```bash
python manage.py runserver
```

9) When the server starts, you will see a link in the terminal or command prompt of this type: "http://127.0.0.1:8000.". Copy and paste that into your browser to see the web app running.

Interface will look like this:
    ![Screenshot (2310)](https://github.com/FarhanTahmid/Mystery-Solver-App/assets/62169118/869da522-44ef-4599-bdf3-b6560c40767b)
    ![Screenshot (2311)](https://github.com/FarhanTahmid/Mystery-Solver-App/assets/62169118/5ab031c3-5148-4267-a27a-5504b55a72e2)

