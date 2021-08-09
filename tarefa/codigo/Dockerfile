
FROM centos/python-36-centos7

COPY . /codigo

WORKDIR /codigo


RUN pip install uvicorn 
RUN pip install pandas
RUN pip install fastapi 
RUN pip install sklearn

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
