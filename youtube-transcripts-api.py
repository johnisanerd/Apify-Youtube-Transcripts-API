"""
Example: call the YouTube Transcripts API Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

The Actor extracts a transcript for each YouTube URL you pass, with both a
timestamped caption list and a plain-text version, plus language metadata.
Pricing is per video, so a single-video run is inexpensive.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Pass one URL as a string, or several as a list to process them in one run.
run_input = {
    "youtube_url": "https://www.youtube.com/watch?v=aircAruvnKk",
}

print(f"Fetching transcript for: {run_input['youtube_url']}")
run = client.actor("johnvc/YoutubeTranscripts").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    if not item.get("success"):
        print(f"\nFailed for {item.get('url', 'unknown URL')}: {item.get('error', 'unknown error')}")
        continue

    segments = item.get("timestamped") or []
    full_text = item.get("non_timestamped") or ""

    print(f"\nVideo:    {item.get('video_id', '')}")
    print(f"Language: {item.get('language', '')} ({item.get('language_code', '')})")
    print(f"Length:   {item.get('total_seconds', 0)} seconds")
    print(f"Captions: {len(segments)} timestamped segments")
    print(f"Transcript characters: {len(full_text)}")

    # Show a short preview of the plain-text transcript.
    preview = full_text[:200].replace("\n", " ").strip()
    if preview:
        print(f"\nPreview: {preview}...")
