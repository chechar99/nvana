# nvana

## Introduction

There is a dockerfile to run the fake API using FastAPI to run the server:

```shell script
docker-compose up -d
```

Then you can run the script:

```shell script
docker-compose exec nvana python src/script_sync.py 
```

Or you can run the tests
```shell script
docker-compose exec nvana pytest
```


This is the asynchronous version of the script:
```shell script
docker-compose exec nvana python src/script_async.py 
```