import json

def to_json_str(obj):
    return json.dumps(obj, ensure_ascii=False)
