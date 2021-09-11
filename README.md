# Music bot discord.py, made with lavalink

# Requirements
First you need to run a command to install discord.py,
```shell
pip install -U git+https://github.com/Devoxin/Lavalink.py@dev
```
Then you need to run a command to install lavalink,
```shell
python3.8 -m pip install -U git+https://github.com/Rapptz/discord.py
```
# Getting start
`1` Add all of the files to your cogs folder <br>
`2` Enable debug event by adding `enable_debug_events = True` to your client settings

# Commands
- play <query> (Loads your input and adds it to the queue; If there is no playing track, then it will start playing)
- disconnect (Disconnects the bot from your voice channel and clears the queue)
- pause (Pauses playback)
- resume (Resumes playback)
- stop (Stops the currently playing track and removes all tracks from the queue)
- clear (Removes all tracks from the queue)
- skip (Skips to the next song)
- shuffle (Randomizes the current order of tracks in the queue)
-loop (Starts/Stops looping your currently playing track)
