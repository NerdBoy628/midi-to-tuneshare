# MIDI to TuneShare converter

This program will convert MIDI files to TuneShare codes that can be played on Scratch. Unlike the previous version, this doesn't require using onlinesequencer. [You can use TuneShare online here.](https://scratch.mit.edu/projects/863714854)

## How to use
### Setup

1. Download `main.py`

### Running the Program
 
 1. Replace the `path` variable with the path to your MIDI file. On Mac, you can get this by right clicking on a file, holding alt (or option), and clicking "Copy as Pathname". On Windows, right click the file and click "Copy as path".
 2. The `multiplier` variable determines the accuracy of the notes. 8 is the default, but you may need to find a better value through trial and error.
 3. If you want the song to approximate tempo changes, set `tempo_changes` to `True`. This probably won't sound good though.
 4. If you want to disable any of the MIDI tracks, add them to the `disabled_tracks` list. For example, to disable tracks 5 and 7, set it to `[5,7]`
 5. Now run the script and it will copy the code to your clipboard automatically!
 6. Go into the TuneShare editor, click Import, and paste the code.

### Debugging

1. Are the notes not lined up?\
	Change the `multiplier` variable to something else. If the song is in 4/4 time this should be a multiple of 4, if it's in 3/4 time then a multiple of 3, etc. If this number is too large, then the song may not play fast enough, due to the 480 bpm limit in TuneShare.
2. Is the song not uploading?\
	This usually means there's too many notes. Try a shorter song, or open the file in a MIDI editor like [signal](signal.vercel.app) and see if you can disable or remove any tracks.
3. Is the speed/tempo not right?\
	Just change it in the song editor (Settings > Tempo)
4. Is something else weird going on?\
	Please tell me any feedback, questions, or bug reports by commenting on this Scratch project: [https://scratch.mit.edu/projects/870613190/](https://scratch.mit.edu/projects/870613190/)

### What is TuneShare?

Ok if you don't know what TuneShare is why are you here\
But anyway it's an online song maker created by [CodeGio](https://scratch.mit.edu/users/codeGIO/), where you can create and share songs online, add them to playlists, and more. It was created in Scratch, a kids programming language. The link is [https://scratch.mit.edu/projects/863714854](https://scratch.mit.edu/projects/863714854)
