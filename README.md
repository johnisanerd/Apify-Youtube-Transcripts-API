[# YouTube Transcript Getter – Priced Per Video](https://apify.com/johnvc/youtubetranscripts)

## 🎬 YouTube Transcript Getter – Priced Per Video

> **Extract YouTube transcripts effortlessly with full metadata and per‑video pricing.**

This repository provides a Python example for running the Apify Actor  
[`johnvc/youtubetranscripts`](https://apify.com/johnvc/youtubetranscripts) via the Apify Python client.
It is ideal for:

- **Content creators** who need ready‑to‑use transcripts for repurposing content.
- **SEO and marketing teams** who want full text versions of videos for indexing and analysis.
- **Researchers and developers** who need timestamped and non‑timestamped captions with language metadata.

You can run this Actor in the Apify cloud with **pay‑per‑event (per‑video) pricing**, making it very inexpensive for both single and batch use cases:  
[`YouTube Transcript Getter – Priced Per Video`](https://apify.com/johnvc/youtubetranscripts).

---

### 🚀 Quick Start

#### Prerequisites
- **Python** 3.8 or higher
- An **Apify account** and **API token**

#### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Apify-Youtube-Transcripts-API
```

#### 2. Create and activate a virtual environment (using `uv`, recommended)

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

#### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

#### 4. Configure your API token

Create a `.env` file in the project root (or copy from an example if you have one):

```bash
echo 'APIFY_API_TOKEN=your_api_token_here' > .env
```

You can get your API token from your Apify account dashboard:  
[`https://apify.com`](https://apify.com).

Alternatively, set the environment variable directly:

```bash
export APIFY_API_TOKEN="your_api_token_here"
```

On Windows (PowerShell):

```powershell
$Env:APIFY_API_TOKEN="your_api_token_here"
```

#### 5. Run the example

```bash
python youtube-transcripts-api.py
```

The script will:

- Trigger the `johnvc/youtubetranscripts` Actor on Apify.
- Wait for the run to finish and store results in an Apify dataset.
- Stream the resulting dataset records and print them to stdout.

---

## 💡 What is the `johnvc/youtubetranscripts` Actor?

The [`johnvc/youtubetranscripts`](https://apify.com/johnvc/youtubetranscripts) Actor (YouTube Transcript Getter – Priced Per Video) extracts transcripts from YouTube videos with rich metadata.  
According to the Actor documentation, it:

- Supports **regular YouTube videos**, **YouTube Shorts**, and various URL formats.
- Returns **timestamped** and **non‑timestamped** transcript variants.
- Includes **language information**, language code, and translation metadata.
- Charges **per video**, not per second, making pricing simple and predictable.  

Example minimal input for a single video:

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=p8gV_7zFN44"
}
```

For full details, pricing, and the most up‑to‑date information, see the Apify Actor page:  
[`https://apify.com/johnvc/youtubetranscripts`](https://apify.com/johnvc/youtubetranscripts).

---

## 📦 Example Input Payloads

Below are some sample inputs you can use when running the Actor directly in Apify or via API.

### Example 0: Single video

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=p8gV_7zFN44"
}
```

### Example 1: Three videos (batch)

```json
{
  "youtube_url": [
    "https://www.youtube.com/watch?v=5kcaHAuGxmY",
    "https://www.youtube.com/watch?v=p8gV_7zFN44",
    "https://www.youtube.com/watch?v=Wd_MUsNQDso"
  ]
}
```

> **Note**: The examples above are taken directly from the Actor documentation on Apify:  
> [`https://apify.com/johnvc/youtubetranscripts`](https://apify.com/johnvc/youtubetranscripts).

---

## 🔄 How the Example Script Works

The included `youtube-transcripts-api.py` script:

- Loads your `APIFY_API_TOKEN` from the environment (using `python-dotenv` if available).
- Initializes an `ApifyClient`.
- Builds a simple `run_input` payload with a `youtube_url` value.
- Calls the `johnvc/youtubetranscripts` Actor with the prepared input.
- Iterates over the resulting dataset and prints each item to the console.

You can customize the `run_input` in `youtube-transcripts-api.py` to:

- Change the **single `youtube_url` string** to a list of URLs.
- Pass **multiple `youtube_url` values** (as shown in the docs) to process several videos in one run.
- Integrate this logic into a larger application or data pipeline.

For the Apify Python client docs, see:  
[`https://docs.apify.com/sdk/python`](https://docs.apify.com/sdk/python).

---

## 🧾 Output and Export

The Actor stores results in an Apify dataset.  
From the dataset console link printed by the script (for example,  
`https://console.apify.com/storage/datasets/<DATASET_ID>`), you can:

- Inspect the transcripts for each video.
- Download them as JSON, CSV, Excel, or other supported export formats.
- Access them programmatically via the Apify Dataset API.

For more about datasets and exports, see Apify documentation:  
[`https://docs.apify.com/platform/storage/dataset`](https://docs.apify.com/platform/storage/dataset).

---

## ❤️ Made with Apify

Turn any YouTube content into structured, searchable text with the YouTube Transcripts API powered by Apify.  

Last Updated: 2025.11.27
