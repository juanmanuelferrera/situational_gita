# Quick Start Guide - Situational Gita Article Generator

## The Easiest Way to Use This System

You have **two options** for using this system:

---

## Option 1: Terminal Claude Code (RECOMMENDED - EASIEST)

### Why This is Better:
- ✅ **No API key needed** - Uses Claude Code's built-in AI
- ✅ **No costs** - Included with Claude Code subscription
- ✅ **Faster setup** - No pip installs, no configuration
- ✅ **Better integration** - Direct access to files
- ✅ **Same quality** - Uses the same Claude AI

### How to Use:

1. **Open this folder in Claude Code**
   ```bash
   # You're already here!
   pwd  # Should show: .../situational_gita
   ```

2. **Run extraction once (first time only)**
   ```bash
   python3 extract_themes.py
   ```

3. **Generate articles by asking Claude directly**:

   **Example 1 - Single Article:**
   ```
   You: "Generate an article about Anger using the system we built"
   ```

   **Example 2 - Specific Strategy:**
   ```
   You: "Generate an article about Loneliness using the Letter/Confession narrative strategy"
   ```

   **Example 3 - Batch:**
   ```
   You: "Generate articles for these themes: Anger, Depression, Loneliness, Fear, Pride"
   ```

4. **Claude Code will**:
   - Read the style guide
   - Select appropriate narrative strategy
   - Access the book content
   - Generate the article
   - Save it to `articles/` folder
   - Show you the result

### Why This Works:

Claude Code has access to all the files in this folder:
- `WRITING_STYLE_GUIDE.md` - Your style rules
- `situational_gita.txt` - The book content
- `narrative_strategies.py` - The 12 strategies
- `comprehensive_gita_data.json` - Extracted content

So you can just **have a conversation** instead of running commands!

---

## Option 2: Standalone Python Scripts (For Automation)

### Why Use This:
- ⚠️ **Requires Anthropic API key** (costs money)
- ✅ **Good for automation** - Can run in background
- ✅ **Good for large batches** - Generate 100+ articles
- ✅ **Portable** - Works on any computer

### Setup:

1. **Install dependencies**
   ```bash
   pip3 install anthropic
   ```

2. **Get API key** from https://console.anthropic.com/

3. **Set API key**
   ```bash
   export ANTHROPIC_API_KEY='your-key-here'
   ```

4. **Run UI**
   ```bash
   python3 gita_ui.py
   ```

---

## Which Should You Choose?

### Use Terminal Claude Code If:
- ✅ You have Claude Code (which you do!)
- ✅ You want to generate 1-20 articles
- ✅ You want interactive, conversational workflow
- ✅ You don't want to pay for API
- ✅ You want to iterate and refine
- ✅ **YOU WANT THE EASIEST OPTION** ⭐

### Use Standalone Scripts If:
- ✅ You need to generate 50+ articles in batch
- ✅ You want to automate (cron jobs, etc.)
- ✅ You need to run on server without Claude Code
- ✅ You're okay paying for API usage

---

## Terminal Claude Code Workflow (Recommended)

### Step 1: First Time Setup (One Time)
```bash
# Extract content from book (takes 2-3 minutes)
python3 extract_themes.py
```

### Step 2: Generate Articles (Ongoing)

Just talk to Claude! Here are example conversations:

**Conversation 1:**
```
You: Generate an article about Anger

Claude: I'll generate an article about Anger using the Single Day narrative
strategy (perfect for intense emotions). Let me create this...

[Claude generates and saves the article]

Claude: ✓ Article saved to articles/anger.md
Here's a preview of the opening...
[Shows preview]

Want me to generate more articles?
```

**Conversation 2:**
```
You: Generate 5 articles using different narrative strategies for:
1. Depression
2. Loneliness
3. Confusion
4. Ambition
5. Fear

Claude: I'll generate each with a unique narrative strategy:

1. Depression - Reverse Chronology (trace the descent)
2. Loneliness - Letter/Confession (intimate vulnerability)
3. Confusion - Question Investigation (philosophical exploration)
4. Ambition - Dual Narrative (contrasting paths)
5. Fear - Single Day (compressed intensity)

Starting generation...
[Generates all 5]

All articles saved to articles/ folder!
```

**Conversation 3:**
```
You: Show me which narrative strategy would work best for "Death of a loved one"

Claude: For "Death of a loved one", the best narrative strategy is:

**Observer Witness**
- Told through eyes of someone watching
- Contemplative and witnessing tone
- Creates gentle distance while honoring emotion
- Structure focuses on compassionate observation

Would you like me to generate this article?
```

### Step 3: Review and Refine

```
You: Can you review the Anger article and make it more empathetic?

Claude: [Reviews article, makes edits, saves updated version]
✓ Updated article with more empathetic tone

You: Perfect! Now generate 10 more articles using varied strategies
```

---

## Complete Workflow Example

### Day 1: Setup (5 minutes)
```bash
# 1. Open folder in Claude Code (you're here)

# 2. Extract content
python3 extract_themes.py

# Done! Ready to generate articles
```

### Day 2: Generate Articles (Interactive)
```
You: Generate an article about Loneliness

Claude: [Generates using Letter/Confession strategy]

You: Great! Now do Depression and Fear

Claude: [Generates both]

You: Show me all available themes

Claude: [Shows all 60 themes]

You: Generate articles for the first 10 themes, using varied strategies

Claude: [Generates all 10 with different narrative approaches]
```

