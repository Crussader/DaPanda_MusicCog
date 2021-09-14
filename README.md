# Music bot discord.py, made with lavalink
# Getting started
## Requirements
First you need to run a command to install `discord.py`,
```shell
pip install -U git+https://github.com/Rapptz/discord.py

```
To be able to play tracks you will need `lavalink`,
```shell
pip install -U git+https://github.com/Devoxin/Lavalink.py@dev
```
And for the menus you will need `discord-ext-menus-views`
```shell
pip install git+https://github.com/oliver-ni/discord-ext-menus-views
```
## Installation
`1` Add `music.py` and `music-config.json` to your cogs folder.<br>
`1` PLEASE NOTE: you need a bot session for the commands to work.
`2` Enable debug event by adding `enable_debug_events = True` to your client settings.<br>
`3` Add `user_id` parameter to the `music-config.json` file.

Everything else is customizable from the json file.

## Commands
- play <query> (Loads your input and adds it to the queue; If there is no playing track, then it will start playing)
- disconnect (Disconnects the bot from your voice channel and clears the queue)
- pause (Pauses playback)
- resume (Resumes playback)
- stop (Stops the currently playing track and removes all tracks from the queue)
- clear (Removes all tracks from the queue)
- skip (Skips to the next song)
- shuffle (Randomizes the current order of tracks in the queue)
- loop (Starts/Stops looping your currently playing track)
- queue (Displays the current song queue)
- current (Displays info about the current track in the queue)
- restart (Restarts the current track in the queue)
- seek <position> (Skips to the specified timestamp in the currently playing track)
- volume [volume] (Sets the player's volume; If there is not input, it will return the current value)
- remove <start> [end] (Removes all the tracks from the specified start through the specified end (if the end is not specified it will remove only one track))
- move <position> <track> (Moves the specified song to the specified position)
- nodes
- change_node (owner only)

# Features
- Multi-Node support
- Playlists support
- Only the DJ or someone that have (`manage_messages`) permission can control the player
- Buttons / Dropdowns
  
# Need Help?
[Discord Server](https://discord.gg/DNKEDurMyn)
