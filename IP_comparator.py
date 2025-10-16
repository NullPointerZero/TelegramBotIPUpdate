import requests

HEADERS = {"User-Agent": "python-requests (get public ip)"}

def get_public_ip():
    try:
        url = "https://whatismyipaddress.com/"
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        ip = extract_ip_from_anchor(r.text)
        return ip
        if ip:
            return ip
    except Exception:
        pass
    raise RuntimeError("Konnte keine öffentliche IP ermitteln.")


def extract_ip_from_anchor(html: str) -> str:
    # Erst aus dem href lesen: href="https://whatismyipaddress.com/ip/..."
    base = "https://whatismyipaddress.com/ip/"
    # doppelte Anführungszeichen
    m1 = f'href="{base}'
    i = html.find(m1)
    quote = '"'
    # einfache Anführungszeichen, falls nötig
    if i == -1:
        m1 = f"href='{base}"
        i = html.find(m1)
        quote = "'"
    if i != -1:
        start = i + len(m1)
        end = html.find(quote, start)
        if end != -1:
            cand = html[start:end].strip()
            if is_ipv4(cand):
                return cand
            # Falls IPv6 o.ä.: einfach zurückgeben, wenn du das willst
            # return cand

    # Fallback: Link-Text zwischen > und < nehmen
    if i != -1:
        tag_end = html.find(">", i)
        if tag_end != -1:
            next_lt = html.find("<", tag_end + 1)
            if next_lt != -1:
                text = html[tag_end + 1: next_lt].strip()
                if is_ipv4(text):
                    return text

    raise RuntimeError("Keine IPv4 im <a>-Tag gefunden.")

def is_ipv4(tok: str) -> bool:
    parts = tok.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit():
            return False
        n = int(p)
        if n < 0 or n > 255:
            return False
    return True

if __name__ == "__main__":
    try:
        print(get_public_ip())
    except Exception as e:
        print(f"Fehler: {e}")
