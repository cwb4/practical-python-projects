"""
Using This Code Example
=========================
The code examples are provided by Yasoob Khalid to help you 
reference Practical Python Projects book. Code samples follow
PEP-0008, with exceptions made for the purposes of improving book
formatting. Example code is provided "as is".
Permissions
============
In general, you may use the code we've provided with this book in your
programs . You do not need to contact us for permission unless you're
reproducing a significant portion of the code and using it in educational
distributions. Examples:
* Writing an education program or book that uses several chunks of code from
    this course requires permission. 
* Selling or distributing a digital package from material taken from this
    book does require permission.
* Answering a question by citing this book and quoting example code does not
    require permission.
Attributions usually include the title, author, publisher and an ISBN. For
example, "Practical Python Projects, by Yasoob Khalid. Copyright 2020 Yasoob."
If you feel your use of code examples falls outside fair use of the permission
given here, please contact me at hi@yasoob.me.
"""

from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip
clip = ImageClip('website_image.png')
bg_clip = ColorClip(size=(1600,1000), color=[228, 220, 220])
scroll_speed = 180
total_duration = (clip.h - 800)/scroll_speed
fl = lambda gf,t : gf(t)[int(scroll_speed*t):int(scroll_speed*t)+800,:]
clip = clip.fl(fl, apply_to=['mask'])
video = CompositeVideoClip([bg_clip, clip.set_pos("center")])
video.duration = total_duration
video.write_videofile("movie.mp4", fps=26)
