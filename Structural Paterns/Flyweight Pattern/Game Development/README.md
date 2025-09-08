# Problem:
Suppose you are developing a shooting game where players shoot each other with bullets. Each bullet has properties like color, position (x, y) and velocity. In a typical game, there can be thousands of bullets on the screen at any given time. 

# Naive Approach:
Creating a new bullet object for each bullet. The problems with this approach are:
- Memory Consumption: Each bullet object consumes memory. With thousands of bullets, this can lead to high memory consumption and performance issues.
- Performance Overhead: Creating and destroying many objects can lead to performance overhead due to frequent garbage collection.
- Redundant Data: Many bullets may share the same properties (like color) leading to redundant data storage.

# Solution: Flyweight Pattern
The Flyweight Pattern helps to minimize memory usage by sharing as much data as possible with similar objects. In this case, we can separate the intrinsic properties (shared) from the extrinsic properties (unique to each bullet).
- Intrinsic Properties: These are properties that can be shared among multiple bullets, such as color.
- Extrinsic Properties: These are properties that are unique to each bullet, such as position (x, y) and velocity.
- Furthermore, we can implement factory method pattern here by creating a class called FlyweightFactory (in this case BulletTypeFactory) for managing the creation and sharing of flyweight objects (in this case, bullet colors).
- The BulletTypeFactory will maintain a pool of BulletType objects (flyweights) and will return an existing object if it already exists, or create a new one if it doesn't.
- This way, we can significantly reduce memory consumption by sharing the intrinsic properties among multiple bullet instances.