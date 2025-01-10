import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        n1 = HtmlNode("p", "p tag", None, {
            'href': 'http://google.com', 'id': '1234'})
        props = n1.props_to_html()
        self.assertEqual(props, ' href="http://google.com" id="1234"')

        n2 = HtmlNode("p", "p tag", None, {})
        props = n2.props_to_html()
        self.assertEqual(props, "")


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


class TestParentNode(unittest.TestCase):
    def test_throws_value_error_when_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "leaf")])
        try:
            node.to_html()
            self.fail("Expected ValueError")
        except (ValueError):
            pass

    def test_throws_value_error_when_no_children(self):
        node = ParentNode("div", None)
        try:
            node.to_html()
            self.fail("Expected ValueError")
        except (ValueError):
            pass

    def test_throws_value_error_when_empty_children(self):
        node = ParentNode("div", [])
        try:
            node.to_html()
            self.fail("Expected ValueError")
        except (ValueError):
            pass

    def test_returns_parent_and_children(self):
        parent = ParentNode(
            "div",
            [
                LeafNode("p", "leaf"),
                ParentNode(
                    "div",
                    [
                        LeafNode("a", "nested", {'href': 'http://google.com'})
                    ]
                )
            ]
        )
        expected = '<div><p>leaf</p><div><a href="http://google.com">nested</a></div></div>'
        parent_html = parent.to_html()
        self.assertEqual(parent_html, expected)


if __name__ == "__main__":
    unittest.main()
