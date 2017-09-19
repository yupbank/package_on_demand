import jsonschema
import pytest


def main():
    with pytest.raises(jsonschema.ValidationError) as e:
        jsonschema.validate([2, 3, 4], {"maxItems" : 2})
    print e

if __name__ == "__main__":
    main()
