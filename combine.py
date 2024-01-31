from moviepy.editor import VideoFileClip, concatenate_videoclips
from data import *

class combine:
    def make_video(input_statements):

        # Create a list of video paths based on input statements
        video_paths = [r"C:\Users\91820\{}\{}".format(input_statement, input_statement) for input_statement in input_statements]
        print(video_paths)
        # Load each video clip
        video_clips = [VideoFileClip(path) for path in video_paths]

        # Concatenate video clips
        final_clip = concatenate_videoclips(video_clips, method="compose")

        # Write the compiled video to the output path
        final_clip.write_videofile(output_path, codec="libx264", fps=24)

        print(f"Compiled video saved at: {output_path}")