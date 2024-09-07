from dataclasses import dataclass, is_dataclass
from typing import Any, Type, TypeVar


@dataclass
class Geo:
    lat: str
    lng: str


@dataclass
class Address:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


@dataclass
class Company:
    name: str
    catchPhrase: str
    bs: str


@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


T = TypeVar("T")


def map_dict_to_dataclass(data: dict[str, Any], cls: Type[T]) -> T:
    """
    Recursively maps a dictionary to the corresponding dataclass.

    :param data: The dictionary containing the data.
    :param cls: The target dataclass type.
    :return: An instance of the dataclass with data from the dictionary.
    """
    # Create a dictionary that will be used to instantiate the dataclass
    field_values = {}

    for field in cls.__dataclass_fields__.keys():  # type: ignore
        # Get the type of the field
        field_type = cls.__dataclass_fields__[field].type  # type: ignore

        # If the field type is a dataclass, recurse into it
        if is_dataclass(field_type):  # type: ignore
            field_values[field] = map_dict_to_dataclass(data[field], field_type)  # type: ignore
        else:
            field_values[field] = data[field]

    # Return an instance of the dataclass
    return cls(**field_values)
