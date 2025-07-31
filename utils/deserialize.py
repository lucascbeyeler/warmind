from inspect import getmembers
from typing import get_args, get_origin
from enum import Enum
from typing import Union

def deserialize(data: Union[any, dict[str, any]], expect_object: object) -> object:
    """ Transform a complex dictionary into an object.
          :param data: The dictionary you want to convert
          :expect_object: The object you want to convert your dictionary
          :return: The instance of the object with the data from the dictionary

          TODO:
              * Convert this into a decorator to be easier to used;
              * Make possible to deal with Java and Python syntax differences presents between JSONs to respect PEP8
     """
    if data is None:
        return None

    instance = {}
    for members in getmembers(expect_object):
        if members[0] == "__annotations__":
            for kname, vtype in members[1].items():
                # Check if data is a dictionary. If not, raise an error.
                if not isinstance(data, dict):
                    raise TypeError(f"Expected dictionary for deserialization, but got {type(data)} for field {kname} in {expect_object.__name__}")

                field_data = data.get(kname)

                # Check if the field is Optional
                is_optional = get_origin(vtype) is Union and type(None) in get_args(vtype)

                if field_data is None:
                    if not is_optional:
                        # If data is None for a non-optional field, raise an error
                        raise ValueError(f"Missing or None value for non-optional field '{kname}' of type {vtype} in {expect_object.__name__}")
                    else:
                        instance[kname] = None # It's optional and None, so set to None
                else:
                    # If data is present, proceed with deserialization via __actions
                    instance[kname] = __actions(vtype=vtype, data=field_data)
            return expect_object(**instance)


def __actions(vtype: object, data: Union[any, dict[str, any]]):
    """ Convert the data to the correct type based on the attributes correspondent to that object.
        The dictionary and the dataclass should share the same field names for this to work.
        Not meant to be used directly - please use deserialize instead.
    """
    if data is None:
        return None

    if vtype in (str, int, float, bool):
        return data

    if isinstance(data, list):
        element_type = get_args(vtype)[0]
        return [deserialize(expect_object=element_type, data=v) for v in data]

    if issubclass(vtype, Enum):
        return vtype(data)

    return deserialize(data=data, expect_object=vtype)