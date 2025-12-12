# Situational Gita Article Generator - Complete Guide

## How It Works & How to Take Full Advantage

---

## Table of Contents
1. [Overview](#overview)
2. [How the System Works](#how-the-system-works)
3. [Getting Started](#getting-started)
4. [All Available Functions](#all-available-functions)
5. [Advanced Usage](#advanced-usage)
6. [Tips for Best Results](#tips-for-best-results)
7. [Troubleshooting](#troubleshooting)

---

## Overview

This system transforms the Situational Gita book into unique, modern articles about Bhagavad Gita wisdom for everyday life. Each article uses a different narrative strategy to avoid repetitive writing.

### What Makes This System Special:

1. **12 Unique Narrative Strategies**: Each article uses a different storytelling approach
2. **Intelligent Matching**: Themes automatically paired with suitable narrative strategies
3. **AI-Powered**: Uses Claude to generate high-quality, empathetic content
4. **Style-Aware**: Follows your exact writing guidelines (Light of Dharma style)
5. **Comprehensive Content Extraction**: Pulls all relevant material from the source book
6. **Hugo-Ready Output**: Articles generated with proper frontmatter for immediate publishing

---

## How the System Works

### The Complete Pipeline:

```
1. SOURCE BOOK (PDF)
   ↓
2. TEXT EXTRACTION (pdftotext)
   ↓
3. THEME IDENTIFICATION (60 life situations)
   ↓
4. CONTENT EXTRACTION (comprehensive_gita_data.json)
   ↓
5. NARRATIVE STRATEGY SELECTION (12 different approaches)
   ↓
6. AI ARTICLE GENERATION (Claude)
   ↓
7. MARKDOWN OUTPUT (Hugo-ready articles)
```

### Components Explained:

#### 1. Theme Extraction (`extract_themes.py`)
- Identifies 60 life themes from the book
- Examples: Anger, Loneliness, Depression, Ambition, Boss, Fear, etc.
- Extracts comprehensive context for each theme

#### 2. Narrative Strategies (`narrative_strategies.py`)
- **12 unique storytelling frameworks**
- Prevents formulaic, repetitive articles
- Matches themes to appropriate strategies

**The 12 Strategies:**

1. **Dual Narrative**: Two parallel stories showing contrast
   - Best for: Comparative themes (Ambition, Achievement)

2. **Reverse Chronology**: Start with crisis, trace back
   - Best for: Heavy themes (Depression, Grief)

3. **Observer Witness**: Told through someone watching
   - Best for: Death, Loss, external situations

4. **Single Day**: 24-hour compressed narrative
   - Best for: Intense emotions (Anger, Temptation)

5. **Dialogue-Driven**: Story through conversations
   - Best for: Relationship themes (Boss, Family, Teams)

6. **Recursive Loop**: Pattern repeating with variations
   - Best for: Habitual issues (Laziness, Addiction)

7. **Letter/Confession**: First-person direct address
   - Best for: Personal struggles (Loneliness, Shame)

8. **Before/After**: Transformation snapshots
   - Best for: Change, Growth, Practice

9. **Multiple Vignettes**: Several brief stories
   - Best for: Universal themes (Family, Friends, Professionals)

10. **Question Investigation**: Exploring a question
    - Best for: Philosophical themes (Identity, Meaning, Confusion)

11. **Case Study**: Clinical examination
    - Best for: Complex patterns, Psychology

12. **Seasonal Journey**: Story across time/seasons
    - Best for: Long-term themes (Practice, Spiritual Journey)

#### 3. Style Variations (`StyleVariation` class)
Adds additional variation to each article:
- **10 different opening hooks** (mid-action, confession, sensory-rich, etc.)
- **5 pacing styles** (slow burn, rapid fire, rhythmic waves, etc.)
- **10 section naming approaches** (questions, metaphors, commands, etc.)

#### 4. Article Generator (`article_generator.py`)
- Loads full book content
- Applies narrative strategy
- Uses Claude AI to generate article
- Ensures style guide compliance
- Outputs Hugo-ready markdown

#### 5. Interactive UI (`gita_ui.py`)
- Simple menu system
- No command-line arguments needed
- Guides you through all functions

---

## Getting Started

### Prerequisites

```bash
# 1. Install Python dependencies
pip install anthropic

# 2. Get Anthropic API key from: https://console.anthropic.com/
# (You need a paid account with Claude API access)

# 3. Set API key (choose one method):

# Method A: For current session only
export ANTHROPIC_API_KEY='your-api-key-here'

# Method B: Permanent (recommended)
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### First-Time Setup

```bash
# Navigate to project directory
cd /Users/jaganat/.emacs.d/git_projects/situational_gita

# Make UI executable
chmod +x gita_ui.py

# Run the interactive UI
python3 gita_ui.py
```

### Quick Start Workflow

1. **Run UI**: `python3 gita_ui.py`

2. **Extract Content** (first time only):
   - Select option 2: "Extract comprehensive content from book"
   - Wait 2-3 minutes
   - Creates `comprehensive_gita_data.json`

3. **Generate Test Article**:
   - Select option 4: "Generate a single article"
   - Choose a theme (try "Anger" or "Loneliness")
   - Use auto-select strategy
   - Wait 1-2 minutes
   - Check `articles/` folder

4. **Review Quality**:
   - Read generated article
   - Check structure variety
   - Verify Gita citations
   - Assess tone and empathy

5. **Batch Generate** (if satisfied):
   - Select option 5: "Generate multiple articles"
   - Start with 5 articles
   - Review all before generating more

---

## All Available Functions

### Option 1: View All Themes
**What it does**: Displays all 60 life themes from the book

**When to use**:
- Browse available topics
- Choose themes for article generation
- Understand coverage

**How to use**:
```
Main Menu → 1 → Browse list → Press Enter to continue
```

### Option 2: Extract Comprehensive Content
**What it does**:
- Analyzes entire book (267KB of text)
- Finds all mentions of each theme
- Extracts large context windows (200+ lines)
- Identifies chapter references
- Saves to `comprehensive_gita_data.json`

**When to use**:
- First time setup (required)
- After updating source book
- If JSON file is missing/corrupted

**How to use**:
```
Main Menu → 2 → Confirm (y) → Wait 2-3 minutes
```

**Output**:
- `comprehensive_gita_data.json` (large file with all extracted content)
- Console shows summary statistics

**Time**: 2-3 minutes

### Option 3: Preview Narrative Strategies
**What it does**:
- Shows all 12 narrative strategies
- Explains each approach
- Generates sample blueprint for a theme

**When to use**:
- Understand how variety is created
- See which strategy fits which theme
- Learn the system's approach

**How to use**:
```
Main Menu → 3 → Browse strategies →
Optional: Generate sample blueprint for a theme
```

**Features**:
- See strategy descriptions
- View tone and style for each
- Generate blueprint showing:
  - Selected narrative strategy
  - Opening hook
  - Pacing style
  - Section naming approach
  - Complete structure outline

### Option 4: Generate Single Article
**What it does**:
- Generates one article for chosen theme
- Applies narrative strategy
- Creates Hugo-ready markdown
- Saves to `articles/` folder

**When to use**:
- Testing quality
- Generating specific article
- Learning how system works

**How to use**:
```
Main Menu → 4 → Select theme (number, 'all', or 'search') →
Choose strategy selection (auto or random) → Wait 1-2 minutes
```

**Features**:
- **Theme Selection**:
  - Enter number (1-60)
  - Type 'all' to see full list
  - Type 'search' to find by keyword

- **Strategy Selection**:
  - Auto-select (recommended): Intelligent matching
  - Random: Completely random for unexpected results

**Output**:
- Article saved to `articles/theme_name.md`
- Shows strategy used
- Displays file path

**Time**: 1-2 minutes per article

### Option 5: Generate Multiple Articles (Batch)
**What it does**:
- Generates multiple articles automatically
- Shows progress for each
- Creates summary JSON
- Saves all to `articles/` folder

**When to use**:
- After testing quality
- Bulk content creation
- Building article library

**How to use**:
```
Main Menu → 5 → Enter batch size (e.g., 5) →
Choose strategy approach → Confirm (y) → Wait
```

**Features**:
- **Batch Size**: Any number (start with 5-10)
- **Strategy Options**:
  - Auto-select: Different strategy per theme
  - Random: All random strategies

- **Progress Display**:
  - Shows current article (e.g., [3/10])
  - Displays theme being generated
  - Shows strategy being used
  - Success/failure indication

**Output**:
- Multiple .md files in `articles/`
- `articles/batch_summary.json` with results
- Success/failure statistics

**Time**: ~2 minutes per article (10 articles = ~20 minutes)

### Option 6: Setup/Change API Key
**What it does**:
- Set API key for current session
- Show how to set permanently
- Check if key is already set

**When to use**:
- First time setup
- Changing API keys
- If generation fails (invalid key)

**How to use**:
```
Main Menu → 6 → Choose option →
Either enter key or follow permanent setup instructions
```

### Option 7: Help & Documentation
**What it does**:
- Shows overview of system
- Lists features
- Explains workflow
- Provides tips

**When to use**:
- First time using
- Forgot how something works
- Quick reference

### Option 8: Exit
**What it does**: Closes the UI cleanly

---

## Advanced Usage

### Command-Line Alternative (For Experts)

If you prefer command-line over UI:

```bash
# Single article
python3 article_generator.py --theme "Anger" --output articles

# Batch with auto-select strategies
python3 article_generator.py --batch --limit 10

# Batch with random strategies
python3 article_generator.py --batch --limit 10 --random-strategy

# Custom output directory
python3 article_generator.py --batch --limit 5 --output my_folder
```

### Direct Script Access

```python
# In Python script or interactive shell
from article_generator import ArticleGenerator
from narrative_strategies import generate_article_blueprint

# Initialize generator
gen = ArticleGenerator()

# Generate article
article = gen.generate_article("Anger")
gen.save_article("Anger", article)

# Get blueprint for theme
blueprint = generate_article_blueprint("Loneliness")
print(blueprint['narrative_strategy'])  # Shows which strategy
```

### Customizing Narrative Strategies

Edit `narrative_strategies.py` to add new strategies:

```python
'your_new_strategy': {
    'name': 'Your Strategy Name',
    'description': 'What makes it unique',
    'structure': [
        'Step 1',
        'Step 2',
        # ... more steps
    ],
    'tone': 'The emotional quality',
    'opening_style': 'How to begin'
}
```

### Customizing Theme Matching

Edit `select_strategy_for_theme()` in `narrative_strategies.py`:

```python
elif any(word in theme_lower for word in ['your', 'keywords']):
    return NarrativeStrategy.STRATEGIES['your_strategy']
```

### Adjusting Article Length

Edit `article_generator.py`, line ~99:

```python
- Length: 2,000-3,500 words  # Change to your preference
```

---

## Tips for Best Results

### 1. Start Small, Scale Up
- Generate 3-5 test articles first
- Review quality carefully
- Adjust if needed
- Then batch generate

### 2. Review Generated Articles
**Check for**:
- Accurate Bhagavad Gita citations
- Proper verse numbers (e.g., 2.47)
- Empathetic tone
- Structural variety
- Modern, relatable examples

### 3. Edit Before Publishing
Articles are 90-95% ready but benefit from:
- Fact-checking verses
- Personalizing examples
- Adjusting tone if needed
- Adding your unique insights

### 4. Use Auto-Select Strategies
The intelligent matching usually works best:
- Anger → Single Day (intense 24-hour narrative)
- Loneliness → Letter/Confession (intimate vulnerability)
- Confusion → Question Investigation (philosophical exploration)

### 5. Mix It Up
Occasionally use random strategy for:
- Unexpected perspectives
- Breaking patterns
- Fresh approaches

### 6. Track What Works
Keep notes on which strategies work best for which themes. Over time you'll develop preferences.

### 7. Batch Wisely
- Start: 5 articles
- Review quality
- Next batch: 10-15
- Scale up gradually

### 8. Organize Output
Create folders for different purposes:

```bash
articles/
├── published/      # Reviewed and ready
├── drafts/         # Need editing
├── archive/        # Previous versions
└── ideas/          # Future topics
```

### 9. Monitor Costs
Claude API charges by tokens:
- ~$0.10-0.30 per article (varies)
- Monitor your Anthropic dashboard
- Set budget alerts

### 10. Maintain Quality
Every 10-20 articles:
- Review for pattern repetition
- Check if variety is maintained
- Adjust prompts if needed

---

## Troubleshooting

### Problem: "API key not found"
**Solution**:
```bash
# Check if set
echo $ANTHROPIC_API_KEY

# Set it
export ANTHROPIC_API_KEY='your-key'

# Or use UI: Main Menu → 6
```

### Problem: "No module named 'anthropic'"
**Solution**:
```bash
pip install anthropic

# Or with pip3
pip3 install anthropic
```

### Problem: Articles feel repetitive
**Solutions**:
1. Use random strategy mode
2. Edit `narrative_strategies.py` to add more variety
3. Generate in smaller batches
4. Review and adjust section naming approaches

### Problem: Generation fails/errors
**Possible causes**:
1. **Invalid API key**: Check key is correct
2. **Rate limiting**: Wait 1-2 minutes, try again
3. **Network issue**: Check internet connection
4. **Token limit**: Article might be too long

**Solutions**:
```bash
# Check API key validity
python3 -c "import os; print(os.getenv('ANTHROPIC_API_KEY'))"

# Test connection
python3 -c "from anthropic import Anthropic; client = Anthropic(); print('OK')"
```

### Problem: Missing comprehensive_gita_data.json
**Solution**:
```bash
# Run extraction
python3 gita_ui.py
# Select option 2

# Or command-line
python3 extract_themes.py
```

### Problem: Articles lack Gita content
**Possible cause**: Book text not loading properly

**Solution**:
1. Check `situational_gita.txt` exists
2. Re-extract content (option 2 in UI)
3. Verify file size: `ls -lh situational_gita.txt`

### Problem: Slow generation
**Normal speeds**:
- Single article: 1-2 minutes
- 10 articles: ~20 minutes

**If slower**:
- Check internet speed
- Anthropic API might be busy
- Try during off-peak hours

---

## Full Feature List

### Data Extraction
- ✅ PDF to text conversion
- ✅ Theme identification (60 themes)
- ✅ Comprehensive content extraction
- ✅ Large context windows (200+ lines)
- ✅ Chapter identification
- ✅ JSON export

### Narrative Variety
- ✅ 12 unique narrative strategies
- ✅ Intelligent theme-to-strategy matching
- ✅ Random strategy option
- ✅ 10 opening hook variations
- ✅ 5 pacing style options
- ✅ 10 section naming approaches
- ✅ Blueprint generation

### Article Generation
- ✅ Single article generation
- ✅ Batch generation (any size)
- ✅ Progress display
- ✅ Strategy selection (auto/random)
- ✅ Theme search
- ✅ Style guide integration
- ✅ Hugo frontmatter
- ✅ Automatic file naming
- ✅ Success tracking

### User Interface
- ✅ Interactive menu system
- ✅ No command-line args needed
- ✅ API key management
- ✅ Theme browsing
- ✅ Strategy preview
- ✅ Built-in help
- ✅ Progress indicators
- ✅ Error handling

### Output & Organization
- ✅ Markdown articles
- ✅ Hugo frontmatter (title, date, tags, description)
- ✅ Organized file structure
- ✅ Batch summary JSON
- ✅ Clear file naming

### Quality Control
- ✅ Style guide compliance
- ✅ Empathetic tone
- ✅ Active voice preference
- ✅ Varied sentence structure
- ✅ Creative section headers
- ✅ No formulaic writing
- ✅ Gita verse integration
- ✅ Modern examples

---

## Understanding the Generated Articles

### Article Structure
Each generated article follows its unique narrative strategy but contains these elements:

```markdown
---
title: "Creative, engaging title"
date: 2025-12-12T10:30:00-05:00
draft: false
author: ["Light of Dharma"]
tags: ["theme-tag", "related-tag"]
description: "Brief description for SEO/preview"
---

[Opening following narrative strategy]

## Creative Section Header 1
[Content...]

## Creative Section Header 2
[Content...]

[... more sections based on strategy ...]

[Closing with hope and practical steps]
```

### What to Look For

**Good article indicators**:
- ✅ Unique structure (not formulaic)
- ✅ Specific, named characters
- ✅ Concrete modern examples
- ✅ Accurate Gita verses with numbers
- ✅ Empathetic tone
- ✅ Creative section headers
- ✅ Practical takeaways
- ✅ Hopeful ending

**May need editing**:
- ⚠️ Generic examples (make more specific)
- ⚠️ Missing verse numbers (add them)
- ⚠️ Abstract concepts (add concrete details)
- ⚠️ Repetitive phrasing (vary language)

---

## Next Steps

1. **Run the UI**: `python3 gita_ui.py`
2. **Extract content** (option 2)
3. **Generate 3 test articles** (option 4)
4. **Review quality**
5. **Batch generate** if satisfied (option 5)
6. **Edit and publish**

---

## Support & Resources

**Files**:
- `README.md` - Quick start guide
- `COMPLETE_GUIDE.md` - This file
- `WRITING_STYLE_GUIDE.md` - Style guidelines

**Scripts**:
- `gita_ui.py` - Interactive UI (recommended)
- `article_generator.py` - Main generator
- `narrative_strategies.py` - Strategy definitions
- `extract_themes.py` - Content extraction

**Data**:
- `situational_gita.txt` - Source book
- `comprehensive_gita_data.json` - Extracted content
- `articles/` - Generated articles

---

**Happy article generation! 🙏**
