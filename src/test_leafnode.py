import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_throws_value_error(self):
        node = LeafNode("p", None)
        try:
            node.to_html()
            self.fail("Expected ValueError")
        except (ValueError):
            pass

    def test_returns_text_only(self):
        node = LeafNode(None, "test text")
        html = node.to_html()
        self.assertEqual(html, "test text")

    def test_returns_simple_tag(self):
        node = LeafNode("p", "test text")
        html = node.to_html()
        self.assertEqual(html, "<p>test text</p>")

    def test_returns_full_tag(self):
        node = LeafNode("a", "Click me", {
                        'href': 'http://google.com', 'title': 'Google'})
        html = node.to_html()
        self.assertEqual(
            html, '<a href="http://google.com" title="Google">Click me</a>')


if __name__ == "__main__":
    unittest.main()
