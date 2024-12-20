import unittest

from parentnode import ParentNode
from leafnode import LeafNode


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
