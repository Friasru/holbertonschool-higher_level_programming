#!/usr/bin/python3
"""Module for serializing and deserializing python dictionaries"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a python dictionary"""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True

    except (IOError, OSError):
        return False
    except Exception:
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary

    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
    except (IOError, OSError):
        return None
    except Exception:
        return None
