import instaloader
from data import *

class downloaded:    
    download_files=[]
    
    def download_reels():
    
        # Create an Instaloader instance
        L = instaloader.Instaloader()

        # Load session if it exists, or create a new session
        try:
            L.load_session_from_file(insta_username)
        except instaloader.InstaloaderException:
            L.context.log_in(insta_username, input(insta_password))
            L.save_session_to_file()

        # List of Instagram reel URLs to download
        #paste your links here

        # Create full reel URLs
        full_reel_urls = ['https://www.instagram.com' + url for url in reel_urls]
        print(full_reel_urls)
        # List to store downloaded file names
        downloaded_files = []

        # Loop through the list of reel URLs and download each reel
        for reel_url in full_reel_urls:
            try:
                post = instaloader.Post.from_shortcode(L.context, reel_url.split('/')[-2])
                # Get the timestamp in the format 2023-11-19_12-00-01_UTC
                timestamp_utc = post.date_utc.strftime('%Y-%m-%d_%H-%M-%S_UTC')
                filename = f"{timestamp_utc}.mp4"
                # Save the file locally without specifying a target folder
                L.download_post(post, target=filename)
                
                downloaded_files.append(filename)
                print(f"{filename}")
                # print(f"   {post.caption}\n")
            except instaloader.exceptions.InstaloaderException as e:
                print(f"Failed to download reel: {e}")

        # Print all downloaded file names with single quotes and commas
        print("File names of all downloaded reels:")
        formatted_filenames = [f"{filename}" for filename in downloaded_files]
        return formatted_filenames
