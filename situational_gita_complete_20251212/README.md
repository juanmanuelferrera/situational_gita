# Situational Gita Article Generator

An AI-powered system for creating unique, empathetic articles about Bhagavad Gita teachings for modern life. Each article uses a different narrative structure to avoid formulaic writing.

## Features

- **12 Unique Narrative Strategies**: Each article uses a different storytelling approach (dual narrative, reverse chronology, dialogue-driven, etc.)
- **Intelligent Theme Matching**: Automatically selects the most appropriate narrative strategy for each theme
- **Style Variation System**: Varies opening hooks, pacing, and section naming to create distinct articles
- **Light of Dharma Style Guide Integration**: Follows your exact writing standards for empathetic, provocative writing
- **Hugo-Ready Output**: Articles generated with proper frontmatter for immediate publishing

## Setup

### 1. Install Dependencies

```bash
pip install anthropic
```

### 2. Set API Key

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or add to your `.bashrc`/`.zshrc`:
```bash
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Extract Themes from PDF

First, convert the PDF and extract themes:

```bash
# Convert PDF to text (already done)
pdftotext situational_gita.pdf situational_gita.txt

# Extract themes and create themes_data.json
python gita_parser.py
```

This creates `themes_data.json` with all extracted themes and content.

## Usage

### Generate a Single Article

```bash
python article_generator.py --theme "Anger"
```

The system will:
1. Select the best narrative strategy for "Anger" (likely "Single Day" approach)
2. Generate a unique article structure
3. Create the article using Claude
4. Save to `articles/anger.md`

### Generate Multiple Articles (Batch Mode)

```bash
# Generate articles for all themes
python article_generator.py --batch

# Generate first 10 themes only
python article_generator.py --batch --limit 10

# Use completely random strategies instead of theme-matched
python article_generator.py --batch --limit 5 --random-strategy
```

### Custom Output Directory

```bash
python article_generator.py --batch --output my_articles
```

## Narrative Strategies

The system uses 12 different narrative approaches:

1. **Dual Narrative**: Two parallel stories showing contrast
2. **Reverse Chronology**: Start with consequence, work backwards
3. **Observer Witness**: Told through eyes of someone watching
4. **Single Day**: Entire arc within 24 hours
5. **Dialogue-Driven**: Story told through conversations
6. **Recursive Loop**: Same scenario repeating with variations
7. **Letter/Confession**: First-person direct address
8. **Before/After**: Two snapshots separated by change
9. **Multiple Vignettes**: Several brief, distinct stories
10. **Question Investigation**: Structured around exploring a question
11. **Case Study**: Clinical examination of a pattern
12. **Seasonal Journey**: Story unfolds across seasons/time

### Theme-to-Strategy Mapping

The system intelligently matches themes to strategies:

- **Anger** → Single Day (compress intensity into 24 hours)
- **Loneliness** → Letter/Confession (intimate vulnerability)
- **Confusion** → Question Investigation (explore through inquiry)
- **Depression** → Reverse Chronology (trace the descent)
- **Ambition** → Dual Narrative (contrast approaches)
- **Boss/Leadership** → Dialogue-Driven (power through speech)
- **Habits/Laziness** → Recursive Loop (pattern repetition)
- **Family** → Multiple Vignettes (panoramic view)
- **Death/Loss** → Observer Witness (contemplative distance)

## Exploring Narrative Strategies

To see how the system selects strategies for different themes:

```bash
python narrative_strategies.py
```

This shows:
- Which strategy is chosen for each sample theme
- The tone and structure of each approach
- Opening hooks and pacing styles

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
