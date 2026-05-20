"""Base prompt templates."""


def get_system_prompt(theme: str, mood: str) -> str:
    """Get base system prompt.

    Args:
        theme: Narrative theme
        mood: Narrative mood

    Returns:
        System prompt string
    """
    return f"""
You are a vivid and creative narrative writer. Your task is to create immersive, 
detail-rich descriptions that transport readers into the scene.

Theme: {theme}
Mood: {mood}

Generate engaging, cinematic narratives with:
- Rich sensory details (visual, tactile, atmospheric)
- Authentic period-specific elements
- Dynamic energy and pacing
- Seamless narrative flow without lists or bullet points

Use evocative language and maintain consistent tone throughout.
"""
