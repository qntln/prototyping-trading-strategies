# Prototyping trading strategies in Python

## Getting started

1. Make sure you have Python 3.6 installed on your computer. Follow these instructions if you don't.

  - [Windows](http://docs.python-guide.org/en/latest/starting/install3/win/)
  - [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/)
  - [macOS](http://docs.python-guide.org/en/latest/starting/install3/osx/)

2. You can verify that you have the correct and working version by running `python3 --version`. It should print `Python 3.6.3` or `Python 3.6.1` for example.

3. Install pipenv, a modern Python package manager, by running `pip3 install pipenv` (or `brew install pipenv` on macOS). See [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for more details.

4. Create a new empty directory called `ki-workshop` and move to it in your terminal (`cd ki-workshop`).

5. Run the following command to install all the Python packages we will need to run our code:

	```
	pipenv install pandas==0.21.0 plotly==2.2.1 jupyter==1.0.0 scipy==1.0.0 statsmodels==0.8.0 numpy==1.13.3
	```

6. We will be using [Jupyter Notebook](http://jupyter.org) to prototype our strategy. Check that it works for you by running the following command. It should open a web browser window for you.

	```
	pipenv run jupyter notebook
	```

7. Stay tuned for the code and data you will be provided at the December 7 workshop!