#Install the OS
FROM python:3.14.0-slim-bookworm
#Create and set the current working directory for my docker container
WORKDIR /my_flask_app
#Copy the requirements.txt into my current working directory
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
#Install the commands in my requirements.txt recursively
RUN pip install --no-cache-dir -r requirements.txt
#Copy everything else
COPY . .
EXPOSE 5000
CMD ["python","-m","flask","--app","loan_prediction.py","run","--host=0.0.0.0"]
