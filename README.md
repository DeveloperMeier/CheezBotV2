# Pre-Requisites
- Docker
- Python 3.7
- Discord.py (installed via pip)

# Set-up
1. Create the file `.env` in the root directory with contents looking like:
```
DISCORD_TOKEN=SOME_TOKEN_VALUE_FROM_DISCORD_DEVELOPER_CONSOLE
GIPHY_TOKEN=SOME_TOKEN_VALUE_FROM_GIPHY_CONSOLE
YOUTUBE_TOKEN=SOME_TOKEN_VALUE_FROM_YOUTUBE_CONSOLE
SPOTIFY_TOKEN=SOME_TOKEN_VALUE_FROM_SPOTIFY_CONSOLE
```


# Run It
1. Option 1: [Docker]
```
docker build -t bot && docker run bot
```

2. Option 2: [Locally with Python]
```
python3 -m pip install -r requirements.txt
python3 main.py
```

# Structure

```
- db/
  -- models/
    -- server.py
    -- user.py
    -- channel.py
    -- permissions.py
- config/
  -- access.py
  -- restrictions.py
  -- whitelist.py
  -- blacklist.py
- connectors/
  -- spotify.py
  -- youtube.py
  -- giphy.py
  -- reddit.py
- commands/
  -- gif/
     -- puppy.py
     -- kitten.py
     -- boobs.py
     -- 420.py
  -- roles/
     -- gameroles.py
     -- commandroles.py
     -- roledelegation.py
- admin/
  -- access_control.py
  -- restict_access.py
- utils/
  -- send_message.py
  -- watch_message.py
  -- delete_message.py
- main.py
- .env
- requirements.txt
- Pipfile
- Pipfile.lock
```
