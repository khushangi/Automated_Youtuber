This project consists of two main parts: the first part involves creating a Tampermonkey script using JavaScript, and the second part involves Python scripts for downloading, rearranging, and compiling Instagram reels.

Tampermonkey Script (JavaScript):

In the initial phase of this project, I utilized Tampermonkey, a Chrome extension that allows users to run custom scripts on web pages. 
The JavaScript code, integrated into Tampermonkey, generates a button on your Instagram page. 
This button serves the purpose of enabling users to easily copy the URLs of the reels they desire.

The functionality you implemented in JavaScript provides users with a streamlined process for selecting and gathering the URLs of the Instagram reels they wish to manipulate further. 
By embedding this script into Tampermonkey, you've seamlessly integrated this feature into your browsing experience on Instagram.

Python Scripts:

The Python scripts come into play after the user has selected and copied the URLs of the desired Instagram reels. 
I have created a Python script using the Instaloader library to download these reels. (download.py)
Instaloader is a powerful tool for downloading media from Instagram profiles, and your script efficiently utilizes its capabilities to fetch the reels based on the provided URLs.

Subsequently, I've developed another Python script (rearrange.py) to rearrange the downloaded reels in a specific order according to the user's preferences. This step adds a personalized touch to the compilation process, allowing users to curate their content in a way that makes sense to them.

Finally, the last Python script (combine.py) utilizes the `moviepy.editor` library, specifically the `VideoFileClip` and `concatenate_videoclips` functions. This part of the project is responsible for merging the individual reels into a single compiled video. `VideoFileClip` helps to load each reel as a video clip, and `concatenate_videoclips` is then employed to concatenate these clips, creating a cohesive video sequence.

Project Overview:

In essence, this project provides Instagram users with an enhanced and customized experience for handling reels. 
The Tampermonkey script simplifies the process of collecting reel URLs, making it more user-friendly and accessible. 
The Python scripts take over from there, leveraging the capabilities of Instaloader to download reels, allowing users to arrange them in a specific order, and finally compiling them into a single video file.

This project has a thoughtful approach to user experience. 
By combining these technologies, a comprehensive solution is created that empowers users to have greater control over their Instagram reel content. 
