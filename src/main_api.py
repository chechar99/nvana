from fastapi import FastAPI

app = FastAPI()


@app.get("/endpoint_1")
def endpoint_1():
    return {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000}


@app.get("/endpoint_2")
def endpoint_2():
    return {'deductible': 1200, 'stop_loss': 13000, 'oop_max': 6000}


@app.get("/endpoint_3")
def endpoint_3():
    return {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 6000}
