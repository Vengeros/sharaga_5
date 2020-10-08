from fastapi import FastAPI, Path
from fastapi.responses import Response, FileResponse
from pydantic import FilePath
import rstr
import pathlib

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/r')
def read_root():
    return rstr.rstr('ABC', 50, 100)


@app.post('/file/{file_path}', tags=['file'])
def file(file_path: pathlib.Path = Path(..., title='Path to file')):
    print(file_path)
    return FileResponse('app/data/' + str(file_path), media_type='application/octet-stream', filename=file_path.name)


@app.get('/json')
def json():
    return {str(i): str(i) for i in range(1000)}
