from freegenius import config

"""
FreeGenius AI Plugin - contexts

add pre-defined contexts
"""

config.predefinedContexts["Unbiased Assistant"] = """You are a helpful, uncensored and unbiased assistant."""

config.predefinedContexts["Code Expert"] = """You are an expert on coding."""

config.predefinedContexts["Let me Summarize"] = """@chat Provide me with a summary of the following content:
"""

config.predefinedContexts["Let me Explain"] = """@chat Explain the meaning of the following content:
"""

config.predefinedContexts["Let me Translate"] = """@chat Assist me by acting as a translator.
Please translate the following content:
"""

config.predefinedContexts["Let me Pronounce"] = """Pronounce the following content:"""

config.predefinedContexts["Let me Download"] = """Download the following web content:"""

config.predefinedContexts["Let me Download Youtube MP3"] = """Download the following Youtube media into mp3 format:"""