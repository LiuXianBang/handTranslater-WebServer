import os
import pyttsx3
from fastapi import FastAPI
from fastapi.responses import FileResponse

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# rate = engine.getProperty('rate')  # 获取当前语速
engine.setProperty('rate', 100)
engine.setProperty('volume', 0.7)
if os.path.isfile('output.mp3'):
    os.remove('output.mp3')

app = FastAPI()


@app.get("/tts")
def read_item(text: str):
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    if os.path.isfile('output.mp3'):
        return FileResponse('output.mp3')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="", port=8000)
