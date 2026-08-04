
import json


def merge_settings(a: dict, b: dict):
    """
    Recursively merge two settings dictionaries.
    
    - for nested dicts: merge recursively
    - for lists: concatenate and remove duplicates
    - for other values: b's value takes precedence
    
    Args:
        a: base settings dictionary
        b: settings dictionary to merge in
    
    Returns:
        Merged settings dictionary
    """
    result = a.copy()
    
    for key, value in b.items():
        if key not in result:
            # Key only in b, add it
            result[key] = value
        elif isinstance(result[key], dict) and isinstance(value, dict):
            # Both are dicts, merge recursively
            result[key] = merge_settings(result[key], value)
        elif isinstance(result[key], list) and isinstance(value, list):
            # Both are lists, concatenate and deduplicate while preserving order
            # For complex objects like dicts, use JSON representation for comparison
            seen = set()
            merged = []
            for item in result[key] + value:
                # Create a hashable representation for deduplication
                if isinstance(item, dict):
                    item_key = json.dumps(item, sort_keys=True)
                else:
                    item_key = item
                
                if item_key not in seen:
                    seen.add(item_key)
                    merged.append(item)
            result[key] = merged
        else:
            # Different types or scalar values, b takes precedence
            result[key] = value
    
    return result

if __name__ == "__main__":
    from pprint import pprint

    config1 = {
        "that.option": {
            "list1": [
                "value1"
            ]
        }
    }

    config2 = {
        "that.option": {
            "list1": [
                "value2"
            ],
            "list2": [
                "value3"
            ]
        },
        "this.option": "hello world"
    }

    pprint(merge_settings(config1, config2))