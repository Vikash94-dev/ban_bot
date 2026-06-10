<div align="center">
  <h2>🎵 iTunes Music Assistant (Disguised Mass-Ban Bot) 🎵</h2>
  <p>A highly customized Telegram bot designed to secretly ban all non-admin members under the guise of a music player assistant.</p>
</div>

---

### ⚠️ Warning
This bot will **immediately ban all regular members** in the group when triggered. There is no confirmation prompt. Ensure you only use it in groups where you intend to perform a mass-ban.

### ⚙️ Preconditions  
+ The bot **must** be an Admin with "Ban members" privileges.
+ That's it! Any user in the group can trigger the command.

### 🚀 Usage 
1. Send `/play` (or `/fusrodah`) in the chat.
2. The bot will immediately reply with a deceptive message: 
   > *"Hold on a moment... Inviting 𝙞𝙏𝙪𝙣𝙚𝙨 ✕ 𝙈𝙪𝙨𝙞𝙘™ ♪ assistant to your chat."*
3. The bot will completely silently ban all non-admin members in the background using a high-speed, concurrent batching system designed to bypass rate limits.
4. Once finished, the message will quietly update to *"Task completed."*

### 🛠 Configuration
Create a `.env` file in the root directory (or set up Environment Variables/Secrets on your hosting platform) with your Telegram credentials:
```ini
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```

### 🌍 Deployment & 24/7 Uptime
This bot includes a built-in Flask web server (`keep_alive.py`), allowing it to stay awake 24/7 on modern free hosting platforms like [Render.com](https://render.com).

1. Deploy the code to your chosen platform (e.g., Render, Replit, Fly.io).
2. The platform will automatically install dependencies from `requirements.txt`.
3. The start command is: `python bot.py`
4. Copy your web app's live URL and use a free pinging service like [UptimeRobot](https://uptimerobot.com) to ping the URL every 5 minutes. This will prevent your bot from ever going to sleep!
