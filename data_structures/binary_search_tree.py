"""This mod contains class Binary Search Tree"""

from data_structures.node_tree import NodeTree


class BinarySearchTree:
    """This class implements work like a binary search tree"""

    count = 0

    def __init__(self, value):
        self.head = NodeTree(value)
        self.count += 1
        # helps property for deleting element
        self._previous_branch = None
        self._position_branch = None

    @staticmethod
    def _check_branch_to_value(current_node: NodeTree, location: bool):
        """Return True if we can append value to tree"""
        if location:
            if current_node.right is None:
                return True
            return False
        if current_node.left is None:  # value
            return True
        return False

    @staticmethod
    def _select_branch(select_node: NodeTree, value):
        """Return True if we can move value to right branch"""
        if select_node.value < value:
            return True
        return False

    def _insert_to_empty_tree(self, element):
        """Insert element if tree empty"""
        self.head = element
        self.count += 1

    def _insert_if_node_none(self, previous_node: NodeTree, node_to_insert: NodeTree, element):
        """Helps func if node is None after while"""
        if previous_node.value < element:
            previous_node.right = node_to_insert
        else:
            previous_node.left = node_to_insert
        self.count += 1

    def _insert_to_tree(self, selected_branch, permission,
                        node: NodeTree, node_to_insert: NodeTree):
        """Insert element if his position in center of tree"""
        if selected_branch and permission:
            # can insert to right branch
            node.right = node_to_insert
            self.count += 1
            return True
        if not selected_branch and permission:
            # can insert to left branch
            node.left = node_to_insert
            self.count += 1
            return True
        return False

    def insert(self, element):
        """Add element to binary tree"""
        node_to_insert = NodeTree(element)
        # if tree is empty
        if self._check_empty_tree():
            self._insert_to_empty_tree(node_to_insert)
            return None
        # if duplicate
        if self.lookup(element) is not None:
            return None

        node = self.head
        index = 0
        previous_node = None
        while index != self.count:
            # if we added value to last branch
            if node is None:
                self._insert_if_node_none(previous_node, node_to_insert, element)
                break
            # if we add element in center tree
            selected_branch = self._select_branch(node, element)
            permission_to_insert = self._check_branch_to_value(node, selected_branch)
            # maybe insert value to tree if we can
            if self._insert_to_tree(selected_branch, permission_to_insert, node, node_to_insert):
                break

            index += 1
            previous_node = node
            if selected_branch:
                node = node.right
            else:
                node = node.left

    def lookup(self, value):
        """Get link to value by value"""
        node = self.head
        index = 0
        while index != self.count:
            if node is None:
                return None
            if node.value == value:
                return node
            next_branch = self._select_branch(node, value)
            if next_branch and node.value == value:
                return node
            if node.value == value:
                return node
            index += 1
            # set previous branch for delete func
            self._previous_branch = node
            self._position_branch = next_branch
            # set next node
            node = node.right if next_branch else node.left

    def _check_and_delete_head(self, value):
        """If we delete one element and he is head"""
        if self.count == 1 and self.head.value == value:
            self.head = None
            self.count -= 1
            return True
        return False

    def _check_empty_tree(self):
        """Check tree about empty state"""
        if self.count == 0:
            return True
        return False

    def _helper_to_delete_branch(self, value_for_node):
        """Delete something branch in many situation"""
        if self._position_branch:
            self._previous_branch.right = value_for_node
        else:
            self._previous_branch.left = value_for_node
        self.count -= 1

    def _delete_branch_without_children(self, node_to_delete: NodeTree):
        """Delete branch in situation when branch have no children"""
        if node_to_delete.left is None and node_to_delete.right is None:
            # delete
            self._helper_to_delete_branch(None)
            return True
        return False

    def _del_branch_with_left_child(self, node_to_delete: NodeTree):
        """Delete branch in situation when branch have a left child"""
        if node_to_delete.left is not None and node_to_delete.right is None:
            # delete
            self._helper_to_delete_branch(node_to_delete.left)
            return True
        return False

    def _del_branch_with_right_child(self, node_to_delete: NodeTree):
        """Delete branch in situation when branch have a right child"""
        if node_to_delete.left is None and node_to_delete.right is not None:
            # delete
            self._helper_to_delete_branch(node_to_delete.right)
            return True
        return False

    def _del_branch_with_two_child(self, node_to_delete: NodeTree):
        """Delete branch in situation when branch have two children"""
        if node_to_delete.left and node_to_delete.right:
            # we search max value in left branch current node to delete
            node = node_to_delete.left
            index = 0

            # this node to position after deleting node
            node_to_del_position = None
            previous_node = None

            # link to nodes if long deleting
            node_in_air_left = node_to_delete.left
            node_in_air_right = node_to_delete.right

            # get necessary elements
            while index != self.count:
                node_to_del_position = node
                if node.right is None:
                    break
                previous_node = node
                index += 1
                node = node.right

            # proces permutations for delete element with two children
            if self._position_branch:
                self._previous_branch.right = node_to_del_position
            else:
                self._previous_branch.left = node_to_del_position

            # create connections with branches
            node_to_del_position.left = node_in_air_left
            node_to_del_position.right = node_in_air_right

            # clear right child after reposition
            previous_node.right = None
            self.count -= 1
            return True
        return False

    def delete(self, value):
        """Delete element by value"""
        # check to one head and maybe delete this
        if self._check_and_delete_head(value):
            return None
        # get node for delete
        node_to_delete = self.lookup(value)
        # search situation about current node to delete
        if node_to_delete is not None:
            if self._delete_branch_without_children(node_to_delete):
                return None
            if self._del_branch_with_left_child(node_to_delete):
                return None
            if self._del_branch_with_right_child(node_to_delete):
                return None
            if self._del_branch_with_two_child(node_to_delete):
                return None
            return None
