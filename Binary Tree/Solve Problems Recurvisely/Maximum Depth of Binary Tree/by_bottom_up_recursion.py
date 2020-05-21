'''

Description:

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
       
    def maxDepth(self, root: TreeNode) -> int:

        

        def helper( node: TreeNode ):

            if not node:
                # Base case: empty node
                return 0

            else:
                # General case
                return max( helper( node.left ), helper( node.right ) ) + 1

        # ---------------------------------------------------

        return helper( node = root )



# n : the number of nodes in binary trees

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for call stack, which is of O( n )



def test_bench():

    root = TreeNode( 3 )

    root.left = TreeNode( 9 )
    root.right = TreeNode( 20 )

    root.right.left = TreeNode( 15 )
    root.right.right = TreeNode( 7 )

    # expected output:
    '''
    3
    '''
    print( Solution().maxDepth( root ) )

    # ----------------------------------------

    root = TreeNode( 2 )
    
    root.left = TreeNode( 1 )
    root.right = TreeNode( 3 )

    # expected output:
    '''
    2
    '''
    print( Solution().maxDepth( root ) )

    # ----------------------------------------

    root = TreeNode( 2 )

    # expected output:
    '''
    1
    '''
    print( Solution().maxDepth( root ) )

    # ----------------------------------------

    root = None

    # expected output ( test for empty tree ):
    '''
    0
    '''
    print( Solution().maxDepth( root ) )


if __name__ == '__main__':

    test_bench()