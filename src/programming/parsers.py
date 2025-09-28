
import re
from typing import List, Optional
from .block_generator import Intent


class NaturalLanguageParser:
    """
    Converts natural language to structured intents.
    NOTE: This regex-based parser is a starting point. It's effective for simple,
    well-defined commands but will be less robust for complex or ambiguous phrasing.
    Future versions should consider more advanced NLP techniques.
    """

    def __init__(self):
        # ... (patterns remain the same as your original)
        self.action_patterns = {
            r"move|walk|go": "move", r"jump|hop|leap": "jump", r"play sound|make noise|sound": "play_sound",
            r"change color|color": "change_color", r"rotate|turn|spin": "rotate", r"hide|disappear": "hide",
            r"show|appear": "show", r"say|speak|talk": "say",
        }
        self.trigger_patterns = {
            r"when (.+) pressed|when (.+) key": ("key_press", r"\1|\2"), r"when flag clicked|when start": ("flag_click", None),
            r"when (.+) clicked": ("sprite_click", r"\1"), r"forever|always|continuously": ("forever", None), r"repeat (\d+)": ("repeat", r"\1"),
        }
        self.direction_patterns = {
            r"right|to the right": "right", r"left|to the left": "left", r"up|upward": "up", r"down|downward": "down",
        }

    def parse(self, text: str) -> List[Intent]:
        text = text.lower().strip()
        intents = []
        sentences = self._split_sentences(text)
        for sentence in sentences:
            intent = self._parse_sentence(sentence)
            if intent:
                intents.append(intent)
        return intents

    def _split_sentences(self, text: str) -> List[str]:
        """REVISED: Improved sentence splitting to better handle conjunctions."""
        # Use regex to split on common conjunctions, preserving them for context if needed later.
        sentences = re.split(r'\s+(and|then|and then)\s+', text)
        # Filter out the conjunctions and any empty strings
        return [s.strip() for s in sentences if s and s not in ['and', 'then', 'and then']]

    def _parse_sentence(self, sentence: str) -> Optional[Intent]:
        # ... (parsing logic remains the same)
        intent = Intent(action="unknown")
        for pattern, action in self.action_patterns.items():
            if re.search(pattern, sentence):
                intent.action = action
                break
        for pattern, (trigger_type, param_pattern) in self.trigger_patterns.items():
            match = re.search(pattern, sentence)
            if match:
                intent.trigger = trigger_type
                if param_pattern and match.groups():
                    param_value = next((g for g in match.groups() if g), None)
                    if param_value:
                        if trigger_type == "key_press":
                            intent.parameters["key"] = param_value
                        elif trigger_type == "repeat":
                            intent.parameters["times"] = int(param_value)
                break
        for pattern, direction in self.direction_patterns.items():
            if re.search(pattern, sentence):
                intent.parameters["direction"] = direction
                break
        number_match = re.search(
            r"(\d+)\s*(steps?|pixels?|seconds?)", sentence)
        if number_match:
            value, unit = number_match.groups()
            if "step" in unit or "pixel" in unit:
                intent.parameters["steps"] = int(value)
            elif "second" in unit:
                intent.parameters["seconds"] = float(value)
        if "direction" in intent.parameters and "steps" not in intent.parameters:
            intent.parameters["steps"] = 10
        return intent if intent.action != "unknown" else None
