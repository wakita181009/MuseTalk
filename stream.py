from scripts.realtime_inference import Avatar

if __name__ == "__main__":
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
    avatar.generate_frames(audio_path, fps, skip_save_images)
