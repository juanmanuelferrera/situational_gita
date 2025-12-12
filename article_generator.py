#!/usr/bin/env python3
"""
AI-Powered Article Generator for Situational Gita
Uses OpenAI/Anthropic API to generate articles following the Light of Dharma style guide
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import anthropic
from narrative_strategies import generate_article_blueprint, NarrativeStrategy


class ArticleGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with API key from environment or parameter"""
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.style_guide = self._load_style_guide()
        self.themes_data = self._load_themes_data()
        self.full_book = self._load_full_book_text()

    def _load_style_guide(self) -> str:
        """Load the writing style guide"""
        style_path = Path('WRITING_STYLE_GUIDE.md')
        if style_path.exists():
            with open(style_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def _load_themes_data(self) -> Dict:
        """Load extracted themes data"""
        themes_path = Path('comprehensive_gita_data.json')
        if themes_path.exists():
            with open(themes_path, 'r', encoding='utf-8') as f:
                return json.load(f)

        # Fallback: load themes_data.json if it exists
        fallback_path = Path('themes_data.json')
        if fallback_path.exists():
            with open(fallback_path, 'r', encoding='utf-8') as f:
                return json.load(f)

        return {}

    def _load_full_book_text(self) -> str:
        """Load the full book text for comprehensive context"""
        text_path = Path('situational_gita.txt')
        if text_path.exists():
            with open(text_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def create_article_prompt(self, theme: str, theme_content: Dict, use_random_strategy: bool = False) -> str:
        """Create the prompt for AI article generation with varied narrative strategies"""

        # Generate unique narrative blueprint for this article
        blueprint = generate_article_blueprint(theme, use_random=use_random_strategy)

        # Include relevant sections of the book (limited by token count)
        book_excerpt = self.full_book[:50000] if len(self.full_book) > 50000 else self.full_book

        prompt = f"""You are an expert writer creating articles about Bhagavad Gita teachings for modern life.

THEME: {theme}

SITUATIONAL GITA BOOK CONTENT (search this for relevant material about the theme):
{book_excerpt}

ADDITIONAL EXTRACTED CONTENT:
{json.dumps(theme_content, indent=2) if theme_content else "No pre-extracted content available"}

WRITING STYLE GUIDE TO FOLLOW:
{self.style_guide}

UNIQUE NARRATIVE BLUEPRINT FOR THIS ARTICLE:
This article should NOT follow a formulaic structure. Instead, use this specific approach:

Strategy: {blueprint['narrative_strategy']}
Description: {blueprint['description']}
Tone: {blueprint['tone']}
Opening Style: {blueprint['opening_style']}
Opening Hook: {blueprint['opening_hook']}
Pacing: {blueprint['pacing']}
Section Naming: {blueprint['section_naming_approach']}

STRUCTURE TO FOLLOW (be creative with section names):
{json.dumps(blueprint['structure'], indent=2)}

TASK:
Create a compelling, empathetic article about "{theme}" that uses THIS SPECIFIC narrative approach.

DO NOT use the standard structure you might default to. Instead:

1. Follow the narrative strategy above to create a UNIQUE structure
2. Use the specified opening hook and style
3. Name your sections creatively according to the section naming approach
4. Maintain the specified tone throughout
5. Use the pacing style indicated

CONTENT REQUIREMENTS (adapt to the narrative strategy):
- Ground everything in Gita wisdom with verses from Prabhupada's Bhagavad Gita (1972 edition)
- Include verse numbers (e.g., Bhagavad-gita 2.47)
- Use modern, concrete examples and scenarios
- Show real people facing real struggles
- Explain psychology and mechanics
- Demonstrate consequences
- Offer authentic alternative and practical path forward

CRITICAL STYLE REQUIREMENTS:
- Follow the Light of Dharma style guide exactly
- Lead with empathy, show understanding of why people struggle
- Use active voice, vivid verbs, concrete nouns
- Vary sentence length and structure
- Create creative section headers (NOT formulaic ones like "What Is It?" or "How It Plays Out")
- Length: 2,000-3,500 words
- Include Hugo frontmatter with title, date, draft status, author, tags, and description
- Quote ONLY from Srila Prabhupada's books
- No em dashes
- No cliché AI phrases like "Why This Matters"
- Be provocative but detached
- Write as if to a younger version of yourself

REMEMBER: Every article should feel structurally different. This one uses the "{blueprint['narrative_strategy']}" approach.
Make it distinctive, memorable, and true to that strategy.

OUTPUT FORMAT:
Return ONLY the complete markdown article with Hugo frontmatter.
"""

        return prompt

    def generate_article(self, theme: str, max_tokens: int = 8000, use_random_strategy: bool = False) -> str:
        """Generate an article for a specific theme using Claude"""

        theme_content = self.themes_data.get('theme_content', {}).get(theme, {})

        if not theme_content:
            print(f"Warning: No content found for theme '{theme}'")
            theme_content = {'theme': theme, 'content_sections': []}

        prompt = self.create_article_prompt(theme, theme_content, use_random_strategy)

        print(f"Generating article for theme: {theme}...")

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=max_tokens,
                temperature=1.0,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            article = message.content[0].text
            return article

        except Exception as e:
            print(f"Error generating article: {e}")
            return ""

    def save_article(self, theme: str, article: str, output_dir: str = 'articles'):
        """Save the generated article to a file"""

        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Create filename from theme
        filename = theme.lower().replace(' ', '_').replace('/', '_')
        filename = f"{filename}.md"

        filepath = output_path / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(article)

        print(f"Article saved to: {filepath}")
        return filepath

    def generate_multiple_articles(self, themes: List[str], output_dir: str = 'articles'):
        """Generate articles for multiple themes"""

        results = {}

        for i, theme in enumerate(themes, 1):
            print(f"\n{'='*60}")
            print(f"Processing {i}/{len(themes)}: {theme}")
            print('='*60)

            article = self.generate_article(theme)

            if article:
                filepath = self.save_article(theme, article, output_dir)
                results[theme] = {
                    'status': 'success',
                    'filepath': str(filepath)
                }
            else:
                results[theme] = {
                    'status': 'failed',
                    'filepath': None
                }

            # Brief pause to respect rate limits
            if i < len(themes):
                import time
                time.sleep(2)

        return results

    def batch_generate_from_themes_file(self, limit: Optional[int] = None):
        """Generate articles for all themes in themes_data.json"""

        themes = self.themes_data.get('themes', [])

        if limit:
            themes = themes[:limit]

        print(f"Generating articles for {len(themes)} themes...")

        results = self.generate_multiple_articles(themes)

        # Save results summary
        summary_path = Path('articles/generation_summary.json')
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)

        print(f"\nGeneration complete!")
        print(f"Summary saved to: {summary_path}")

        # Print statistics
        successful = sum(1 for r in results.values() if r['status'] == 'success')
        failed = len(results) - successful

        print(f"\nStatistics:")
        print(f"  Successful: {successful}")
        print(f"  Failed: {failed}")
        print(f"  Total: {len(results)}")


def main():
    """CLI interface for article generation"""
    import argparse

    parser = argparse.ArgumentParser(description='Generate Gita-based articles with varied narrative structures')
    parser.add_argument('--theme', type=str, help='Generate article for specific theme')
    parser.add_argument('--batch', action='store_true', help='Generate articles for all themes')
    parser.add_argument('--limit', type=int, help='Limit number of articles in batch mode')
    parser.add_argument('--output', type=str, default='articles', help='Output directory')
    parser.add_argument('--random-strategy', action='store_true', help='Use completely random narrative strategies instead of theme-matched')

    args = parser.parse_args()

    try:
        generator = ArticleGenerator()

        if args.theme:
            # Generate single article
            article = generator.generate_article(args.theme)
            if article:
                generator.save_article(args.theme, article, args.output)
                print("Article generated successfully!")
            else:
                print("Failed to generate article")

        elif args.batch:
            # Generate multiple articles
            generator.batch_generate_from_themes_file(limit=args.limit)

        else:
            print("Please specify --theme or --batch")
            parser.print_help()

    except ValueError as e:
        print(f"Error: {e}")
        print("Please set ANTHROPIC_API_KEY environment variable")


if __name__ == '__main__':
    main()
