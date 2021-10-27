import dataclasses
import json
import sys

@dataclasses.dataclass
class Item:
    type: str
    attributes: dict

    def make_item(self):
        if self.type == "filler":
            return "<filter {}></filter>".format(self.make_attributes())
        elif self.type == "text":
            return "<textarea {}/>".format(self.make_attributes())

    def make_attributes(self):
        return " ".join(["{}=\"{}\"".format(k,v) for k,v in self.attributes.items() if not (v is list)])

@dataclasses.dataclass
class Form:
    name: str
    postmessage: str
    items: [Item]

    def __post_init__(self):
        self.items = [Item(**item) for item in self.items]

    def make_form(self):
        elements = "\n".join([item.make_item() for item in self.items])
        return "<form name=\"{}\" postmessage=\"{}\">\n{}\n</form>".format(self.name, self.postmessage, elements)

with open('C:\\Users\Lenovo\mu_code\json1.json', 'r') as form_json:
    loaded_json = json.load(form_json)
    form = Form(**loaded_json["form"])
    print(form.make_form())
