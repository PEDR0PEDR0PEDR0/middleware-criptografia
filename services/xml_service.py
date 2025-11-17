# services/xml_service.py
import xml.etree.ElementTree as ET
import json

# Função simplificada de conversão JSON para XML (você pode usar bibliotecas como dicttoxml)
def json_to_xml(json_data: dict, root_tag: str) -> str:
    # Implementação de conversão.
    # Exemplo: Monta a string XML manualmente ou com lxml/dicttoxml
    xml_string = f'<{root_tag}>'
    for key, value in json_data.items():
        xml_string += f'<{key}>{value}</{key}>'
    xml_string += f'</{root_tag}>'
    return xml_string

# Função simplificada de conversão XML para JSON (você pode usar bibliotecas como xmltodict)
def parse_xml_to_dict(xml_string: str) -> dict:
    # Implementação de conversão.
    # Exemplo: Usar ET ou xmltodict para gerar um dicionário.
    # Para o escopo deste esqueleto, vou simular um parser simples
    # (em um projeto real, use xmltodict/lxml)
    root = ET.fromstring(xml_string.strip())
    data = {root.tag: {child.tag: child.text for child in root}}
    return data
    
def dict_to_json(data: dict) -> str:
    return json.dumps(data)