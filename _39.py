"""
Using PIL for Python and docstrings and OOP:

39. We can write a description of a binary tree, such as we might use for a search, as a list of
nodes with pointers to its children. Write a program that will take such a description and
display the tree graphically.
"""

from PIL import Image, ImageDraw

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeDrawer:
    def __init__(self):
        self.node_radius = 20
        self.horizontal_spacing = 50
        self.vertical_spacing = 50
        self.node_color = "lightblue"

    def draw_binary_tree(self, root):
        tree_width, tree_height = self.get_tree_dimensions(root)
        image = Image.new("RGB", (tree_width, tree_height), "white")
        draw = ImageDraw.Draw(image)

        self.draw_tree_recursive(draw, root, tree_width // 2, 20)

        image.show()

    def draw_tree_recursive(self, draw, node, x, y):
        if node is not None:
            # Draw the node
            self.draw_node(draw, node.value, x, y)

            # Draw left child
            left_x = x - self.horizontal_spacing // 2
            left_y = y + self.vertical_spacing
            self.draw_tree_recursive(draw, node.left, left_x, left_y)

            # Draw right child
            right_x = x + self.horizontal_spacing // 2
            right_y = y + self.vertical_spacing
            self.draw_tree_recursive(draw, node.right, right_x, right_y)

    def draw_node(self, draw, value, x, y):
        draw.ellipse(
            [x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius],
            fill=self.node_color
        )
        draw.text((x, y), str(value), fill="black", font=None, anchor="mm")

    def get_tree_dimensions(self, root):
        def get_tree_size(node):
            if node is None:
                return 0, 0
            left_width, left_height = get_tree_size(node.left)
            right_width, right_height = get_tree_size(node.right)
            width = left_width + self.horizontal_spacing + right_width
            height = max(left_height, right_height) + self.vertical_spacing
            return width, height

        return get_tree_size(root)

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Draw the binary tree
    drawer = BinaryTreeDrawer()
    drawer.draw_binary_tree(root)
