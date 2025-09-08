# Problem:
Design a File I/O System for a software application.
- At the core, there is a simple file reader/writer that reads/writes plain text.
- Some use cases require extra functionality to be applied dynamically, such as:
    - Encryption of data before writing / after reading.
    - Compression of data before writing / after reading.
    - Buffering to improve performance.
- The system should allow combining these behaviors (e.g., a file could be compressed + encrypted).
- New functionalities should be easy to add without modifying existing code.