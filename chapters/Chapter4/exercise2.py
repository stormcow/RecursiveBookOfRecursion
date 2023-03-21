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


def addDepth(node: dict):
    if len(node["children"]) == 0:
        # add children
        newChild = {"data": "I", "children": []}
        node["children"].append(newChild)
        return
    else:
        for child in node["children"]:
            addDepth(child)


def preorderTraverse(node: dict):
    print(node["data"], end=" ")
    if len(node["children"]) > 0:
        for child in node["children"]:
            preorderTraverse(child)
    return


print(getDepth(root))
addDepth(root)
print(getDepth(root))
preorderTraverse(root)
