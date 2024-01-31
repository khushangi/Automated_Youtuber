from download import downloaded
from rearrange import *
from combine import *

def main():
    reels = downloaded.download_reels()
    print(reels)
    reels = shuffle.rearrange_statements(reels)
    print(reels)
    combine.make_video(reels)
    
    
if __name__ == "__main__":
    main()