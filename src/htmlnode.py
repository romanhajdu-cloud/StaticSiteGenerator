
class HTMLNode():
    def __init__(self, tag:str= None, value:str= None, children: list= None, props: dict= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        formated_string = ""
        if self.props is None:
            return formated_string
        
        for key in self.props:
            formated_string += f'{key}="{self.props[key]}" '
        return formated_string

    def __repr__(self):
        print(f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props_to_html()} ")

    def __eq__(self, other):
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.children == other.children and 
                self.props == other.props)

class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict= None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html()
        if props_str:
            props_str = " " + props_str.strip()

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        print(f"tag: {self.tag}, value: {self.value}, props: {self.props_to_html()} ")

        


