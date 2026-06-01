# 🎬 YouTube Transcripts API: Captions and Subtitles in Clean JSON

> The efficient, reliable, and developer-friendly way to use the YouTube Transcripts API.

**Actor page:** [apify.com/johnvc/YoutubeTranscripts](https://apify.com/johnvc/YoutubeTranscripts?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/YoutubeTranscripts/input-schema](https://apify.com/johnvc/YoutubeTranscripts/input-schema?fpr=9n7kx3)

The YouTube Transcripts API extracts the transcript for one or more YouTube videos and returns clean, structured JSON. Each video comes back with a timestamped caption list (text, start, and duration), a plain-text version of the full transcript, and language metadata. It works with standard videos, Shorts, youtu.be short links, embed URLs, and mobile URLs, processes multiple URLs in parallel, and is billed per video.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Youtube-Transcripts-API.git
   cd Apify-Youtube-Transcripts-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python youtube-transcripts-api.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python youtube-transcripts-api.py
```

## Why Use This YouTube Transcripts API?

**Two transcript formats.** Each video returns a timestamped caption list and a plain-text version, so you can build interactive players or feed clean text straight into search and analysis.

**Many URL formats.** Standard videos, Shorts, youtu.be short links, embed URLs, and mobile URLs all work.

**Batch in parallel.** Pass an array of URLs and each is processed in parallel; invalid URLs are recorded as errors in the dataset without stopping the run.

**Language metadata.** Every record reports the transcript language, language code, and whether the captions were auto-generated.

**Predictable, pay-per-use pricing.** Billing is per video, not per second, with no subscription, which keeps both single and batch runs inexpensive.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can pull transcripts for you on demand.

## Features

### Core Capabilities
- **Single or batch input**: one URL as a string, or many as an array
- **Broad URL support**: standard videos, Shorts, youtu.be, embed, and mobile URLs
- **Timestamped captions** with text, start, and duration per segment
- **Plain-text transcript** as a single string
- **Per-video error handling**: invalid URLs are logged without failing the run

### Data Quality
- **Two formats per video**: timestamped and plain text
- **Language metadata**: language name, language code, and auto-generated flag
- **Video duration** in seconds
- **Success flag** on every record for easy filtering
- **Consistent JSON** shape across every video

## Usage Examples

### Single video
```json
{
  "youtube_url": "https://www.youtube.com/watch?v=aircAruvnKk"
}
```

### Multiple videos (batch)
```json
{
  "youtube_url": [
    "https://www.youtube.com/watch?v=aircAruvnKk",
    "https://youtu.be/9bZkp7q19f0",
    "https://www.youtube.com/shorts/abcdEFGhijk"
  ]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `youtube_url` | `string` or `array` | Yes | - | One YouTube URL as a string, or several as an array. Works with standard videos, Shorts, youtu.be, embed, and mobile URLs. Each URL is processed in parallel. |

## Output Format

One item per video. The transcript text below is shown as a placeholder to respect content copyright; your own run returns the actual caption text.

```json
{
  "video_id": "aircAruvnKk",
  "language": "English",
  "language_code": "en",
  "is_generated": false,
  "total_seconds": 1105.64,
  "timestamped": [
    { "text": "<caption segment text>", "start": 4.22, "duration": 1.18 }
  ],
  "non_timestamped": "<full transcript as a single plain-text string>",
  "url": "https://www.youtube.com/watch?v=aircAruvnKk",
  "timestamp": "2026-05-29T11:58:40",
  "success": true
}
```

The `timestamped` array holds one entry per caption segment with its `text`, `start`, and `duration` in seconds; `non_timestamped` is the full transcript as a single string. Language metadata (`language`, `language_code`, `is_generated`) and `total_seconds` describe the video, and `success` is `true` when a transcript was found. Invalid or unavailable URLs are returned with `success: false` and an error note instead.

---

## Use as an MCP tool

You can load the YouTube Transcripts API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the YouTube Transcripts API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the YouTube Transcripts API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the YouTube Transcripts API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/YoutubeTranscripts`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts`, using OAuth when prompted.
5. Ask Claude to run the YouTube Transcripts API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the YouTube Transcripts API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/YoutubeTranscripts`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the YouTube Transcripts API to power content repurposing, search indexing, and research with reliable, structured captions.*

Last Updated: 2026.06.02
