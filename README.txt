The arrays.py and node.py files are the same in Chapters 4-6. The bag_test.py file is the same in Chapters 5 and 6, however, the arraybag.py and linkedbag.py files are NOT the same in Chapters 5 and 6. In Chapter 5 they are fully implemented on their own, whereas in Chapter 6 they are factored and depend on the abstractbag.py and abstractcollection.py modules.


In Chapter 3, I coded a few search and sort functions. I also studied the time and space complexities of the algorithms underlying each function.


In Chapter 4, I wrote three classes. The first mimics an array in C, the second is a node class that is used to build the third, a singly-linked list. These are all meant to be exported for use in other collections.


In Chapter 5, I developed an interface for the bag ADT. I then used this specification to implement an unsorted bag using first the array and then the linked list from Chapter 4. Both classes implement the interface functionality identically, although there are always time and space tradeoffs based on implentation choice.

I then implemented an array-based set and an array-based sorted bag that inherited from the array-based bag class.


In Chapter 6, I used inheritance to factor the common methods and data in the LinkedBag and ArrayBag classes into an AbstractBag super class. In this structure, the concrete classes still implement the bag interface from Chapter5, but they inherit common methods and data from the AbstractBag class. Furthermore, I factored some data and methods common to all collections, such as self.length and __len__, into an AbstractCollection class. Now, abstract classes for specific collections, such as AbstractBag, can inherit from the AbstractCollection class. The process of factoring common methods and data into abstract super classes reduces redundancy in implementations. Abstract classes, like interfaces, are not meant to be instantiated. However, unlike interfaces, abstract classes do contain implementation code. That being said, they are not complete.

Some python files that were implemented for learning purposes in earlier chapters of the data structures book can be found in the python_scrapbook directory. Some files in there won't work without dependencies, but I don't want them cluttering up the data-structures directory.

Standalone c files, minimal as they are (I don't honestly know any C), can be found in the c_scrapbook directory.

The meat and potatoes of this repository is in the collectionframework directory, where I implement a host of different collection types. There are also interfaces and abstract classes, the former live in the interfaces directory; it contains commented specifications, or blueprints, for each concrete class. The abstractclasses directory contains abstract classes; these are used to factor common methods and data from concrete classes so that they may simply inherit from the relevant abstract class.

Finally, there's the collectiontesting directory; it contains unit testing modules for each concrete class.

