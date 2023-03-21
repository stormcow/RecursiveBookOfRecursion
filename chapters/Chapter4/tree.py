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


def preorderTraverse(node: dict):
    print(node["data"], end=" ")
    if len(node["children"]) > 0:
        for child in node["children"]:
            preorderTraverse(child)
    return


def postorderTraverse(node: dict):
    for child in node["children"]:
        postorderTraverse(child)
    print(node["data"], end=" ")
    return


def inorderTraverse(node: dict):
    if len(node["children"]) >= 1:
        inorderTraverse(node["children"][0])  # Traverse the left child
    print(node["data"], end=" ")
    if len(node["children"]) >= 2:
        inorderTraverse(node["children"][1])  # Traverse the right child
    return


preorderTraverse(root)
print("\n")
postorderTraverse(root)
print("\n")
inorderTraverse(root)

# def myTraversal(node: dict):
# print(node["data"])
# if len(node["children"]) == 0:
# return
# else:
# for child in node['children']:
# return myTraversal(child)
#
#
# myTraversal(root)
#
