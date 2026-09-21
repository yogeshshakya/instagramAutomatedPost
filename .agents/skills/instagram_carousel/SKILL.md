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

IMPORTANT: Use the `ask_question` tool to ask the user whether they want to proceed in **Automate** or **Manual** mode.
- Option 1: "Automate (Save to slides/ & Push to Git)"
- Option 2: "Manual (Save to manual_slides/ & Do NOT Push)"

Wait for the user's responses (details + mode choice) before proceeding to Step 2.

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

## Step 4 & 5: Organize Files & Git Auto-Push
Once all images (thumbnail + 8 slides) are generated in your artifact directory, move them to the project directory and push to Git ONLY IF all 9 images were successfully created.

To do this, use the `run_command` tool with the following bash script. 
**IMPORTANT**: 
1. Replace `<Automate_Or_Manual>` with "Automate" or "Manual".
2. Replace `<AGENT_INSERT_CAPTION_TEXT_HERE>` with the actual formatted captions, hashtags, and SEO keywords from your generated JSON.

```bash
DATE=$(date +%Y-%m-%d)
# IMPORTANT: Replace <Automate_Or_Manual> with "Automate" or "Manual" based on user's choice
MODE="<Automate_Or_Manual>" 

if [ "$MODE" = "Manual" ]; then
    BASE_DIR="/Applications/GenAI/InstagramJavascript/manual_slides/$DATE"
else
    BASE_DIR="/Applications/GenAI/InstagramJavascript/slides/$DATE"
fi

mkdir -p "$BASE_DIR"

# Calculate next carousel count
COUNT=$(ls -1d "$BASE_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')
NEXT_COUNT=$((COUNT + 1))
TARGET_DIR="$BASE_DIR/$NEXT_COUNT"
mkdir -p "$TARGET_DIR"

# Move files (suppress errors if missing)
mv $(ls -t <ARTIFACT_DIR>/*thumbnail*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/thumbnail.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide1*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide1.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide2*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide2.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide3*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide3.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide4*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide4.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide5*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide5.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide6*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide6.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide7*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide7.jpg" 2>/dev/null || true
mv $(ls -t <ARTIFACT_DIR>/*slide8*.jpg 2>/dev/null | head -n 1) "$TARGET_DIR/slide8.jpg" 2>/dev/null || true

# Save the captions, SEO keywords, and hashtags
cat << 'EOF' > "$TARGET_DIR/caption.txt"
<AGENT_INSERT_CAPTION_TEXT_HERE>
EOF

# Validation Check: Verify all 9 images exist
IMAGE_COUNT=$(ls -1 "$TARGET_DIR"/*.jpg 2>/dev/null | wc -l | tr -d ' ')

if [ "$IMAGE_COUNT" -eq 9 ]; then
    echo "Success: All 9 images generated."
    if [ "$MODE" = "Automate" ]; then
        echo "Pushing to Git..."
        git add "$TARGET_DIR/caption.txt" slides/
        git commit -m "Auto-generated carousel: <Carousel_Topic_Name>"
        git push
    else
        echo "Manual Mode Active: Saved to manual_slides/. Skipping Git push."
    fi
else
    echo "Error: Incomplete generation ($IMAGE_COUNT/9 images). Aborting and removing incomplete folder."
    rm -rf "$TARGET_DIR"
fi
```

Inform the user about the final result (whether it was successfully pushed or if it aborted due to missing slides).
