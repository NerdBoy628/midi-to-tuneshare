# MIDI to TuneShare converter

This program will convert MIDI files to TuneShare codes that can be played on Scratch. [You can get TuneShare here.](https://scratch.mit.edu/projects/863714854)

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
