from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def ping(host="127.0.0.1", count=1):
    command = f"ping -c {count} {host}"
    result = subprocess.run(command.split(" "), capture_output=True)
    return result
    
@app.get("/snmpwalk")
async def snmpwalk(host="127.0.0.1", community="public", version="2c"):
    command = f"snmpwalk -v {version} -c {community} {host}"
    result = subprocess.run(command.split(" "), capture_output=True)
    return result