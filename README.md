# Situational Gita Article Generator

> Transform ancient Gita wisdom into unique, modern articles with AI-powered variety

An intelligent system that generates empathetic articles about Bhagavad Gita teachings for modern life. Each article uses a different narrative structure from a library of 12 storytelling frameworks, ensuring every piece feels fresh and engaging.

## ✨ Key Features

- **60 Life Themes**: Anger, Depression, Loneliness, Fear, Ambition, and 55 more
- **12 Narrative Strategies**: Each article uses a different storytelling approach
- **Intelligent Matching**: Themes automatically paired with suitable strategies
- **Style Compliance**: Follows Light of Dharma writing guidelines
- **Variation System**: 6,000+ possible combinations prevent repetitive writing
- **Hugo-Ready**: Articles generated with proper frontmatter
- **Two Usage Modes**: Claude Code (easy) or Standalone scripts (automation)

## 🚀 Quick Start (2 Steps)

### Option 1: Using Claude Code (Recommended - No API Key Needed!)

```bash
# 1. Extract content (first time only, takes 2-3 minutes)
python3 extract_themes.py

# 2. Generate articles by talking to Claude
# Just say: "Generate an article about Anger"
```

That's it! No API key, no costs, same quality.

### Option 2: Using Standalone Scripts (For Automation)

```bash
# 1. Install dependencies
pip3 install anthropic

# 2. Set API key
export ANTHROPIC_API_KEY='your-api-key-here'

# 3. Extract content
python3 extract_themes.py

# 4. Run interactive UI
python3 gita_ui.py
```

## 📖 Usage Examples

### Using Claude Code (Conversational)

```
You: "Generate an article about Anger"
Claude: [Generates using Single Day strategy, saves to articles/anger.md]

You: "Generate 5 articles: Depression, Loneliness, Fear, Pride, Confusion"
Claude: [Generates all 5 with different strategies]

You: "Show me which strategy would work best for Death of a loved one"
Claude: [Shows Observer Witness strategy, explains why]

You: "Generate an article about Boss using Dialogue-Driven strategy"
Claude: [Generates with specific strategy]
```

### Using Standalone Scripts

```bash
# Interactive menu (easiest)
python3 gita_ui.py

# Command line - Single article
python3 article_generator.py --theme "Anger"

# Batch generation
python3 article_generator.py --batch --limit 10

# Random strategies
python3 article_generator.py --batch --limit 5 --random-strategy
```

## 🎭 The 12 Narrative Strategies

Each article uses one of these unique storytelling approaches:

| Strategy | Description | Best For |
|----------|-------------|----------|
| **Dual Narrative** | Two parallel stories showing contrast | Ambition, Achievement |
| **Reverse Chronology** | Start with crisis, trace backwards | Depression, Grief |
| **Observer Witness** | Told through someone watching | Death, Loss |
| **Single Day** | 24-hour compressed narrative | Anger, Temptation |
| **Dialogue-Driven** | Story through conversations | Boss, Family, Teams |
| **Recursive Loop** | Pattern repeating with variations | Laziness, Habits |
| **Letter/Confession** | First-person direct address | Loneliness, Shame |
| **Before/After** | Transformation snapshots | Change, Growth |
| **Multiple Vignettes** | Several brief stories | Family, Universal themes |
| **Question Investigation** | Exploring a question | Confusion, Identity |
| **Case Study** | Clinical examination | Complex patterns |
| **Seasonal Journey** | Story across time | Spiritual journey |

**Plus**: 10 opening hooks × 5 pacing styles × 10 section naming approaches = **6,000+ variations!**

### Preview Strategies

```bash
# See all strategies and sample blueprints
python3 narrative_strategies.py

# Or ask Claude: "Show me narrative strategies for Fear"
```

## Article Structure

Each article includes:

1. **Hugo Frontmatter**
   - Title
   - Date
   - Draft status
   - Author
   - Tags
   - Description
   - (Optional) Image reference

