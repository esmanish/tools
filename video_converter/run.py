import moviepy.editor as moviepy
clip = moviepy.VideoFileClip("video.mov") #include location of your video with it's extension here.
clip.write_videofile("output.mp4") # output video name and the extension to which you want to convert your video.
