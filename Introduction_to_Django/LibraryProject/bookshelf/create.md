
Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.:
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Save the new instance:
new_book.save()
Verify the new instance:
new_book.id 
new_book.title
new_book.publication_year