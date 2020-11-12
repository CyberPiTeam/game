# python version for image
FROM python:3.8.5
# Unbuffered python output
ENV PYTHONUNBUFFERED 1

#working directory
WORKDIR /cyberpi

# add the requirements
COPY requirements.txt /cyberpi/

#install the requirements really dont know why i bothered to put one of them in a text file but wont work with out it
RUN pip3 install -r requirements.txt
RUN pip3 install --user django-crispy-forms
# Copy the current stuff into the container
COPY . /cyberpi/

#port to expose to host
EXPOSE 8000
#Runs @  start of container
CMD /cyberpi/start.sh