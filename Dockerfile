FROM python:3.14
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# RUN pip install fastapi[standard]
COPY ./web_app /code/web_app
# ENTRYPOINT ["fastapi", "run", "web_app/main.py"]
# CMD ["--port", "80"]
CMD ["python", "web_app/main.py"]
