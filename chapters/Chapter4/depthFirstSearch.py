root = {
    "name": "Alice",
    "children": [
        {"name": "Bob", "children": [{"name": "Darya", "children": []}]},
        {
            "name": "Caroline",
            "children": [
                {
                    "name": "Eve",
                    "children": [
                        {"name": "Gonzalo", "children": []},
                        {"name": "Hadassah", "children": []},
                    ],
                },
                {"name": "Fred", "children": []},
            ],
        },
    ],
}


def find8LetterName(node: dict):
    print(f"Visiting node {node['name']}...")

    # Preorder depth first search
    print(f"Checking if {node['name']} is 8 letters...")
    if len(node["name"]) == 8:
        return node["name"]

    if len(node["name"]) > 0:
        for child in node["children"]:
            retrunValue = find8LetterName(child)
            if retrunValue != None:
                return retrunValue

    return None


print(f"Found an 8-letter name: {find8LetterName(root)}")
