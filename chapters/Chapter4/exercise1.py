root = {"data": "A", "children": []}
node2 = {"data": "B", "children": []}
node3 = {"data": "C", "children": []}
node4 = {"data": "D", "children": []}
node5 = {"data": "E", "children": []}
node6 = {"data": "F", "children": []}
node7 = {"data": "G", "children": []}
node8 = {"data": "H", "children": []}

root["children"] = [node2, node3]
node2["children"] = [node4]
node3["children"] = [node5, node6]
node5["children"] = [node7, node8]


def reverseInorderTraverse(node: dict):
    if len(node["children"]) >= 2:
        reverseInorderTraverse(node["children"][1])  # Traverse the left child
    print(node["data"], end=" ")
    if len(node["children"]) >= 1:
        reverseInorderTraverse(node["children"][0])  # Traverse the right child
    return


reverseInorderTraverse(root)
