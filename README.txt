Some python files that were implemented for learning purposes in earlier chapters of the data structures book can be found in the python_scrapbook directory. Some files in there won't work without dependencies, but I don't want them cluttering up the data-structures directory.

Standalone c files, minimal as they are (I don't honestly know any C), can be found in the c_scrapbook directory.

The meat and potatoes of this repository is in the collectionframework directory, where I implement a host of different collection types. There are also interfaces and abstract classes, the former live in the interfaces directory; it contains commented specifications, or blueprints, for each concrete class. The abstractclasses directory contains abstract classes; these are used to factor common methods and data from concrete classes so that they may simply inherit from the relevant abstract class.

Finally, there's the collectiontesting directory; it contains unit testing modules for each concrete class and a script to run them all at once.

I chose not to abstract binary trees into a base class because the only two potential subclasses would be linked binary search trees and array heaps. These two classes are two different implementations but they also implement different abstract data types. I don't implement array binary search trees because BSTs have the potential to be unbalanced and thus arrays would waste a relatively vast amount of space. I don't implement linked heaps because heaps are always complete binary trees, and thus the array implementation is more efficient in terms of space, with the only downside coming from growing or shrinking the underlying array if necessary.
