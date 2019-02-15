

class HelpResource:
    def on_get(self, req, resp):
        content = {
            'Help': 'This is the help of the API',
        }
        resp.media = content


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote
