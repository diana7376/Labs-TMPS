// Abstraction for notification (DIP)
public interface INotifier
{
    void Send(string message);
}

// Implementation of Notifier - Email (OCP)
public class EmailNotifier : INotifier
{
    public override void Send(string message)
    {
        Console.WriteLine("Email sent: " + message);
    }
}

// Implementation of Notifier - SMS (OCP)
public class SmsNotifier : INotifier
{
    public override void Send(string message)
    {
        Console.WriteLine("SMS sent: " + message);
    }
}

// User Registration - SRP
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

// Usage
class Program
{
    static void Main()
    {
        INotifier notifier = new EmailNotifier(); // Change to SmsNotifier to extend
        var registration = new UserRegistration(notifier);
        registration.Register("Alice");
    }
}
