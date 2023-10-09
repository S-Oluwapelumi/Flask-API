# Flask-API
Crafting a Flask server that can take an incoming POST request

## What is Flask?
Flask is a web framework that allows developers to build lightweight web applications quickly and easily with Flask Libraries. It is another way to help beginners and professionals learn Python Flask framework which makes it one of the most popular #python-based web framework. It was developed by Armin Ronacher, leader of the International Group of Python Enthusiasts(POCCO).

### Creating a Flask Virtual Environment
> **Virtualenv is a virtual Python environment builder. It helps a user to create multiple Python environments side-by-side. Thereby, it can avoid compatibility issues between the different versions of the libraries.
You can use the Terminal or Gitbash in order to create this environment.**

**The following command installs virtualenv:**
  
  ```
pip install virtualenv
```
**Create a Python virtual environment**  
>you can give the 'venv' any name you want it to be
```
virtualenv venv
```
**Activate virtual environment for windows**
```
venv\Scripts\activate
```
**for linux** 
```
venv/bin/activate
```
We are now ready to install Flask in this environment.

**We then have to run the requirements.txt file in this repository, which will install all the required packages alongside Flask**
```
pip install -r requirements.txt
```
**To create and have the requirements.txt in your environment, you  can simple run the code below**
```
pip freeze > requirements.txt
```
> :tada: Our environment is now ready to run Flask


### To execute the script, we have to run a Flask Application using python syntax i.e python <app_name>.py
```
python test.py
```
  
**This will run the flask app server programmatically in debug mode. You should have same result as the image below**

> :information_source: **Note:**
> 
> By default, the URL for Flask is http://127.0.0.1:5000 while the endpoint for the python script is 'test'

![Flask server running](https://github.com/S-Oluwapelumi/Flask-API/assets/125037312/263ee1cf-e03c-4b7c-9019-7fb8f4483dd6)


## To ensure that the script is working and view response, we have to make use of an API testing tool. In this case, we'll use `Postman`
>**Postman is a popular tool for API testing that allows developers to create and execute HTTP requests and test API responses. Postman makes API testing more efficient and effective with features such as request builders, response visualizations, and test automation.**

**To install POSTMAN, we go to the website [Postman.com](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) and download Postman version compatible with your operating system.**


**After downloading and installing, Postman opens up it homepage by default**

### Navigate to Postman homepage
**In the homepage of Postman, naviagte to the `Workspaces` and select `My Workspace`, this should take you to the below page:**

![postman image](https://github.com/S-Oluwapelumi/Flask-API/assets/125037312/50c1403f-540e-4a12-9363-93e39c9bab39)

>Follow the numbering and instruction below using the image
1. Click on the dropdown icon and Select `POST`
2. Copy and Paste the URL below
```
http://127.0.0.1:5000/test
```
4. Click on `Body`
5. Click on `raw`
6. Click on the dropdown icon and select `JSON`
7. Copy and paste the below JSON code. _Requires 'user' and 'prompt' fields in the form data_
   ```
   {
    "prompt":"letter",
    "user":"fatima"
   }
   ```
8. Click on `Send` _this is to test the test.py script_
9. >This gives you the response and tells you if the code is running fine or not. If the code successfully runs, them it outputs `Status == 200` but if there's an invalid entry, it returns `Invalid request`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)






  
 