### Day 3: Review and Batch
```
You: I reviewed the articles. They're great!
     Generate the remaining 50 themes.

Claude: [Generates all remaining articles over ~1 hour]

You: Can you create a summary of which strategies were used for each?

Claude: [Creates summary document]
```

---

## What Claude Code Can Do That Scripts Can't

### 1. Intelligent Refinement
```
You: Make this article more provocative but still empathetic

Claude: [Adjusts tone, regenerates sections]
```

### 2. Custom Strategies
```
You: Create a new narrative strategy called "Inner Dialogue"
     where the entire article is a conversation between
     two parts of someone's mind

Claude: [Creates new strategy, generates article using it]
```

### 3. Iterative Improvement
```
You: The opening is too abstract. Make it more concrete with
     sensory details

Claude: [Rewrites opening with specific details]
```

### 4. Multi-Article Coordination
```
You: Generate 3 articles about anger, each using a different
     strategy. Then let me pick which one is best.

Claude: [Generates 3 versions, you choose, Claude continues]
```

### 5. Style Evolution
```
You: I noticed the articles are using too many questions as
     section headers. Vary this more.

Claude: [Adjusts future articles to avoid pattern]
```

---

## File Structure After Setup

```
situational_gita/
├── QUICK_START.md              ← You are here
├── COMPLETE_GUIDE.md           ← Detailed documentation
├── README.md                   ← Overview
├── WRITING_STYLE_GUIDE.md      ← Style rules
│
├── situational_gita.pdf        ← Source PDF
├── situational_gita.txt        ← Converted text
│
├── extract_themes.py           ← Extract content (run once)
├── narrative_strategies.py     ← 12 strategies
├── article_generator.py        ← Generator (for standalone)
├── gita_ui.py                  ← UI (for standalone)
│
├── comprehensive_gita_data.json ← Extracted content
│
└── articles/                   ← Generated articles
    ├── anger.md
    ├── loneliness.md
    ├── depression.md
    └── ...
```

---

## Example Commands for Claude Code

Copy and paste these into Claude Code:

### Generate Single Article
```
Generate an article about "Anger" following the narrative strategies
and style guide in this folder.
```

### Generate with Specific Strategy
```
Generate an article about "Loneliness" using the Letter/Confession
narrative strategy.
```

### Generate Multiple
```
Generate articles for these 5 themes, each with a different narrative
strategy:
1. Anger
2. Depression
3. Confusion
4. Fear
5. Pride
```

### Preview Strategy
```
What narrative strategy would work best for "Death of a loved one"?
Show me the blueprint without generating the article yet.
```

### Batch Generate
```
Generate articles for all themes related to emotions:
Anger, Fear, Depression, Loneliness, Pride, Shame, Grief
```

### Custom Request
```
Generate an article about "Dealing with a Difficult Boss" using
a combination of Dialogue-Driven and Case Study strategies.
```

---

## FAQ

### Q: Do I still need the Python scripts if I use Claude Code?
**A:** You only need `extract_themes.py` to run once. The other scripts are for standalone use.

### Q: Can I mix both approaches?
**A:** Yes! Use Claude Code for most articles, use standalone scripts for large batches.

### Q: Which is faster?
**A:** Both take ~1-2 minutes per article. Claude Code might be slightly faster due to no network calls.

### Q: Which produces better quality?
**A:** Same quality - both use the same Claude AI and same prompts.

### Q: Can I modify articles after generation?
**A:** Yes! Edit the .md files directly, or ask Claude to refine them.

### Q: How do I know which strategy was used?
**A:** Claude will tell you, or check the article structure - each strategy has a distinct pattern.

---

## Getting Started Right Now

### Absolute Simplest Path:

```bash
# 1. Extract content (first time only)
python3 extract_themes.py

# 2. Then just talk to Claude Code:
# "Generate an article about Anger"
```

That's it! 🎉

---

## Tips for Working with Claude Code

### 1. Be Specific
❌ "Make an article"
✅ "Generate an article about Anger using the Single Day narrative strategy"

### 2. Iterate
```
You: Generate article about Fear
Claude: [Generates]
You: Make the opening more vivid with sensory details
Claude: [Improves]
You: Perfect! Use this style for the next 5 articles
```

### 3. Ask for Previews
```
You: Show me the narrative strategy blueprint for Depression
     before generating the full article
```

### 4. Request Variations
```
You: Generate 3 different versions of the Loneliness article,
     each with a different strategy, then I'll pick the best one
```

### 5. Batch Smartly
```
You: Generate 5 articles, then pause so I can review quality
     before generating more
```

---

## Support

If something doesn't work:

1. **Check file exists**:
   ```bash
   ls comprehensive_gita_data.json
   ```

2. **Re-extract if needed**:
   ```bash
   python3 extract_themes.py
   ```

3. **Ask Claude**:
   ```
   "Something went wrong. Can you check what files are missing?"
   ```

---

## Ready to Start?

```bash
# Run this once:
python3 extract_themes.py

# Then talk to Claude Code:
# "Generate an article about [theme]"
```

**That's all you need!** 🚀
