---
name: instagram_carousel
description: Automates the creation of an 8-slide Instagram carousel including the thumbnail, JSON script generation, image generation, and organizing them into dated sequential folders.
---

# Instagram Carousel Generator Workflow

Use this skill whenever the user asks to "create an Instagram carousel" or "Instagram slide create karne ke liye bolu" for a specific topic.

Follow these exact steps in order:

## Step 1: Gather Information
Ask the user for the following details (in Hinglish):
- **Topic**: The main subject of the carousel.
- **Label**: Top mini-text.
- **Hook**: Main bold punchline for the thumbnail.
- **Research (Optional)**: Any specific research briefing to use for the script.

Wait for the user's response before proceeding to Step 2.

## Step 2: Generate Thumbnail Image
Use the `generate_image` tool to create the cover thumbnail (portrait 4:5, standard aspect ratio '3:4').
- **ImagePaths**: MUST include the avatar image located at `/Applications/GenAI/InstagramJavascript/assets/avatar.png`.
- **Prompt Guidelines**:
  - Must look like a professionally art-directed technology editorial thumbnail, NOT a generic Canva template.
  - Dark navy/deep blue futuristic developer environment with cyan/electric blue accents.
  - The 3D boy avatar must be an ACTIVE visual storytelling element (e.g., pointing, holding, pausing code). DO NOT just place him passively.
  - Include the exact Text: The Label, Hook, and Topic/Headline provided by the user, plus the handle `@modernjavascripthub` at the bottom.
  - Cinematic lighting, strong typography.

## Step 3: Generate JSON Script & Slide Images
1. First, based on the user's topic and research, generate the 8-slide JSON script. Focus on advanced JS/React, non-obvious behavior, simple language, no basic definitions. Ensure the JSON structure exactly matches the previously established 8-slide format (Hook, Simple Explanation, Code, Flow, Under the Hood, Common Mistake, Better Approach, Summary). Output ONLY valid JSON.
2. Immediately after outputting the JSON, use the `generate_image` tool concurrently to generate 8 slide images corresponding to the 8 slides in the JSON.
  - **Image Naming**: `slide1`, `slide2`, `slide3`, ..., `slide8`.
  - **Prompt Guidelines**: Premium tech editorial look, dark navy blue, cyan accents, visual storytelling (flow diagrams, metaphors, comparisons). NO AVATAR in these 8 slides. Ensure text and graphics match the JSON script.

## Step 4: Organize Files
Once all images (thumbnail + 8 slides) are generated in your artifact directory, move them to the project directory: `/Applications/GenAI/InstagramJavascript/slides/YYYY-MM-DD/<carousel_count>/`.

To do this, use the `run_command` tool with a bash script like this to calculate the date, count folders, and move the files:

```bash
DATE=$(date +%Y-%m-%d)
BASE_DIR="/Applications/GenAI/InstagramJavascript/slides/$DATE"
mkdir -p "$BASE_DIR"

# Calculate next carousel count
COUNT=$(ls -1d "$BASE_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')
NEXT_COUNT=$((COUNT + 1))
TARGET_DIR="$BASE_DIR/$NEXT_COUNT"
mkdir -p "$TARGET_DIR"

# Move files (taking the most recently generated ones if multiple exist)
mv $(ls -t <ARTIFACT_DIR>/*thumbnail*.jpg | head -n 1) "$TARGET_DIR/thumbnail.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide1*.jpg | head -n 1) "$TARGET_DIR/slide1.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide2*.jpg | head -n 1) "$TARGET_DIR/slide2.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide3*.jpg | head -n 1) "$TARGET_DIR/slide3.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide4*.jpg | head -n 1) "$TARGET_DIR/slide4.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide5*.jpg | head -n 1) "$TARGET_DIR/slide5.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide6*.jpg | head -n 1) "$TARGET_DIR/slide6.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide7*.jpg | head -n 1) "$TARGET_DIR/slide7.jpg"
mv $(ls -t <ARTIFACT_DIR>/*slide8*.jpg | head -n 1) "$TARGET_DIR/slide8.jpg"
```

Confirm to the user once the files have been successfully organized. Do NOT save the JSON file to the project folder.

## Step 5: Git Auto-Push
After organizing the files in Step 4, run the following git commands in the `/Applications/GenAI/InstagramJavascript/` directory to push the newly created carousel to the remote repository:
```bash
git add slides/
git commit -m "Auto-generated carousel: <Carousel_Topic_Name>"
git push
```
Inform the user once the push is successful!
