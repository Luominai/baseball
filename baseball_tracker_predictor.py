from pathlib import Path

import track_and_line as tkln

# create selections of sample videos? and offer sample frames and ball screenshot

def main():
    video_selection = input("Welcome to the Baseball Tracker and Predictor!\nWould you like to use a sample video? [y/n] ").lower()

    sample = False
    video_path = ''
    if video_selection == 'y':
        video_path = 'videos/memorial_pitch.mp4'
        sample = True
    else:

        video_path = input("Enter video file path: ")

        while not video_path[-3:] != '.mp4' or not Path(video_path).is_file():
            video_path = input("Last input was invalid\nRe-enter video path.")


    # draw and show line 
    # ball_coors = tkln.video_process(video_path)videos/pitch_02.mp4n
    if sample:
         sample = (input('Would you like to use sample frames and ball (for template matching)? [y/n] ').lower() =='y')

    if not sample: 
        start = input('Capture frames to based your prediction on.\n\ts = pause/unpause \n\td = next frame \n\tf = screenshot.\nMove the four windows until all are visable, then unpause. Would you like to start frame collection? [y/n] ')
    else: 
        start = 'y'

    if start == 'y':
        tkln.video_process(video_path, sample)

    ### add prediction here and show img  ###

    end = input('Goodbye.\nPress enter to end program. ')

    return 

main()