# Sample_tracking
Prototype for sampling tracking tasks

## Prerequisites
Docker

## Setup
`docker compose -f docker-compose.yml -f docker-compose-develop.yml up --remove-orphans --force-recreate`

You may encounter an error during the first startup that is caused by the postgres db creation overhead, leading the django server to attempt connections prematurely.
This is fixed by simply restarting the compose, then it won't reoccur.


