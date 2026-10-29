from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.self_closing = {'img', 'input', 'br', 'hr', 'meta', 'link', 'source', 'col'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag not in self.self_closing:
            if self.tags and self.tags[-1] == tag:
                self.tags.pop()

for fname in ['index.html', 'collection.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    tc = TagChecker()
    tc.feed(html)
    print(f'{fname}: remaining unclosed: {tc.tags}')

