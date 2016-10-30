FROM python:2.7-slim

RUN \
  apt-get update && \
  apt-get install -y wget vim build-essential && \
  apt-get clean

RUN \
  pip install jieba wordcloud requests

COPY data/ /usr/local/lib/python2.7/site-packages/jieba
COPY data/extra_dict /usr/local/lib/python2.7/site-packages/jieba

WORKDIR /usr/local/lib/python2.7/site-packages/jieba

CMD ["/bin/bash"]
