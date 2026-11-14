
from repositories.in_memory import (
    InMemoryBookRepository,
    InMemoryMemberRepository,
    InMemoryIssueRepository
)

from services.book_service import BookService
from services.member_service import MemberService
from services.library_service import LibraryService


def main():

    # Creating repository objects to store library data
    book_repo = InMemoryBookRepository()
    member_repo = InMemoryMemberRepository()
    issue_repo = InMemoryIssueRepository()

    # Creating service objects
    book_service = BookService(book_repo)
    member_service = MemberService(member_repo)

    library_service = LibraryService(
        book_repo,
        member_repo,
        issue_repo
    )

    # Adding books to the library
    print("\n--- Adding Books ---")

    book_service.add_book("B1", "Clean Code", "Robert C. Martin")
    book_service.add_book("B2", "Design Patterns", "Gang of Four")
    book_service.add_book(
        "B3",
        "The Pragmatic Programmer",
        "Andrew Hunt and David Thomas"
    )

    print("Books added successfully!")

    # Registering library members
    print("\n--- Registering Members ---")

    member_service.register_member(
        "M1", "Ajaz", "ajaz@example.com"
    )

    member_service.register_member(
        "M2", "Rahul", "rahul@example.com"
    )

    print("Members registered successfully!")

    # Displaying all books
    print("\n--- Available Books ---")
    display_books(book_service)

    # Issuing a book to a member
    print("\n--- Issuing Book ---")

    try:
        issue = library_service.issue_book("B1", "M1")

        print("Book issued successfully!")
        print("Issue ID:", issue.issue_id)
        print("Due Date:", issue.due_date)

    except ValueError as e:
        print("Error:", e)

    # Trying to issue the same book to another member
    print("\n--- Trying to Issue the Same Book Again ---")

    try:
        library_service.issue_book("B1", "M2")

    except ValueError as e:
        print("Cannot issue book:", e)

    # Returning the issued book
    print("\n--- Returning Book ---")

    try:
        returned_book = library_service.return_book("B1", "M1")

        print("Book returned successfully!")
        print("Return Date:", returned_book.return_date)

    except ValueError as e:
        print("Error:", e)

    # Displaying books after the return
    print("\n--- Updated Book List ---")
    display_books(book_service)

    # Displaying complete issue history
    print("\n--- Issue History ---")

    issues = library_service.list_issues()

    for issue in issues:

        if issue.is_active:
            status = "Currently Issued"
        else:
            status = "Returned"

        print(
            "Issue ID:", issue.issue_id,
            "| Book ID:", issue.book_id,
            "| Member ID:", issue.member_id,
            "| Status:", status
        )


# Function to display all books
def display_books(book_service):

    books = book_service.list_books()

    for book in books:
        print(
            f"{book.book_id} - {book.title} "
            f"by {book.author} - {book.status.value}"
        )


if __name__ == "__main__":
    main()
