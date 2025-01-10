
import unittest
from title_markdown import extract_title


class TestTitleMarkdown(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
            # Hello
            """
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")
