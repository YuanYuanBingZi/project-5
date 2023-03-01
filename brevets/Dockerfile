FROM python:3.8
LABEL maintainer="tongg@uoregon.edu"
RUN apt-get update -y
RUN pip install pymongo
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-B"]
CMD ["flask_brevets.py"]
