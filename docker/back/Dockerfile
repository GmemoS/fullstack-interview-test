FROM python:3.9

LABEL version="1.0"
LABEL org.opencontainers.image.authors="Carlos Guillermo Jimenez Salcedo"

COPY back /usr/src/git_manager/back
WORKDIR /usr/src/git_manager/back
RUN pip install pipenv
RUN pipenv install --system

RUN git clone --bare https://github.com/GmemoS/fullstack-interview-test.git /usr/src/git_manager/repo

CMD ["python", "/usr/src/git_manager/back/src/api.py"]
