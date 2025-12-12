#!/usr/bin/env python3
"""
Enhanced Situational Gita Content Parser
Extracts themes AND comprehensive content for article generation
"""

import re
from pathlib import Path
from typing import Dict, List
import json


class EnhancedGitaParser:
    def __init__(self, text_file: str):
        self.text_file = Path(text_file)
        self.content = self._load_content()
        self.themes = []
        self.theme_content = {}
        self.chapters = {}

    def _load_content(self) -> str:
        """Load the text file content"""
        with open(self.text_file, 'r', encoding='utf-8') as f:
            return f.read()

    def extract_themes(self) -> List[str]:
        """Extract all themes from the document"""
        themes = []
        lines = self.content.split('\n')

        # The themes appear starting around line 374
        # They have pattern: $ or % or other special char + capitalized word
        theme_patterns = [
            r'^\d+→([A-Z][a-z]+(?:\s+[a-z]+)*)[\s]*$',  # Single capitalized words
            r'^\d+→([A-Z][a-z]+(?:\s+[A-Z]?[a-z]+)*)[\s]*$',  # Multiple words
        ]

        # Start looking from line 373
        for i in range(373, min(len(lines), 500)):
            line = lines[i]

            # Clean the line of special characters at start
            cleaned = re.sub(r'^[^\w\d\s→]+', '', line)
            cleaned = re.sub(r'^\d+→', '', cleaned).strip()

            # If we have a line that looks like a capitalized theme
            if cleaned and len(cleaned) > 2:
                # Check if it starts with capital letter
                if cleaned[0].isupper():
                    # Clean up encoding artifacts
                    cleaned = cleaned.replace('ࢥ', '')
                    cleaned = cleaned.replace('ࢳH', 'The')
                    cleaned = cleaned.replace('ࢳ', '')

                    # More aggressive cleaning
                    cleaned = re.sub(r'[^\w\s\&]', '', cleaned).strip()

                    if cleaned and len(cleaned) > 2 and not cleaned.isupper():
                        themes.append(cleaned)

        self.themes = list(dict.fromkeys(themes))  # Remove duplicates while preserving order
        return self.themes

    def extract_chapter_summaries(self) -> Dict[int, Dict]:
        """Extract chapter summaries and content"""
        chapters = {}
        lines = self.content.split('\n')

        # Find all chapter markers
        for i, line in enumerate(lines):
            # Look for CHAPTER markers
            chapter_match = re.search(r'CHAPTER\s+(\d+|[IVX]+)', line, re.IGNORECASE)
            if chapter_match:
                chapter_num = chapter_match.group(1)

                # Try to convert roman numerals or use as-is
                try:
                    if chapter_num.isdigit():
                        ch_num = int(chapter_num)
                    else:
                        # Roman to int conversion
                        roman_map = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
                                    'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
                                    'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
                                    'XVI': 16, 'XVII': 17, 'XVIII': 18}
                        ch_num = roman_map.get(chapter_num, None)

                    if ch_num:
                        # Get title (next non-empty line)
                        title = ""
                        for j in range(i+1, min(i+5, len(lines))):
                            if lines[j].strip() and not lines[j].strip().startswith('→'):
                                title = re.sub(r'^\d+→', '', lines[j]).strip()
                                break

                        # Get next 100 lines as content
                        content = '\n'.join(lines[i:min(i+100, len(lines))])

                        chapters[ch_num] = {
                            'number': ch_num,
                            'title': title,
                            'content_preview': content[:1000]
                        }
                except:
                    pass

        self.chapters = chapters
        return chapters

    def find_theme_content_comprehensive(self, theme: str) -> Dict:
        """
        Find ALL content related to a theme - much more comprehensive
        Returns chapters, verses, explanations, and context
        """
        theme_data = {
            'theme': theme,
            'occurrences': [],
            'related_chapters': [],
            'full_context': []
        }

        lines = self.content.split('\n')

        # Search for theme mentions
        theme_pattern = re.compile(rf'\b{re.escape(theme)}\b', re.IGNORECASE)

        for i, line in enumerate(lines):
            if theme_pattern.search(line):
                # Get large context window: 100 lines before and after
                start = max(0, i - 100)
                end = min(len(lines), i + 200)

                context = '\n'.join(lines[start:end])

                occurrence = {
                    'line_number': i,
                    'line_content': line,
                    'context': context,
                    'context_size': end - start
                }

                theme_data['occurrences'].append(occurrence)

        # Find which chapters mention this theme
        for ch_num, ch_data in self.chapters.items():
            if theme.lower() in ch_data.get('content_preview', '').lower():
                theme_data['related_chapters'].append(ch_num)

        return theme_data

    def extract_all_content(self) -> Dict:
        """Extract everything: themes, chapters, and comprehensive theme content"""
        print("Extracting themes...")
        themes = self.extract_themes()
        print(f"Found {len(themes)} themes")

        print("\nExtracting chapter summaries...")
        chapters = self.extract_chapter_summaries()
        print(f"Found {len(chapters)} chapters")

        print("\nExtracting comprehensive content for each theme...")
        theme_content = {}
        for i, theme in enumerate(themes, 1):
            print(f"  {i}/{len(themes)}: {theme}")
            theme_content[theme] = self.find_theme_content_comprehensive(theme)

        return {
            'themes': themes,
            'chapters': chapters,
            'theme_content': theme_content
        }

    def save_to_json(self, output_file: str = 'comprehensive_gita_data.json'):
        """Save all extracted data to JSON"""
        data = self.extract_all_content()

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\n✓ Saved comprehensive data to {output_file}")

        # Print summary
        print(f"\nSummary:")
        print(f"  Themes: {len(data['themes'])}")
        print(f"  Chapters: {len(data['chapters'])}")
        print(f"  Average occurrences per theme: {sum(len(tc['occurrences']) for tc in data['theme_content'].values()) / max(len(data['themes']), 1):.1f}")

        return output_file


def main():
    """Test the enhanced parser"""
    parser = EnhancedGitaParser('situational_gita.txt')

    # Extract and save everything
    output_file = parser.save_to_json()

    # Show sample
    if parser.themes:
        print(f"\nFirst 20 themes:")
        for i, theme in enumerate(parser.themes[:20], 1):
            print(f"  {i}. {theme}")

        if len(parser.themes) > 20:
            print(f"  ... and {len(parser.themes) - 20} more")

    # Load and show sample theme data
    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data['themes']:
        first_theme = data['themes'][0]
        theme_info = data['theme_content'][first_theme]
        print(f"\nSample data for '{first_theme}':")
        print(f"  Found in {len(theme_info['occurrences'])} places")
        print(f"  Related to {len(theme_info['related_chapters'])} chapters")
        if theme_info['occurrences']:
            print(f"  First occurrence at line {theme_info['occurrences'][0]['line_number']}")
            print(f"  Context preview (first 200 chars):")
            print(f"    {theme_info['occurrences'][0]['context'][:200]}...")


if __name__ == '__main__':
    main()
