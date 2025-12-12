#!/usr/bin/env python3
"""
Narrative Strategy System
Provides diverse storytelling approaches to prevent formulaic article structure
"""

import random
from typing import Dict, List


class NarrativeStrategy:
    """Defines different approaches to article structure and storytelling"""

    STRATEGIES = {
        'dual_narrative': {
            'name': 'Dual Narrative',
            'description': 'Two parallel stories showing contrast',
            'structure': [
                'Open with Person A facing the challenge',
                'Introduce Person B facing same challenge differently',
                'Weave between both stories showing contrasting approaches',
                'Define the pattern through their diverging paths',
                'Show consequences for both',
                'Gita wisdom explaining why one path works',
                'Practical synthesis of lessons'
            ],
            'tone': 'Comparative and observational',
            'opening_style': 'Split screen - two lives, same problem, different responses'
        },

        'reverse_chronology': {
            'name': 'Reverse Chronology',
            'description': 'Start with the consequence, work backwards',
            'structure': [
                'Open with the crisis moment or consequence',
                'Flash back: how did we get here?',
                'Reveal the pattern through reverse investigation',
                'Show the critical turning point',
                'Present Gita wisdom as the missing piece',
                'Forward movement: the path not taken',
                'Resolution with alternate timeline vision'
            ],
            'tone': 'Investigative and revelatory',
            'opening_style': 'Start at the breaking point, then trace the crack'
        },

        'observer_witness': {
            'name': 'Observer Witness',
            'description': 'Told through eyes of someone watching',
            'structure': [
                'Narrator observes someone struggling',
                'Multiple scenes of the pattern manifesting',
                'Observer\'s growing understanding',
                'Define pattern through observation',
                'Gita wisdom as observer\'s realization',
                'Observer acts or speaks',
                'Resolution showing ripple effect'
            ],
            'tone': 'Contemplative and witnessing',
            'opening_style': 'Watch through another\'s eyes, notice what they notice'
        },

        'single_day': {
            'name': 'Single Day',
            'description': 'Entire arc happens within 24 hours',
            'structure': [
                'Morning: the pattern begins',
                'Midday: escalation and crisis',
                'Afternoon: the moment of choice',
                'Evening: consequences unfold',
                'Gita wisdom woven throughout as internal dialogue',
                'Night: reflection and realization',
                'Dawn: new beginning or deepening trap'
            ],
            'tone': 'Intimate and immediate',
            'opening_style': 'Compress time, intensify focus, one pivotal day'
        },

        'dialogue_driven': {
            'name': 'Dialogue-Driven',
            'description': 'Story told primarily through conversation',
            'structure': [
                'Open with a critical conversation',
                'Define pattern through what people say vs mean',
                'Series of conversations showing progression',
                'The conversation that reveals truth',
                'Gita verses as dialogue between Krishna-Arjuna',
                'The difficult conversation needed',
                'Resolution through authentic communication'
            ],
            'tone': 'Dynamic and interpersonal',
            'opening_style': 'Let speech reveal character, truth emerge through exchange'
        },

        'recursive_loop': {
            'name': 'Recursive Loop',
            'description': 'Same scenario repeating with variations',
            'structure': [
                'Scene 1: the pattern plays out',
                'Scene 2: same pattern, different context',
                'Scene 3: pattern intensifies',
                'Recognition: the loop becomes visible',
                'Define pattern through repetition',
                'Gita wisdom as the loop-breaker',
                'Scene 4: breaking the cycle'
            ],
            'tone': 'Rhythmic and revelatory',
            'opening_style': 'Repetition reveals pattern, pattern reveals prison'
        },

        'letter_confession': {
            'name': 'Letter/Confession',
            'description': 'First-person direct address',
            'structure': [
                'Open with direct address: "Dear Friend..." or "I need to tell you..."',
                'Personal confession of the struggle',
                'Stories from the confession',
                'Define pattern through self-recognition',
                'Gita wisdom as discovered truth',
                'What I learned',
                'What I hope for you'
            ],
            'tone': 'Intimate and vulnerable',
            'opening_style': 'Break fourth wall, speak directly, make it personal'
        },

        'before_after': {
            'name': 'Before/After Transformation',
            'description': 'Two snapshots separated by change',
            'structure': [
                'Before: vivid portrait of life in the pattern',
                'The catalyst: what sparked change',
                'Define the pattern from hindsight',
                'The struggle to change',
                'Gita wisdom as the guide',
                'After: life transformed',
                'The ongoing work'
            ],
            'tone': 'Hopeful and testimonial',
            'opening_style': 'Show the transformation, then explain the journey'
        },

        'multiple_vignettes': {
            'name': 'Multiple Vignettes',
            'description': 'Several brief, distinct stories',
            'structure': [
                'Vignette 1: workplace manifestation',
                'Vignette 2: family manifestation',
                'Vignette 3: spiritual practice manifestation',
                'Vignette 4: relationship manifestation',
                'Connect the dots: define the universal pattern',
                'Gita wisdom addressing the core',
                'Universal application'
            ],
            'tone': 'Panoramic and interconnected',
            'opening_style': 'Multiple angles, same truth, mosaic of meaning'
        },

        'question_investigation': {
            'name': 'Question Investigation',
            'description': 'Article structured around exploring a question',
            'structure': [
                'Open with the question that haunts',
                'First attempted answer (insufficient)',
                'Story revealing complexity',
                'Second attempted answer (closer)',
                'Define pattern through investigation',
                'Gita wisdom as the answer',
                'Living the answer'
            ],
            'tone': 'Philosophical and searching',
            'opening_style': 'Chase a question, find unexpected answers'
        },

        'case_study': {
            'name': 'Case Study Analysis',
            'description': 'Clinical examination of a pattern',
            'structure': [
                'Present the case',
                'Initial observations',
                'Detailed analysis of symptoms',
                'Diagnosis: define the pattern',
                'Etiology: why it develops',
                'Gita wisdom as treatment',
                'Prognosis and prescription'
            ],
            'tone': 'Analytical yet compassionate',
            'opening_style': 'Medical precision meets spiritual insight'
        },

        'seasonal_journey': {
            'name': 'Seasonal Journey',
            'description': 'Story unfolds across seasons/time',
            'structure': [
                'Spring: beginning with hope',
                'Summer: pattern emerges in heat',
                'Fall: crisis and falling',
                'Winter: darkness and despair',
                'Define pattern through seasons',
                'Gita wisdom as eternal spring',
                'New season: integration and growth'
            ],
            'tone': 'Cyclical and naturalistic',
            'opening_style': 'Let time reveal, let seasons teach'
        }
    }

    @staticmethod
    def get_random_strategy() -> Dict:
        """Get a random narrative strategy"""
        strategy_name = random.choice(list(NarrativeStrategy.STRATEGIES.keys()))
        return NarrativeStrategy.STRATEGIES[strategy_name]

    @staticmethod
    def get_strategy(name: str) -> Dict:
        """Get a specific narrative strategy by name"""
        return NarrativeStrategy.STRATEGIES.get(name, None)

    @staticmethod
    def get_all_strategies() -> Dict:
        """Get all available strategies"""
        return NarrativeStrategy.STRATEGIES

    @staticmethod
    def select_strategy_for_theme(theme: str) -> Dict:
        """Intelligently select strategy based on theme"""

        theme_lower = theme.lower()

        # Theme-specific mappings
        if any(word in theme_lower for word in ['anger', 'temper', 'rage']):
            return NarrativeStrategy.STRATEGIES['single_day']

        elif any(word in theme_lower for word in ['loneliness', 'isolation', 'alone']):
            return NarrativeStrategy.STRATEGIES['letter_confession']

        elif any(word in theme_lower for word in ['confusion', 'decisions', 'choices']):
            return NarrativeStrategy.STRATEGIES['question_investigation']

        elif any(word in theme_lower for word in ['depression', 'grief', 'sorrow']):
            return NarrativeStrategy.STRATEGIES['reverse_chronology']

        elif any(word in theme_lower for word in ['achievement', 'ambition', 'success']):
            return NarrativeStrategy.STRATEGIES['dual_narrative']

        elif any(word in theme_lower for word in ['boss', 'leader', 'authority']):
            return NarrativeStrategy.STRATEGIES['dialogue_driven']

        elif any(word in theme_lower for word in ['habit', 'pattern', 'cycle', 'laziness']):
            return NarrativeStrategy.STRATEGIES['recursive_loop']

        elif any(word in theme_lower for word in ['family', 'children', 'relationships']):
            return NarrativeStrategy.STRATEGIES['multiple_vignettes']

        elif any(word in theme_lower for word in ['transformation', 'change', 'growth']):
            return NarrativeStrategy.STRATEGIES['before_after']

        elif any(word in theme_lower for word in ['death', 'loss', 'grief']):
            return NarrativeStrategy.STRATEGIES['observer_witness']

        else:
            # For other themes, random selection
            return NarrativeStrategy.get_random_strategy()


