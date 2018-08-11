FROM python:3

ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN apt-get update && \
    apt-get install -qq -y build-essential libpq-dev --no-install-recommends && \
    apt-get install -y curl && \
    apt-get -y autoclean && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash && \
    apt-get install -y nodejs npm && \
    apt-get autoremove -y

#RUN \
#    apt-get install nodejs npm && apt-get clean && \
#    npm install -g less && \
#    ln -s /usr/bin/nodejs /usr/bin/node

RUN npm install && npm run dev