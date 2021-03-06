FROM alpine:3.4

ADD . /app

WORKDIR /app

ENV PACKAGES="\
  python \
  py-pip \
  uwsgi-python \
  supervisor \
  openjdk8 \
  zip \
"

RUN apk update && \
    apk add $PACKAGES && \
    pip install --upgrade pip

RUN pip install -r requirements.txt 

ENV JAVA_HOME /usr/lib/jvm/default-jvm

ENV MAVEN_VERSION 3.3.9
ENV MAVEN_HOME /usr/lib/maven
ENV PATH /usr/lib/maven/bin:$JAVA_HOME/bin:$PATH

RUN apk --no-cache add --virtual build-dependencies wget && \
    cd /tmp && \
    wget -q http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - && \
    mv /tmp/apache-maven-$MAVEN_VERSION /usr/lib/maven && \
    ln -s /usr/lib/maven/bin/mvn /usr/bin/mvn && \
    rm -rf /tmp/* && \
    apk del --purge build-dependencies 
RUN cd archetype/ &&\
    mvn install
    
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]