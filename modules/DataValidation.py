import jsonschema
import json

"""
Here is the schema that defines how the data.json file should be laid out.
As the project evolves, this file shoule be changed to allow the fields and attributes
we're using.
"""

schema = {
    "type": "object",
    "properties": {
        "votes": { # the key is the vote id
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "value": { "type": "integer", "minimum": 1, "maximum": 10 }, # upper and lower bounds of vote weight
                    "target_id": { "type": "integer" }, # user or channel snowflake
                    "voter_id": { "type": "integer" },
                    "time": { "type": "integer" }
                },
                "required": ["value", "target_id", "voter_id", "time"]
            }
        },

        "users": { # the key is the user snowflake
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "sanity": { "type": "integer", "minimum": 1, "maximum": 100 },
                    "price": { "type": "integer", "minimum": 1 },
                    "volatility": { "type": "number" } # float inclusive
                },
                "required": ["sanity", "price", "volatility"]
            }
        }
    }
}

def validate_data(data_path) -> bool:
    jsonfile = open(data_path, 'r')
    data = json.loads(jsonfile.read())

    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as err:
        print('The data.json file has failed verification with the following error:')
        print(err)
        return False
        
    return True


