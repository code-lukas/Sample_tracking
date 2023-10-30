FROM python:bookworm

COPY . .

RUN groupadd --gid 1000 pn && useradd --uid 1000 --gid pn --shell /bin/bash --create-home pn
RUN \
  echo "deb https://deb.nodesource.com/node_20.x bookworm main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get upgrade -yqq && \
  apt-get install -yqq nodejs yarn build-essential && \
  pip install -U pip && \
  rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
# pip packages
RUN pip install -r ./requirements.txt

EXPOSE 8080

CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:8080"]
