"""
YouTube Transcripts API: Strongly‑typed Apify example.

This script demonstrates how to use the Apify Actor
`johnvc/youtubetranscripts` to extract transcripts from one or more
YouTube videos and stream the structured results.

Actor docs: https://apify.com/johnvc/youtubetranscripts?fpr=9n7kx3
"""

from __future__ import annotations

import os
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

from apify_client import ApifyClient
from dotenv import load_dotenv
import rich

load_dotenv()

def main():

    # Initialize the ApifyClient with your Apify API token
    # Replace '<YOUR_API_TOKEN>' with your token.
    client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

    # Prepare the Actor input
    run_input = { "youtube_url": "https://www.youtube.com/watch?v=UMam9p487Ug" }

    # Run the Actor and wait for it to finish
    run = client.actor("johnvc/youtubetranscripts").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)

if __name__ == "__main__":
    # for run in range(1, 50):
    #    print(f"Running for {run} times")
    #    main()
    main()

