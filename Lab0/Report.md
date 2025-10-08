# SOLID Principles

## Purpose
This report explores the implementation of three SOLID principles—**Single Responsibility**, **Open/Closed**, and **Dependency Inversion**—in a simple C# code example. The goal is to demonstrate how SOLID helps structure maintainable and extensible software.

## What is SOLID?
**SOLID** is an acronym for five design principles that improve software structure and maintainability:

- **S**ingle Responsibility Principle (SRP): Each class should have one job.
- **O**pen/Closed Principle (OCP): Classes should be open for extension but closed for modification.
- **L**iskov Substitution Principle (LSP): Subtypes should replace the supertype without changing behavior.
- **I**nterface Segregation Principle (ISP): Don't force clients to depend on methods they don't use.
- **D**ependency Inversion Principle (DIP): Depend on abstractions, not concrete classes.

## Idea
I implement a user registration system that sends notifications. Each SOLID principle is represented by specific parts of the design to show the benefits of separation, extensibility, and abstraction.

***

## Principles Implemented

### 1. Single Responsibility Principle (SRP)
**What it means:** Each class should do only one thing.

**Implementation:**
- The `UserRegistration` class is responsible *only* for registering users.
- Notification logic is moved to separate notifier classes.

**Code Snippet:**
```csharp
public class UserRegistration
{
    private readonly INotifier _notifier;

    public UserRegistration(INotifier notifier)
    {
        _notifier = notifier;
    }

    public void Register(string username)
    {
        // Register user logic
        Console.WriteLine($"{username} registered.");
        _notifier.Send($"{username} registration successful!");
    }
}
```

***

### 2. Open/Closed Principle (OCP)
**What it means:** Classes can be extended, but their source code shouldn't need to be changed.

**Implementation:**
- The `INotifier` interface allows new notification types to be added (like SMS, email) without modifying `UserRegistration`.

**Code Snippet:**
```csharp
public interface INotifier
{
    void Send(string message);
}

public class EmailNotifier : INotifier
{
    public void Send(string message)
    {
        Console.WriteLine("Email sent: " + message);
    }
}

public class SmsNotifier : INotifier
{
    public void Send(string message)
    {
        Console.WriteLine("SMS sent: " + message);
    }
}
```

***

### 3. Dependency Inversion Principle (DIP)
**What it means:** Depend on interfaces or abstractions, not concrete implementations.

**Implementation:**
- `UserRegistration` only knows about the `INotifier` abstraction, not about specific notifier types.
- You can change the notifier without affecting `UserRegistration`.

**Code Snippet:**
```csharp
INotifier notifier = new EmailNotifier(); // Can swap to SmsNotifier, etc.
var registration = new UserRegistration(notifier);
registration.Register("Alice");
```

***



## Conclusion
By following SOLID principles in this example, you get code that is easier to maintain, extend, and test. You can add new notification methods or change business rules without breaking existing functionality. Applying even just a few SOLID principles in your design helps keep your codebase *robust* and *clean*.