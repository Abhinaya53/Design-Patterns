# Problem:
Suppose we are designing a file system. In a file system, we have files and directories. A directory can contain files as well as other directories. We want to represent this hierarchical structure in our design. We also want to perform operations like calculating the total size of a directory, listing all files in a directory, etc. 

# Naive Approach:
A naive approach would be to create separate classes for File and Directory. The File class would have attributes like name and size, while the Directory class would have a list of files and directories it contains along with name and size. The problems with this approach are:
- Both File and Directory classes would have similar methods like get_size() and get_details(), leading to code duplication.
- The Directory class would need to handle both files and directories, leading to complex code which violates SRP.
- Adding new types of file system components (like symbolic links) would require changes in multiple places which violates OCP.
- Dependency on concrete classes rather than abstractions, violating DIP.
- Client code would need to differentiate between files and directories, leading to complex conditionals, violating ISP.

# Solution: Composite Pattern
Composite solves this by:
- Defining a common interface (Component) for both File and Directory.
- Implementing the common interface in both File and Directory classes.
- The Directory class can contain a list of Components (both Files and Directories), allowing for a tree structure.
- Client code can treat both Files and Directories uniformly through the Component interface.
- Adding new types of components becomes easier as they just need to implement the Component interface. OCP is maintained.
- The design adheres to SOLID principles by promoting code reuse, reducing complexity, and ensuring that classes have single responsibilities.