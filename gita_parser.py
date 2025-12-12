#!/usr/bin/env python3
"""
Situational Gita Content Parser
Extracts thematic sections and content from the converted text file
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
import json


class GitaParser:
    def __init__(self, text_file: str):
        self.text_file = Path(text_file)
        self.content = self._load_content()
        self.themes = []
        self.theme_content = {}

    def _load_content(self) -> str:
        """Load the text file content"""
        with open(self.text_file, 'r', encoding='utf-8') as f:
            return f.read()

    def extract_themes(self) -> List[str]:
        """Extract all themes from the 'By Theme' section"""

        themes = []
        lines = self.content.split('\n')

        # Find line containing theme marker (line 373 in the text)
        # Pattern: capital letter followed by lowercase (like "Achievements", "Ambition")
        theme_pattern = r'^[\s]*\d+→([A-Z][a-zA-Z\s\&]+)[\s]*$'

        in_theme_section = False
        consecutive_empty = 0

        for i, line in enumerate(lines):
            # Look for the pattern "%\ " which appears to be "By Theme" in the encoding
            # Or find line numbers around 373-374 where themes start
            if i >= 370 and i <= 375:
                in_theme_section = True
                continue

            if in_theme_section:
                # Track consecutive empty lines - if we get too many, we've left the section
                if not line.strip():
                    consecutive_empty += 1
                    if consecutive_empty > 10:  # End of theme section
                        break
                    continue
                else:
                    consecutive_empty = 0

                # Look for theme names (capitalized words)
                match = re.match(theme_pattern, line)
                if match:
                    theme_name = match.group(1).strip()
                    # Filter out very short names and clean up
                    if theme_name and len(theme_name) > 2:
                        # Clean up any encoding artifacts
                        theme_name = theme_name.replace('ࢥ', '')
                        theme_name = theme_name.replace('ࢳH', 'The')
                        theme_name = theme_name.strip()
                        if theme_name:
                            themes.append(theme_name)

        self.themes = themes
        return themes

    def find_theme_content(self, theme: str) -> Dict[str, any]:
        """
        Find all content related to a specific theme
        Returns chapter references, verses, and explanations
        """
        theme_data = {
            'theme': theme,
            'references': [],
            'content_sections': []
        }

        # Search for the theme as a header/section
        pattern = re.compile(rf'\b{re.escape(theme)}\b', re.IGNORECASE)
        lines = self.content.split('\n')

        found_positions = []
        for i, line in enumerate(lines):
            if pattern.search(line):
                found_positions.append(i)

        # Extract content around each found position
        for pos in found_positions:
            # Get context: 50 lines before and after
            start = max(0, pos - 10)
            end = min(len(lines), pos + 100)

            section_content = '\n'.join(lines[start:end])
            theme_data['content_sections'].append({
                'position': pos,
                'context': section_content
            })

        return theme_data

    def extract_all_themes_content(self) -> Dict[str, Dict]:
        """Extract content for all themes"""
        if not self.themes:
            self.extract_themes()

        for theme in self.themes:
            self.theme_content[theme] = self.find_theme_content(theme)

        return self.theme_content

    def save_themes_to_json(self, output_file: str = 'themes_data.json'):
        """Save extracted theme data to JSON"""
        data = {
            'themes': self.themes,
            'theme_content': self.theme_content
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Saved theme data to {output_file}")

    def get_chapter_content(self, chapter_num: int) -> str:
        """Extract content for a specific chapter"""
        pattern = rf'CHAPTER\s+{chapter_num}\b'
        next_chapter_pattern = rf'CHAPTER\s+{chapter_num + 1}\b'

        chapter_match = re.search(pattern, self.content, re.IGNORECASE)
        if not chapter_match:
            return ""

        start_pos = chapter_match.start()

        # Find next chapter or end of document
        next_match = re.search(next_chapter_pattern, self.content, re.IGNORECASE)
        end_pos = next_match.start() if next_match else len(self.content)

        return self.content[start_pos:end_pos]


def main():
    """Test the parser"""
    parser = GitaParser('situational_gita.txt')

    print("Extracting themes...")
    themes = parser.extract_themes()
    print(f"\nFound {len(themes)} themes:")
    for i, theme in enumerate(themes[:20], 1):  # Show first 20
        print(f"{i}. {theme}")

    if len(themes) > 20:
        print(f"... and {len(themes) - 20} more")

    print("\nExtracting content for all themes...")
    theme_content = parser.extract_all_themes_content()

    print("\nSaving to JSON...")
    parser.save_themes_to_json()

    # Show sample content for first theme
    if themes:
        first_theme = themes[0]
        print(f"\n{'='*60}")
        print(f"Sample content for theme: {first_theme}")
        print('='*60)
        content = theme_content.get(first_theme, {})
        if content.get('content_sections'):
            print(content['content_sections'][0]['context'][:500])


if __name__ == '__main__':
    main()
