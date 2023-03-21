root = {
    "data": "A",
    "children": [
        {"data": "B", "children": [{"data": "D", "children": []}]},
        {
            "data": "C",
            "children": [
                {
                    "data": "E",
                    "children": [
                        {"data": "G", "children": []},
                        {"data": "H", "children": []},
                    ],
                },
                {"data": "F", "children": []},
            ],
        },
    ],
}


def getDepth(node: dict):
    if len(node["children"]) == 0:
        # BASE CASE
        return 0
    else:
        # RECURSIVE CASE
        maxChildDepth = 0
        for child in node["children"]:
            childDeph = getDepth(child)
            if childDeph > maxChildDepth:
                maxChildDepth = childDeph
        return maxChildDepth + 1


print(f"Depth of tree is {getDepth(root)}")
