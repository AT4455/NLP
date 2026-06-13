import re

# ── 1. Information Extraction ──────────────────────────────────────────────

EMAIL    = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
PHONE    = r'(\+?\d{1,3}[.\-\s]?)?\(?\d{3,5}\)?[.\-\s]?\d{3,5}[.\-\s]?\d{3,5}'
DATE     = r'\b(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}|\d{4}[\/\-]\d{1,2}[\/\-]\d{1,2})\b'
URL      = r'https?://[^\s<>"{}|\\^`\[\]]+'
HASHTAG  = r'#[a-zA-Z0-9_]+'
MENTION  = r'@[a-zA-Z0-9_]+'

def extract_info(text):
    return {
        "emails":    re.findall(EMAIL,   text),
        "phones":    re.findall(PHONE,   text),
        "dates":     re.findall(DATE,    text),
        "urls":      re.findall(URL,     text),
        "hashtags":  re.findall(HASHTAG, text),
        "mentions":  re.findall(MENTION, text),
    }

# ── 2. Tokenization ────────────────────────────────────────────────────────

def word_tokenize(text):
    return re.findall(r'\b\w+\b', text)

def sentence_tokenize(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

def alpha_tokenize(text):
    return re.findall(r'[a-zA-Z]+', text)

def nltk_style_tokenize(text):
    return re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b|\$[\d.]+|\w+", text)

def tokenize(text, mode="word"):
    modes = {
        "word":     word_tokenize,
        "sentence": sentence_tokenize,
        "alpha":    alpha_tokenize,
        "nltk":     nltk_style_tokenize,
    }
    tokens = modes.get(mode, word_tokenize)(text)
    return {"tokens": tokens, "count": len(tokens), "unique": len(set(t.lower() for t in tokens))}

# ── 3. Text Cleaning ───────────────────────────────────────────────────────

def clean_text(text, remove_urls=True, remove_html=True, remove_emojis=True,
               remove_social=True, remove_special=True, normalize_spaces=True):
    original_len = len(text)
    steps = []
    if remove_urls:
        text = re.sub(r'https?://\S+', '', text)
        steps.append("URLs removed")
    if remove_html:
        text = re.sub(r'&[a-z]+;', '', text, flags=re.IGNORECASE)
        steps.append("HTML entities removed")
    if remove_emojis:
        text = re.sub(r'[\U0001F300-\U0001F9FF]', '', text)
        steps.append("Emojis removed")
    if remove_social:
        text = re.sub(r'[@#][a-zA-Z0-9_]+', '', text)
        steps.append("Hashtags/mentions removed")
    if remove_special:
        text = re.sub(r"[^a-zA-Z0-9\s.,!?']", '', text)
        steps.append("Special characters removed")
    if normalize_spaces:
        text = re.sub(r'\s{2,}', ' ', text).strip()
        steps.append("Extra spaces normalized")
    return {"cleaned": text, "original_length": original_len,
            "cleaned_length": len(text), "steps": steps}

# ── 4. Validation ──────────────────────────────────────────────────────────

VALIDATORS = {
    "email":  r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$',
    "mobile": r'^(\+91[.\-\s]?)?[6-9]\d{9}$',
    "date":   r'^(0?[1-9]|[12]\d|3[01])\/(0?[1-9]|1[0-2])\/\d{4}$',
    "pan":    r'^[A-Z]{5}[0-9]{4}[A-Z]$',
    "pin":    r'^\d{6}$',
    "url":    r'^https?://[^\s]+$',
}

def validate(field, value):
    pattern = VALIDATORS.get(field)
    if not pattern:
        return {"valid": False, "error": "Unknown field type"}
    return {"valid": bool(re.match(pattern, value)), "pattern": pattern, "value": value}

# ── 5. Custom Pattern ──────────────────────────────────────────────────────

def custom_match(pattern, text, flags_str="g"):
    py_flags = 0
    if 'i' in flags_str:
        py_flags |= re.IGNORECASE
    if 'm' in flags_str:
        py_flags |= re.MULTILINE
    try:
        matches = re.findall(pattern, text, py_flags)
        return {"matches": matches, "count": len(matches), "unique": len(set(matches))}
    except re.error as e:
        return {"error": str(e), "matches": [], "count": 0}