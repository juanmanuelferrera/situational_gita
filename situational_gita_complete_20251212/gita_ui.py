#!/usr/bin/env python3
"""
Situational Gita Article Generator - Interactive UI
A simple, local command-line interface for all article generation functions
"""

import os
import sys
from pathlib import Path
import json
from extract_themes import get_all_themes, extract_comprehensive_content
from narrative_strategies import generate_article_blueprint, NarrativeStrategy, StyleVariation
from article_generator import ArticleGenerator


class GitaUI:
    def __init__(self):
        self.themes = get_all_themes()
        self.generator = None
        self.api_key_set = False

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')

    def print_header(self):
        """Print the UI header"""
        print("="*70)
        print(" " * 15 + "SITUATIONAL GITA ARTICLE GENERATOR")
        print("=" * 70)
        print()

    def check_api_key(self):
        """Check if API key is set"""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if api_key:
            self.api_key_set = True
            return True
        return False

    def setup_api_key(self):
        """Set up API key interactively"""
        print("\n" + "="*70)
        print("  API KEY SETUP")
        print("="*70)
        print("\nYour Anthropic API key is not set.")
        print("\nOptions:")
        print("  1. Set it for this session only")
        print("  2. Add it to your environment permanently")
        print("  3. Skip (won't be able to generate articles)")
        print()

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            api_key = input("\nEnter your Anthropic API key: ").strip()
            os.environ['ANTHROPIC_API_KEY'] = api_key
            self.api_key_set = True
            print("\n✓ API key set for this session")
            input("\nPress Enter to continue...")
            return True

        elif choice == '2':
            print("\nTo set permanently, add this to your ~/.zshrc or ~/.bashrc:")
            print("  export ANTHROPIC_API_KEY='your-api-key-here'")
            print("\nThen run: source ~/.zshrc (or ~/.bashrc)")
            input("\nPress Enter to continue...")
            return False

        return False

    def main_menu(self):
        """Display main menu and handle selection"""
        while True:
            self.clear_screen()
            self.print_header()

            # Show API key status
            if self.check_api_key():
                print("✓ API Key: Set\n")
            else:
                print("✗ API Key: Not set (required for article generation)\n")

            print("MAIN MENU:")
            print()
            print("  1. View all themes ({} total)".format(len(self.themes)))
            print("  2. Extract comprehensive content from book")
            print("  3. Preview narrative strategies")
            print("  4. Generate a single article")
            print("  5. Generate multiple articles (batch)")
            print("  6. Setup/change API key")
            print("  7. Help & Documentation")
            print("  8. Exit")
            print()

            choice = input("Select an option (1-8): ").strip()

            if choice == '1':
                self.view_themes()
            elif choice == '2':
                self.extract_content()
            elif choice == '3':
                self.preview_strategies()
            elif choice == '4':
                self.generate_single_article()
            elif choice == '5':
                self.generate_batch_articles()
            elif choice == '6':
                self.setup_api_key()
            elif choice == '7':
                self.show_help()
            elif choice == '8':
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")
                input("Press Enter to continue...")

    def view_themes(self):
        """Display all available themes"""
        self.clear_screen()
        self.print_header()

        print("ALL THEMES ({} total):".format(len(self.themes)))
        print("="*70)
        print()

        for i, theme in enumerate(self.themes, 1):
            print(f"  {i:2d}. {theme}")
            if i % 20 == 0 and i < len(self.themes):
                input("\nPress Enter to see more...")

        print()
        input("Press Enter to return to main menu...")

    def extract_content(self):
        """Extract comprehensive content from the book"""
        self.clear_screen()
        self.print_header()

        print("EXTRACT COMPREHENSIVE CONTENT")
        print("="*70)
        print()
        print("This will analyze the entire book and extract content for all themes.")
        print("This may take a few minutes...")
        print()

        proceed = input("Continue? (y/n): ").strip().lower()

        if proceed == 'y':
            print("\nExtracting... Please wait...\n")
            try:
                data = extract_comprehensive_content()

                # Save to JSON
                output_file = 'comprehensive_gita_data.json'
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                print(f"\n✓ Extraction complete!")
                print(f"✓ Saved to: {output_file}")
                print(f"\nSummary:")
                print(f"  - Themes: {len(data['themes'])}")
                print(f"  - Chapters: {len(data['chapters'])}")

            except Exception as e:
                print(f"\n✗ Error: {e}")

        print()
        input("Press Enter to return to main menu...")

    def preview_strategies(self):
        """Preview available narrative strategies"""
        self.clear_screen()
        self.print_header()

        print("NARRATIVE STRATEGIES")
        print("="*70)
        print()
        print("These are the different storytelling approaches used to create varied articles:")
        print()

        strategies = NarrativeStrategy.get_all_strategies()

        for i, (key, strategy) in enumerate(strategies.items(), 1):
            print(f"{i}. {strategy['name']}")
            print(f"   {strategy['description']}")
            print(f"   Tone: {strategy['tone']}")
            print()

            if i % 5 == 0 and i < len(strategies):
                input("Press Enter to see more...")

        print("\nWould you like to see a sample blueprint for a theme?")
        choice = input("(y/n): ").strip().lower()

        if choice == 'y':
            print("\nAvailable themes (first 10):")
            for i, theme in enumerate(self.themes[:10], 1):
                print(f"  {i}. {theme}")

            theme_idx = input("\nSelect theme number (1-10): ").strip()
            try:
                theme = self.themes[int(theme_idx) - 1]
                blueprint = generate_article_blueprint(theme)

                print(f"\n{'='*70}")
                print(f"BLUEPRINT FOR: {theme}")
                print('='*70)
                print(f"\nStrategy: {blueprint['narrative_strategy']}")
                print(f"Tone: {blueprint['tone']}")
                print(f"Opening: {blueprint['opening_style']}")
                print(f"Hook: {blueprint['opening_hook']}")
                print(f"Pacing: {blueprint['pacing']}")
                print(f"\nStructure:")
                for i, step in enumerate(blueprint['structure'], 1):
                    print(f"  {i}. {step}")

            except (ValueError, IndexError):
                print("\nInvalid selection")

        print()
        input("\nPress Enter to return to main menu...")

    def generate_single_article(self):
        """Generate a single article"""
        self.clear_screen()
        self.print_header()

        if not self.api_key_set:
            print("✗ API key required for article generation")
            print()
            if not self.setup_api_key():
                return

        print("GENERATE SINGLE ARTICLE")
        print("="*70)
        print()

        # Show themes
        print("Available themes (showing first 20):")
        for i, theme in enumerate(self.themes[:20], 1):
            print(f"  {i:2d}. {theme}")

        if len(self.themes) > 20:
            print(f"  ... and {len(self.themes) - 20} more")

        print()
        print("Options:")
        print("  - Enter a number (1-{})".format(len(self.themes)))
        print("  - Type 'all' to see all themes")
        print("  - Type 'search' to search for a theme")
        print()

        choice = input("Your choice: ").strip().lower()

        selected_theme = None

        if choice == 'all':
            self.view_themes()
            return self.generate_single_article()

        elif choice == 'search':
            search_term = input("\nSearch for: ").strip().lower()
            matches = [t for t in self.themes if search_term in t.lower()]
            if matches:
                print(f"\nFound {len(matches)} matches:")
                for i, theme in enumerate(matches, 1):
                    print(f"  {i}. {theme}")
                idx = input("\nSelect number: ").strip()
                try:
                    selected_theme = matches[int(idx) - 1]
                except (ValueError, IndexError):
                    print("Invalid selection")
                    input("Press Enter to continue...")
                    return
            else:
                print("\nNo matches found")
                input("Press Enter to continue...")
                return

        else:
            try:
                idx = int(choice)
                selected_theme = self.themes[idx - 1]
            except (ValueError, IndexError):
                print("\nInvalid selection")
                input("Press Enter to continue...")
                return

        if selected_theme:
            print(f"\n{'='*70}")
            print(f"GENERATING ARTICLE FOR: {selected_theme}")
            print('='*70)

            # Strategy selection
            print("\nStrategy selection:")
            print("  1. Auto-select (recommended)")
            print("  2. Random strategy")
            print()

            strategy_choice = input("Choose (1-2): ").strip()
            use_random = (strategy_choice == '2')

            # Generate blueprint
            blueprint = generate_article_blueprint(selected_theme, use_random=use_random)
            print(f"\nUsing strategy: {blueprint['narrative_strategy']}")
            print(f"Tone: {blueprint['tone']}")

            print("\nGenerating article... This may take 1-2 minutes...\n")

            try:
                if not self.generator:
                    self.generator = ArticleGenerator()

                article = self.generator.generate_article(selected_theme, use_random_strategy=use_random)

                if article:
                    filepath = self.generator.save_article(selected_theme, article)
                    print(f"\n✓ Article generated successfully!")
                    print(f"✓ Saved to: {filepath}")
                else:
                    print("\n✗ Failed to generate article")

            except Exception as e:
                print(f"\n✗ Error: {e}")

        print()
        input("Press Enter to return to main menu...")

    def generate_batch_articles(self):
        """Generate multiple articles in batch"""
        self.clear_screen()
        self.print_header()

        if not self.api_key_set:
            print("✗ API key required for article generation")
            print()
            if not self.setup_api_key():
                return

        print("BATCH ARTICLE GENERATION")
        print("="*70)
        print()
        print("Generate multiple articles automatically.")
        print(f"Total themes available: {len(self.themes)}")
        print()

        # Batch size
        batch_size = input("How many articles to generate? (default: 5): ").strip()
        try:
            batch_size = int(batch_size) if batch_size else 5
        except ValueError:
            batch_size = 5

        batch_size = min(batch_size, len(self.themes))

        # Strategy selection
        print("\nStrategy selection:")
        print("  1. Auto-select for each theme (recommended)")
        print("  2. Random strategies")
        print()

        strategy_choice = input("Choose (1-2): ").strip()
        use_random = (strategy_choice == '2')

        print(f"\n{'='*70}")
        print(f"GENERATING {batch_size} ARTICLES")
        print('='*70)
        print("\nThis will take several minutes. Progress will be shown below...")
        print()

        proceed = input("Continue? (y/n): ").strip().lower()

        if proceed == 'y':
            try:
                if not self.generator:
                    self.generator = ArticleGenerator()

                themes_to_generate = self.themes[:batch_size]
                results = {}

                for i, theme in enumerate(themes_to_generate, 1):
                    print(f"\n[{i}/{batch_size}] Generating: {theme}")

                    blueprint = generate_article_blueprint(theme, use_random=use_random)
                    print(f"  Strategy: {blueprint['narrative_strategy']}")

                    article = self.generator.generate_article(theme, use_random_strategy=use_random)

                    if article:
                        filepath = self.generator.save_article(theme, article)
                        results[theme] = {'status': 'success', 'file': str(filepath)}
                        print(f"  ✓ Saved to: {filepath}")
                    else:
                        results[theme] = {'status': 'failed'}
                        print(f"  ✗ Failed")

                    # Small delay
                    import time
                    time.sleep(2)

                # Summary
                successful = sum(1 for r in results.values() if r['status'] == 'success')
                print(f"\n{'='*70}")
                print("BATCH GENERATION COMPLETE")
                print('='*70)
                print(f"\nSuccessful: {successful}/{batch_size}")
                print(f"Failed: {batch_size - successful}/{batch_size}")

                # Save summary
                summary_file = 'articles/batch_summary.json'
                Path('articles').mkdir(exist_ok=True)
                with open(summary_file, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"\nSummary saved to: {summary_file}")

            except Exception as e:
                print(f"\n✗ Error: {e}")

        print()
        input("\nPress Enter to return to main menu...")

    def show_help(self):
        """Show help and documentation"""
        self.clear_screen()
        self.print_header()

        print("HELP & DOCUMENTATION")
        print("="*70)
        print()
        print("OVERVIEW:")
        print("  This tool generates unique articles about Bhagavad Gita teachings")
        print("  for modern life situations using AI and varied narrative strategies.")
        print()
        print("FEATURES:")
        print("  • 60 themes covering life situations (anger, loneliness, etc.)")
        print("  • 12 unique narrative strategies (avoid formulaic writing)")
        print("  • Intelligent theme-to-strategy matching")
        print("  • Light of Dharma writing style (empathetic, provocative)")
        print("  • Hugo-ready markdown with frontmatter")
        print()
        print("REQUIREMENTS:")
        print("  • Anthropic API key (for Claude AI)")
        print("  • Python 3.7+")
        print("  • anthropic package (pip install anthropic)")
        print()
        print("WORKFLOW:")
        print("  1. Extract content from book (option 2) - one time only")
        print("  2. Generate articles (options 4 or 5)")
        print("  3. Review and edit generated articles in 'articles/' folder")
        print()
        print("FILES:")
        print("  • situational_gita.txt - Source book text")
        print("  • WRITING_STYLE_GUIDE.md - Style guide to follow")
        print("  • comprehensive_gita_data.json - Extracted content")
        print("  • articles/ - Generated articles")
        print()
        print("TIPS:")
        print("  • Start with 3-5 articles to test quality")
        print("  • Review generated articles for accuracy")
        print("  • Auto-select strategy usually works best")
        print("  • Each article takes ~1-2 minutes to generate")
        print()

        input("Press Enter to return to main menu...")


def main():
    """Main entry point"""
    ui = GitaUI()
    ui.main_menu()


if __name__ == '__main__':
    main()
