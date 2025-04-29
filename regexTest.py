import re

# GPU matching regex (Python compatible)
gpu_regex = re.compile(
    r'(?i)\b('  # case insensitive, word boundary
    r'(?:RTX|GTX|GT)\s?\d{3,4}(?:\s?(?:TI|SUPER)){1,2}'  # NVIDIA patterns
    r'|'  # OR
    r'R(?:X|adeon)\s?(?:\d{3,4}(?:\s?(?:XT|X|PRO)){1,2}|\s?VII|\s?(?:VEGA|DNA)\s?\d*)'  # AMD patterns
    r')\b',
    re.IGNORECASE
)

# Example usage
text = """
My PC has an RTX4070 Ti Super and my friend has a Radeon RX7900 XT.
Old cards include gtx 1080ti and RX Vega 56. Watch out for fake GTX1080p!
"""

matches = gpu_regex.findall(text)
print("Found GPUs:", matches)