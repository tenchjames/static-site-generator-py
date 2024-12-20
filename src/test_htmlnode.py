import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        n1 = HtmlNode("p", "p tag", None, {
            'href': 'http://google.com', 'id': '1234'})
        props = n1.props_to_html()
        self.assertEqual(props, ' href="http://google.com" id="1234"')

        n2 = HtmlNode("p", "p tag", None, {})
        props = n2.props_to_html()
        self.assertEqual(props, "")


if __name__ == "__main__":
    unittest.main()
