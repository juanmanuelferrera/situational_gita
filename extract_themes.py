#!/usr/bin/env python3
"""
Simple direct theme extractor and comprehensive content parser
"""

import json
import re
from pathlib import Path


def get_all_themes():
    """Manually defined list of all themes from the book"""
    return [
        "Achievements",
        "Ambition",
        "Anger",
        "Boss",
        "Brothers",
        "Children",
        "Competence",
        "Conduct",
        "Confusion",
        "Dealing with envy",
        "Death",
        "Death of a loved one",
        "Decisions",
        "Demotivated",
        "Depression",
        "Determination",
        "Discovering meaning",
        "Discriminated",
        "Existential Crisis",
        "Expectations",
        "Family",
        "Fear",
        "Feeling shameful",
        "Forgetfulness",
        "Friends",
        "God",
        "Greed",
        "Happiness",
        "Identity",
        "Illusion",
        "Knowledge",
        "Laziness",
        "Leader",
        "Life cycle",
        "Loneliness",
        "Losing hope",
        "Love",
        "Lust",
        "The Master",
        "Material World",
        "Nature",
        "Practice",
        "Practicing Forgiveness",
        "Pride",
        "Professionals",
        "Reincarnation",
        "Relation with God",
        "Repression",
        "Respect",
        "Responsibility",
        "Seeking peace",
        "Self Esteem",
        "Sons",
        "Sorrow and Regret",
        "Soul",
        "Spirituality",
        "Teacher",
        "Teams",
        "Temptation",
        "Uncontrolled mind"
    ]


def extract_comprehensive_content(text_file='situational_gita.txt'):
    """Extract all valuable content from the book"""

    with open(text_file, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    data = {
        'themes': get_all_themes(),
        'chapters': {},
        'theme_content': {}
    }

    # Extract content for each theme
    print("Extracting comprehensive content for each theme...")

    for i, theme in enumerate(data['themes'], 1):
        print(f"  {i}/{len(data['themes'])}: {theme}")

        theme_data = {
            'theme': theme,
            'sections': [],
            'full_text': []
        }

        # Find all mentions of this theme
        for line_num, line in enumerate(lines):
            if theme.lower() in line.lower():
                # Extract large context: 100 lines before and after
                start = max(0, line_num - 100)
                end = min(len(lines), line_num + 200)

                context_text = '\n'.join(lines[start:end])

                theme_data['sections'].append({
                    'line_number': line_num,
                    'context': context_text
                })

        # Also get full text for analysis
        theme_data['full_text'] = '\n\n'.join([s['context'] for s in theme_data['sections']])

        data['theme_content'][theme] = theme_data

    # Extract chapter information
    print("\nExtracting chapter content...")
    current_chapter = None
    chapter_content = []

    for line in lines:
        # Detect chapter headers
        chapter_match = re.search(r'CHAPTER\s+[IVX\d]+', line, re.IGNORECASE)
        if chapter_match:
            # Save previous chapter
            if current_chapter and chapter_content:
                data['chapters'][current_chapter] = '\n'.join(chapter_content[:500])

            current_chapter = chapter_match.group()
            chapter_content = [line]
        elif current_chapter:
            chapter_content.append(line)

    # Save last chapter
    if current_chapter and chapter_content:
        data['chapters'][current_chapter] = '\n'.join(chapter_content[:500])

    return data


def main():
    """Main extraction function"""
    print("Situational Gita - Comprehensive Content Extraction")
    print("=" * 60)

    data = extract_comprehensive_content()

    # Save to JSON
    output_file = 'comprehensive_gita_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Saved to {output_file}")
    print(f"\nSummary:")
    print(f"  Total themes: {len(data['themes'])}")
    print(f"  Total chapters: {len(data['chapters'])}")

    # Calculate average sections per theme
    avg_sections = sum(len(tc['sections']) for tc in data['theme_content'].values()) / len(data['themes'])
    print(f"  Average sections per theme: {avg_sections:.1f}")

    # Show sample
    print(f"\nFirst 10 themes:")
    for i, theme in enumerate(data['themes'][:10], 1):
        sections = len(data['theme_content'][theme]['sections'])
        print(f"  {i}. {theme} ({sections} sections)")

    print(f"\nChapters found:")
    for ch in list(data['chapters'].keys())[:5]:
        print(f"  - {ch}")

    if len(data['chapters']) > 5:
        print(f"  ... and {len(data['chapters']) - 5} more")


if __name__ == '__main__':
    main()