class StyleVariation:
    """Provides variations in tone, pacing, and literary devices"""

    OPENING_HOOKS = [
        'Start mid-action, in the thick of conflict',
        'Open with a surprising confession',
        'Begin with a sensory-rich scene',
        'Start with dialogue that reveals character',
        'Open with an internal monologue',
        'Begin with a question that haunts',
        'Start with a specific moment of crisis',
        'Open with a contrast or paradox',
        'Begin with a memory that matters',
        'Start with the end, then explain'
    ]

    PACING_STYLES = [
        'Slow burn: gradual revelation and building tension',
        'Rapid fire: quick scenes, fast cuts, momentum',
        'Rhythmic waves: alternate between action and reflection',
        'Steady accumulation: layer upon layer of evidence',
        'Punctuated equilibrium: long calm, sudden crisis',
    ]

    SECTION_NAMING_APPROACHES = [
        'Use questions as headers',
        'Use single evocative words',
        'Use metaphorical phrases',
        'Use fragments and incomplete thoughts',
        'Use direct imperatives (commands)',
        'Use contradictions and paradoxes',
        'Use time markers (Before, During, After)',
        'Use spatial metaphors (The Surface, The Depths)',
        'Use emotional states as markers',
        'Mix approaches for variety'
    ]

    @staticmethod
    def get_random_variations() -> Dict:
        """Get random style variations"""
        return {
            'opening_hook': random.choice(StyleVariation.OPENING_HOOKS),
            'pacing': random.choice(StyleVariation.PACING_STYLES),
            'section_naming': random.choice(StyleVariation.SECTION_NAMING_APPROACHES)
        }


