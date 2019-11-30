import json
from dicttoxml import dicttoxml
import xmltodict


class Database():
    def __init__(self):
        self._data = {'id': 1, 'content': {'name': 'CongVo', 'role': 'leader'}}

    def load_xml(self):
        xml = dicttoxml(self._data)
        return xml


class DataProcessor():
    def process(self, xml_data):
        raise NotImplementedError


class XMLDataProcessor(DataProcessor):
    def process(self, xml_data):
        return xml_data


class XML2JSONDataProcessor(DataProcessor):

    def _xml_to_json(self, xml_data):
        json_data = json.dumps(xmltodict.parse(xml_data,
                                               xml_attribs=False))
        return json_data

    def process(self, xml_data):
        json_data = self._xml_to_json(xml_data)
        return json_data


class DataProcessAdapter(DataProcessor):
    def __init__(self, adaptee=None):
        self._adaptee = adaptee

    def set_adaptee(self, adaptee):
        self._adaptee = adaptee

    def process(self, xml_data):
        if self._adaptee is None:
            raise ValueError("Must specify `adaptee`")
        return self._adaptee.process(xml_data)


class Display():
    def display(self, data):
        raise NotImplementedError


class XMLDisplay(Display):
    def display(self, xml_data):
        print(f"Display: {xml_data}")


class JsonDisplay(Display):
    def display(self, json_data):
        print(f"Display: {json_data}")


if __name__ == "__main__":
    # Load Data
    db = Database()
    xml_data = db.load_xml()

    xml2json_processor = XML2JSONDataProcessor()
    data_processor = DataProcessAdapter(xml2json_processor)
    json_data = data_processor.process(xml_data)

    # Json Display
    display = JsonDisplay()
    display.display(json_data)

    # XML Display
    xml_processor = XMLDataProcessor()
    data_processor.set_adaptee(xml_processor)

    xml_data = data_processor.process(xml_data)
    display = XMLDisplay()
    display.display(xml_data)