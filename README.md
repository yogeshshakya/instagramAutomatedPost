# Instagram Automated Post Generator 🚀

An end-to-end AI-powered automation pipeline that generates and publishes premium, highly technical 8-slide Instagram carousels for **@modernjavascripthub**.

This project uses the **Antigravity AI Agent** for content creation/design, and **GitHub Actions** for headless publishing to Instagram.

## ⚙️ How It Works (The 100% Autopilot Flow)

1. **The Queue (`topics_queue.json`)**: A queue of advanced JavaScript/React topics extracted from a predefined content strategy.
2. **The Scheduler**: A local cron daemon runs every 6 hours, waking up the AI agent.
3. **The Workflow (`SKILL.md`)**: The agent follows a strict custom skill to:
   - Pop the first topic from the queue.
   - Generate an engaging, cinematic thumbnail featuring the brand's 3D avatar.
   - Generate a deeply technical 8-slide JSON script.
   - Concurrently generate 8 edge-to-edge, infographic-style slide images (no fake UI or letterboxing).
   - Format a highly structured `caption.txt` (Short Intro -> Bullet Points -> SEO -> Hashtags).
4. **File Organization & Pushing**: All files are saved into `slides/YYYY-MM-DD/<carousel_count>/`. The agent automatically commits and pushes this folder to GitHub.
5. **GitHub Actions Publishing**: As soon as the `caption.txt` file hits the `main` branch, the `.github/workflows/autopost.yml` Action wakes up, pulls the images, and safely publishes the carousel directly to Instagram using secure repository secrets.

## 🕹️ Manual vs Automate Modes

When triggering the AI manually via chat, you can choose:
- **Automate Mode**: Saves to `slides/` and pushes to Git, which **automatically publishes** the post to Instagram via GitHub Actions.
- **Manual Mode**: Saves to `manual_slides/`. These are safely pushed to Git as a backup, but **will NOT trigger** the Instagram publisher. 

*Note: You can also manually trigger the publishing of the latest auto-generated folder by going to the GitHub **Actions** tab, selecting "Auto-Post to Instagram", and clicking **Run workflow**.*

## 🔑 Required GitHub Secrets

To enable auto-posting, the following secrets must be set in **Settings > Secrets and variables > Actions**:
- `IG_ACCESS_TOKEN` (Required)
- `IG_BUSINESS_ID` (Required)
- `TELEGRAM_BOT_TOKEN` (Required - Use "dummy" to bypass)
- `TELEGRAM_CHAT` (Required - Use "dummy" to bypass)
- `FB_PAGE_ID` (Optional)
- `FB_PAGE_TOKEN` (Optional)

## 📂 Folder Structure

```text
/
├── .agents/skills/instagram_carousel/   # Core AI custom workflow instructions
├── .github/workflows/autopost.yml       # GitHub Action for publishing to Instagram
├── assets/                              # Brand assets (e.g., avatar image)
├── slides/                              # Auto-generated carousels (Triggers publishing)
├── manual_slides/                       # Manual carousels (Backed up, NOT published)
├── scripts/post.py                      # Python script executed by GitHub Actions
├── topics_queue.json                    # The active queue of upcoming topics
└── process_excel.py                     # Script used to convert raw Excel strategy to JSON
```

## 🎨 Creative Guidelines
- **Target Audience:** Intermediate/Senior JavaScript and React Developers.
- **Visual Style:** Deep navy blue, cyan/electric blue accents, cinematic lighting, edge-to-edge futuristic developer UI.
- **Content:** Non-obvious behaviors, engine internals (V8), memory leaks, garbage collection, and real-world bugs. No basic textbook definitions.

---
*Automatically managed and maintained by the Antigravity AI Assistant.*