2. **Unique Narrative Structure**
   - Creative, non-formulaic section headers
   - Varied opening hooks
   - Different pacing approaches
   - Theme-appropriate tone

3. **Required Elements** (adapted to narrative strategy)
   - Concrete modern examples
   - Bhagavad Gita verses (Prabhupada's 1972 edition)
   - Psychological explanation
   - Real-world consequences
   - Practical way forward
   - Empathetic, non-judgmental tone

## File Structure

```
situational_gita/
├── situational_gita.pdf          # Source PDF
├── situational_gita.txt          # Converted text
├── WRITING_STYLE_GUIDE.md        # Light of Dharma style guide
├── gita_parser.py                # Theme extraction
├── narrative_strategies.py       # 12 unique strategies
├── article_generator.py          # Main generator
├── themes_data.json              # Extracted themes/content
├── articles/                     # Generated articles
│   ├── anger.md
│   ├── loneliness.md
│   └── ...
└── README.md                     # This file
```

## Customization

### Add New Narrative Strategies

Edit `narrative_strategies.py` and add to `NarrativeStrategy.STRATEGIES`:

```python
'your_strategy_name': {
    'name': 'Your Strategy Name',
    'description': 'What makes this approach unique',
    'structure': [
        'Step 1',
        'Step 2',
        # ...
    ],
    'tone': 'The emotional quality',
    'opening_style': 'How to begin'
}
```

### Modify Theme-to-Strategy Matching

Edit `select_strategy_for_theme()` in `narrative_strategies.py`:

```python
elif any(word in theme_lower for word in ['your', 'keywords']):
    return NarrativeStrategy.STRATEGIES['your_strategy_name']
```

### Adjust Article Length

Edit `article_generator.py`, modify the prompt:

```python
- Length: 2,000-3,500 words  # Change to your preference
```

## Tips for Best Results

1. **Run Parser First**: Always run `gita_parser.py` before generating articles to ensure fresh theme data

2. **Review First Few Articles**: Generate 3-5 articles first, review quality, then batch process

3. **Mix Strategy Selection**: Sometimes use `--random-strategy` for unexpected combinations

4. **Edit Generated Content**: The AI creates strong drafts, but review for:
   - Accurate verse citations
   - Authenticity of examples
   - Consistency with your voice

5. **Track Which Strategies Work**: Keep notes on which narrative approaches work best for different themes

## Output Example

Generated articles will have this format:

```markdown
---
title: "When Anger Burns: A Day in the Life of Control Lost"
date: 2025-12-12T10:30:00-05:00
draft: false
author: ["Light of Dharma"]
tags: ["anger", "emotional-control", "bhagavad-gita"]
description: "Following one person through 24 hours of escalating anger, discovering how the Gita teaches transformation in the heat of emotion."
---

[Article opens with single-day narrative structure...]

## Morning: The Spark

[Story begins...]
```

## Troubleshooting

### "No module named 'anthropic'"
```bash
pip install anthropic
```

### "ANTHROPIC_API_KEY not found"
```bash
export ANTHROPIC_API_KEY='your-key'
```

### "No content found for theme"
- Run `python gita_parser.py` first to create `themes_data.json`
- Check that theme name matches exactly

### Articles feel too similar
- Use `--random-strategy` flag
- Review `narrative_strategies.py` and ensure varied strategies
- Check that section naming approaches are being used

## Development

### Test Narrative Strategies
```bash
python narrative_strategies.py
```

### Test Theme Extraction
```bash
python gita_parser.py
```

### Generate Single Test Article
```bash
python article_generator.py --theme "Anger" --output test_output
```

## License

This is a private tool for creating content based on Situational Gita and Light of Dharma style guidelines.

## Support

For issues or questions about the system, check:
1. All dependencies installed
2. API key set correctly
3. `themes_data.json` exists
4. `WRITING_STYLE_GUIDE.md` present
