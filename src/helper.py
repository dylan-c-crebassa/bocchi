import re

def format_query(input_str):
    # Regex pattern to detect URLs (http(s):// or www.)
    url_pattern = re.compile(r'^(https?://|www\.)', re.IGNORECASE)

    if url_pattern.match(input_str.strip()):
        # It's a URL, return as-is
        return input_str.strip()
    else:
        # It's a query, add ytsearch: prefix
        return f"ytsearch:{input_str.strip()}"
    
def ensure_https(url):
    # Check if the URL starts with http:// or https:// using regex
    if not re.match(r"^https?://", url, re.IGNORECASE):
        return "https://" + url
    return url
