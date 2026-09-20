# Instagram Automated Post Generator 🚀

An end-to-end AI-powered automation pipeline that generates premium, highly technical 8-slide Instagram carousels for **@modernjavascripthub**.

This project uses the **Antigravity AI Agent** to completely automate the content creation, image generation, file organization, and version control process for an Instagram technical education page.

## ⚙️ How It Works (The 100% Autopilot Flow)

1. **The Queue (`topics_queue.json`)**: A queue of advanced JavaScript/React topics extracted from a predefined content strategy (Excel file).
2. **The Scheduler**: A local cron daemon runs every 6 hours, waking up the AI agent.
3. **The Workflow (`SKILL.md`)**: The agent follows a strict custom skill to:
   - Pop the first topic from the queue.
   - Generate an engaging, cinematic thumbnail featuring the brand's 3D avatar.
   - Generate a deeply technical 8-slide JSON script (Hook, Explanation, Code, Flow, Internals, Mistake, Better Approach, Summary).
   - Concurrently generate 8 infographic-style slide images.
4. **File Organization**: All generated images are moved into `slides/YYYY-MM-DD/<carousel_count>/`.
5. **Git Auto-Push**: The agent automatically runs `git add`, `git commit`, and `git push` via SSH to keep this remote repository synced.

## 📂 Folder Structure

```text
/
├── .agents/skills/instagram_carousel/   # Core AI custom workflow instructions
├── assets/                              # Brand assets (e.g., avatar image)
├── slides/                              # Auto-generated carousels organized by date
├── topics_queue.json                    # The active queue of upcoming topics
└── process_excel.py                     # Script used to convert raw Excel strategy to JSON
```

## 🎨 Creative Guidelines
- **Target Audience:** Intermediate/Senior JavaScript and React Developers.
- **Visual Style:** Deep navy blue, cyan/electric blue accents, cinematic lighting, futuristic developer UI.
- **Content:** Non-obvious behaviors, engine internals (V8), memory leaks, garbage collection, and real-world bugs. No basic textbook definitions.

---
*Automatically managed and maintained by the Antigravity AI Assistant.*
