# Creational Design Patterns

A clear, practical guide to the **five Creational Design Patterns** from the Gang of Four (GoF), with Python examples and interview notes.

Creational patterns deal with **how objects are created**. They help keep object creation flexible, reusable, and separate from the rest of an application.

## Table of Contents

1. [Why Creational Patterns?](#why-creational-patterns)
2. [Singleton](#1-singleton-pattern)
3. [Factory Method](#2-factory-method-pattern)
4. [Abstract Factory](#3-abstract-factory-pattern)
5. [Builder](#4-builder-pattern)
6. [Prototype](#5-prototype-pattern)
7. [Quick Comparison](#quick-comparison)
8. [How to Choose a Pattern](#how-to-choose-a-pattern)
9. [Interview Revision Questions](#interview-revision-questions)

---

## Why Creational Patterns?

Suppose an application creates database connections, payment services, reports, or complex objects.

If object creation is scattered throughout the code:

- Changing the creation process becomes difficult.
- Business logic becomes tightly coupled to concrete classes.
- Creating related objects consistently is harder.
- Complex constructors can become difficult to maintain.

Creational patterns address these problems by giving object creation a clear structure.

---

## 1. Singleton Pattern

### Intent

Ensure that a class has **only one instance** and provide a single, globally accessible way to access it.

### Real-world example

An application-wide configuration manager or a shared logger.

### Python example

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True
```

### How it works

1. `__new__()` controls object creation in Python.
2. The first call creates an instance and stores it in `_instance`.
3. Later calls return the already-created instance.
4. Both variables therefore refer to the same object.

### When to use it

- Shared application configuration.
- A process-wide logger.
- A carefully managed shared resource.

### Advantages

- Controls the number of instances.
- Provides a shared access point.
- Can avoid repeated initialization of an expensive resource.

### Disadvantages

- Introduces global state.
- Can make unit testing and dependency management harder.
- Requires additional care in multithreaded applications.

### Interview takeaway

**Singleton controls how many instances of a class can exist.**

> Note: This is a simple, single-threaded demonstration. Production implementations may need thread-safety, lifecycle management, and dependency injection considerations.

---

## 2. Factory Method Pattern

### Intent

Define an interface for creating an object, while allowing subclasses to decide which concrete object to create.

### Real-world example

A notification system that can create Email, SMS, or Push notifications.

### Python example

```python
from abc import ABC, abstractmethod


# Product interface
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Concrete products
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS: {message}")


# Creator
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def notify(self, message):
        notification = self.create_notification()
        notification.send(message)


# Concrete creators
class EmailFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()


class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()


email_service = EmailFactory()
email_service.notify("Your order has shipped!")

sms_service = SMSFactory()
sms_service.notify("Your OTP is 1234")
```

### How it works

1. `Notification` defines the common product interface.
2. Email and SMS classes implement that interface.
3. The creator declares the factory method `create_notification()`.
4. Concrete factories decide which notification object to instantiate.
5. Client code uses the creator without directly constructing the concrete product.

### When to use it

- The exact product type depends on a subclass or runtime choice.
- You want to avoid scattering concrete class construction throughout the code.
- You expect new product types to be introduced.

### Advantages

- Reduces coupling between client code and concrete products.
- Makes adding new product types easier.
- Separates object creation from business operations.

### Disadvantages

- Introduces additional classes.
- Can be excessive for a small application with only one or two simple products.

### Interview takeaway

**Factory Method delegates object creation to subclasses.**

---

## 3. Abstract Factory Pattern

### Intent

Provide an interface for creating **families of related objects** without specifying their concrete classes.

### Real-world example

A cross-platform UI application that creates matching Windows or Mac buttons and checkboxes.

### Python example

```python
from abc import ABC, abstractmethod


# Abstract products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


# Windows products
class WindowsButton(Button):
    def render(self):
        print("Rendering Windows button")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering Windows checkbox")


# Mac products
class MacButton(Button):
    def render(self):
        print("Rendering Mac button")


class MacCheckbox(Checkbox):
    def render(self):
        print("Rendering Mac checkbox")


# Abstract factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Concrete factories
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Client code
def render_ui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()


render_ui(WindowsFactory())
render_ui(MacFactory())
```

### How it works

1. Abstract product interfaces define the objects that can be created.
2. Concrete products implement those interfaces for each platform.
3. The abstract factory declares methods for creating each product.
4. Each concrete factory creates a compatible family of products.
5. Client code works with the abstract factory and product interfaces.

### When to use it

- You need multiple families of related objects.
- Products in a family must be compatible with one another.
- You want to switch between product families without changing client code.

### Advantages

- Keeps related products consistent.
- Hides concrete product classes from client code.
- Makes switching product families straightforward.

### Disadvantages

- Adding a new product type means changing the abstract factory and its concrete implementations.
- Can introduce many interfaces and classes.

### Interview takeaway

**Abstract Factory creates families of related objects.**

---

## 4. Builder Pattern

### Intent

Separate the construction of a complex object from its representation, so the same construction process can create different configurations.

### Real-world example

Building a burger meal with different buns, patties, toppings, sides, and drinks.

### Python example

```python
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BurgerMeal:
    bun_type: str
    patty: str
    has_cheese: bool
    toppings: tuple
    side: Optional[str]
    drink: Optional[str]


class BurgerBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.bun_type = "Regular"
        self.patty = "Veg"
        self.has_cheese = False
        self.toppings = []
        self.side = None
        self.drink = None
        return self

    def set_bun(self, bun):
        self.bun_type = bun
        return self

    def set_patty(self, patty):
        self.patty = patty
        return self

    def add_cheese(self):
        self.has_cheese = True
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def set_side(self, side):
        self.side = side
        return self

    def set_drink(self, drink):
        self.drink = drink
        return self

    def build(self):
        return BurgerMeal(
            bun_type=self.bun_type,
            patty=self.patty,
            has_cheese=self.has_cheese,
            toppings=tuple(self.toppings),
            side=self.side,
            drink=self.drink
        )


builder = BurgerBuilder()

meal = (
    builder
    .set_bun("Sesame")
    .set_patty("Paneer")
    .add_cheese()
    .add_topping("Lettuce")
    .add_topping("Tomato")
    .set_side("Fries")
    .set_drink("Cold Coffee")
    .build()
)

print(meal)
```

### How it works

1. The builder maintains the intermediate construction state.
2. Each method configures one part of the object.
3. Returning `self` enables method chaining.
4. `build()` creates the final object.
5. The final `BurgerMeal` is immutable in this example.

### When to use it

- An object has many optional fields.
- Constructors have too many parameters.
- You need different configurations of the same complex object.
- You want construction steps to be readable.

### Advantages

- Avoids long, confusing constructors.
- Makes object creation readable.
- Supports different configurations.
- Separates construction logic from the final object.

### Disadvantages

- Requires additional builder code.
- May be unnecessary for simple objects.

### Interview takeaway

**Builder constructs a complex object step by step.**

---

## 5. Prototype Pattern

### Intent

Create new objects by copying an existing object (the prototype), instead of constructing a new object from scratch.

### Real-world example

Creating multiple document templates or game characters based on an existing configured character.

### Python example

```python
import copy


class GameCharacter:
    def __init__(self, name, health, weapons):
        self.name = name
        self.health = health
        self.weapons = weapons

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Weapons: {self.weapons}"
        )


original = GameCharacter(
    "Warrior",
    100,
    ["Sword", "Shield"]
)

# Shallow copy
shallow_clone = copy.copy(original)

# Deep copy
deep_clone = copy.deepcopy(original)

deep_clone.name = "Elite Warrior"
deep_clone.weapons.append("Bow")

print("Original:", original)
print("Shallow clone:", shallow_clone)
print("Deep clone:", deep_clone)
```

### How it works

1. Create and configure an original object.
2. Copy that object to create another instance.
3. Modify the copied object as required.
4. Choose shallow or deep copying based on whether nested objects should be shared.

### Shallow copy vs Deep copy

| Shallow copy | Deep copy |
|---|---|
| Copies the outer object | Recursively copies nested objects |
| Nested mutable objects may be shared | Nested objects are copied |
| Uses `copy.copy()` | Uses `copy.deepcopy()` |

### When to use it

- Object creation is expensive.
- Many objects share a common initial configuration.
- You need copies of existing objects with small modifications.

### Advantages

- Can reduce repeated initialization work.
- Makes it easy to create configured variations.
- Avoids rebuilding complex objects from scratch.

### Disadvantages

- Copying nested mutable objects requires care.
- Deep copying can be expensive.
- Some objects cannot be safely copied without custom logic.

### Interview takeaway

**Prototype creates new objects by cloning existing objects.**

---

## Quick Comparison

| Pattern | Main purpose | Simple example |
|---|---|---|
| Singleton | One shared instance | Logger |
| Factory Method | Delegate creation to subclasses | Email or SMS notification |
| Abstract Factory | Create related product families | Windows or Mac UI |
| Builder | Construct a complex object step by step | Burger meal |
| Prototype | Create objects by copying | Game character clone |

## How to Choose a Pattern

Ask yourself:

- **Need exactly one shared instance?** → Singleton
- **Need subclasses to decide which object to create?** → Factory Method
- **Need a matching family of related objects?** → Abstract Factory
- **Need to construct an object with many optional parts?** → Builder
- **Need to create objects by copying existing ones?** → Prototype

## Interview Revision Questions

Try answering these without looking at the explanations:

1. What problem does the Singleton pattern solve?
2. How is Factory Method different from Abstract Factory?
3. Why does Abstract Factory create product families?
4. When would you choose Builder over a constructor?
5. What is the difference between shallow copy and deep copy?
6. Which pattern would you use for a cross-platform UI?
7. Which pattern would you use for creating different payment methods?
8. What are the disadvantages of Singleton?
9. Can Builder create immutable objects?
10. Give one real-world example for each creational pattern.

---

## Key Takeaway

Creational patterns are about **controlling and organizing object creation**.

Remember the five ideas:

- Singleton — one instance.
- Factory Method — subclasses decide what to create.
- Abstract Factory — create related families of objects.
- Builder — construct step by step.
- Prototype — clone an existing object.

The goal is not to use a design pattern everywhere. Choose one when it makes the code easier to extend, test, and maintain.
