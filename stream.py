from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from scripts.realtime_inference import Avatar

app = FastAPI()


@app.get("/video_feed")
async def video_feed():
    preparation = False
    batch_size = 4
    bbox_shift = 5
    video_path = "data/video/sun.mp4"
    audio_path = "data/audio/sun.wav"
    fps = 30
    skip_save_images = False
    avatar = Avatar(
        avatar_id="avatar_stream",
        video_path=video_path,
        bbox_shift=bbox_shift,
        batch_size=batch_size,
        preparation=preparation,
    )
    return StreamingResponse(
        avatar.generate_frames(audio_path, fps, skip_save_images),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


import uvicorn
from pyngrok import ngrok
from threading import Thread


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)


thread = Thread(target=run)
thread.start()

public_url = ngrok.connect(port="8000")
print("FastAPI public URL:", public_url)
