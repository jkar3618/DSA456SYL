## Part C: Time Complexity Analysis

Function	    | Time Complexity |	Explanation

insert(data)	| O(n)	| To maintain a sorted order, the function must traverse the list to find the correct insertion point. In the worst case, it traverses all n nodes.

remove(data)	| O(n)	| The function searches for the node containing the specified data. If the node is near the end or not present, it must traverse the entire list.

is_present(data)	| O(n)	| This function linearly searches the list for the target value, checking each node’s data until a match is found or the list ends.

__len__()	| O(1)	| The number of elements is tracked using a counter variable. Therefore, the length can be returned immediately without traversal.
