{
  "name": "BujukkuRenameBot",
  "description": "Contact @Bujukku_Bujukku for support",
  "keywords": [
    "telegram"
  ],
  "env": {
    "WEBHOOK": {
      "description": "Dont Change",
      "value": "ANYTHING"
    },
    "TELEGRAM_BOT_TOKEN": {
      "description": "Paste your Bot Token here",
      "value": ""
    },
    "APP_ID": {
      "description": "Use your value from https://my.telegram.org",
      "value": ""
    },
    "API_HASH": {
      "description": "Use your value from https://my.telegram.org",,
      "value": ""
    },
    "REGISTERED_ACCOUNTS": {
      "description": "allow only pre-defined users to use this bot",
      "value": "1048115250"
    },
    "DEF_THUMB_NAIL_VID_S": {
      "description": "Default User Thumbnail URL",
      "required": false
    },
    "CHUNK_SIZE": {
      "description": "Chunk Size",
      "required": false
    },
    "HTTP_PROXY": {
      "description": "Proxy for Blocked areas",
      "required": false
    }
  },
  "addons": [
  ],
  "buildpacks": [{
    "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest"
  }, {
    "url": "heroku/python"
  }],
  "formation": {
    "worker": {
      "quantity": 1,
      "size": "free"
    }
  }
}