from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("All parent nodes must have children")

        child_html = "".join(map(lambda x: x.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"
