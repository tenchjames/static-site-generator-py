from leafnode import LeafNode
from textnode import TextNode, TextType
from htmlnode import HtmlNode


def main():
    text_node = TextNode("text in the node", TextType.BOLD)
    print(text_node)

    html_node = HtmlNode("p", "a paragraph", None, None)
    print(html_node)

    p = LeafNode("p", "This is a paragraph of text.")
    print(p)
    print(p.to_html())
    a = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(a)
    print(a.to_html())


if __name__ == "__main__":
    main()