def generate_article_blueprint(theme: str, use_random: bool = False) -> Dict:
    """
    Generate a complete blueprint for article structure
    Combines narrative strategy with style variations
    """

    if use_random:
        strategy = NarrativeStrategy.get_random_strategy()
    else:
        strategy = NarrativeStrategy.select_strategy_for_theme(theme)

    variations = StyleVariation.get_random_variations()

    blueprint = {
        'theme': theme,
        'narrative_strategy': strategy['name'],
        'structure': strategy['structure'],
        'tone': strategy['tone'],
        'opening_style': strategy['opening_style'],
        'opening_hook': variations['opening_hook'],
        'pacing': variations['pacing'],
        'section_naming_approach': variations['section_naming'],
        'description': strategy['description']
    }

    return blueprint


def main():
    """Test the narrative strategies"""
    import json

    themes = [
        'Anger',
        'Loneliness',
        'Confusion',
        'Depression',
        'Ambition',
        'Boss',
        'Laziness',
        'Family'
    ]

    print("Narrative Strategy Blueprints for Sample Themes\n")
    print("="*70)

    for theme in themes:
        blueprint = generate_article_blueprint(theme)
        print(f"\nTheme: {theme}")
        print(f"Strategy: {blueprint['narrative_strategy']}")
        print(f"Tone: {blueprint['tone']}")
        print(f"Opening: {blueprint['opening_style']}")
        print(f"Hook: {blueprint['opening_hook']}")
        print("-"*70)


if __name__ == '__main__':
    main()
