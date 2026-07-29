from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import os
from auth import *
from pdf_gen import create_report
from analyzer import analyze_structure
from network import NetworkManager
from status_system import StatusSystem
from merge_core import MergeCore
from stats_monitor import StatsMonitor

app = FastAPI(title="PostScan", version="2.0")
net = NetworkManager()
status = StatusSystem()
merger = MergeCore()
stats = StatsMonitor()

class LoginReq(BaseModel): username:str; password:str
class RegReq(BaseModel): username:str; password:str
class ScanReq(BaseModel): target:str; master_key:str=""

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", encoding="utf-8") as f: return f.read()

@app.post("/api/register")
async def reg(data:RegReq): ok,msg=register_user(data.username,data.password); return {"success":ok,"message":msg}

@app.post("/api/login")
async def login(data:LoginReq): ok,msg,lvl=login_user(data.username,data.password); return {"success":ok,"message":msg,"level":lvl}

@app.post("/api/scan")
async def scan(req:ScanReq):
    level = "FULL" if verify_master_key(req.master_key) else "SCAN_ONLY"
    try:
        result = analyze_structure(req.target, full_mode=(level=="FULL"))
        status.update(scan=True)
        merger.add_source(result)
        stats.add_scan()
        filename = create_report(result)
        return {"success":True,"level":level,"data":result,"pdf":filename,"status":status.get(),"merge":merger.process(),"stats":stats.summary()}
    except Exception as e: raise HTTPException(400, str(e))

@app.get("/api/download/{filename}")
async def dl(filename:str):
    path = f"./{filename}"
    return FileResponse(path, as_attachment=True) if os.path.exists(path) else HTTPException(404,"ไม่พบไฟล์")

