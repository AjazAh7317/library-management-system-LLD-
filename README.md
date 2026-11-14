# Library Management System — Python LLD

A small, modular Library Management System built with Python and object-oriented design. It supports book and member management, issuing and returning books, availability tracking, and issue history.

## Problem statement

Build a system that can:
- Add and list books.
- Register and list members.
- Issue an available book to a registered member.
- Return a book.
- Track whether a book is `AVAILABLE` or `ISSUED`.
- Prevent issuing an already-issued book and prevent an incorrect member from returning it.

## Project structure

```text
library-management-system/
├── enums/
│   └── book_status.py
├── models/
│   ├── book.py
│   ├── member.py
│   └── issue.py
├── repositories/
│   ├── interfaces.py
│   └── in_memory.py
├── services/
│   ├── book_service.py
│   ├── member_service.py
│   └── library_service.py
├── tests/
│   └── test_library.py
├── main.py
└── README.md
```

## Design overview

The project uses three simple layers:

1. **Models** represent domain objects (`Book`, `Member`, and `Issue`).
2. **Repositories** handle storage and retrieval. The included implementation stores data in memory using dictionaries.
3. **Services** implement business rules such as registering members, adding books, issuing books, and returning books.

`main.py` creates the repositories and injects them into the services. This is a basic example of dependency injection.

## Key classes

| Class | Responsibility |
|---|---|
| `Book` | Book details and status transitions |
| `Member` | Member identity and contact details |
| `Issue` | Loan record, due date, and return date |
| `BookStatus` | `AVAILABLE` / `ISSUED` values |
| `InMemoryBookRepository` | Stores and retrieves books |
| `InMemoryMemberRepository` | Stores and retrieves members |
| `InMemoryIssueRepository` | Stores issue history and finds active loans |
| `BookService` | Adds, finds, and lists books |
| `MemberService` | Registers, finds, and lists members |
| `LibraryService` | Applies issue and return business rules |

## SOLID and OOP concepts

- **Single Responsibility Principle:** Models, repositories, and services have separate responsibilities.
- **Open/Closed Principle:** A different repository implementation (for example, a database repository) can be added without rewriting the service business rules.
- **Liskov Substitution Principle:** Alternative repository implementations can be used as long as they honor the repository contracts.
- **Interface Segregation Principle:** Repository contracts are separated by resource.
- **Dependency Inversion Principle:** Services receive repository dependencies instead of creating their own storage objects. The contracts are described with Python `Protocol`.
- **Encapsulation:** Book status changes go through `mark_issued()` and `mark_available()` methods.

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Run the application

Open a terminal in the project directory and run:

```bash
python main.py
```

On Windows PowerShell, the same command works:

```powershell
python main.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Notes and possible extensions

This starter implementation uses in-memory storage, so data resets when the program exits. It is suitable for demonstrating the LLD assignment without requiring database setup.

Possible extensions:
- Persist records using SQLite or MySQL.
- Add fine calculation for overdue returns.
- Add book search and update/delete operations.
- Add member borrowing limits and reservation/waitlist support.
- Add a CLI menu or REST API.
