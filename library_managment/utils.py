def change_book_status(save_form):
    if save_form:
        book_id = save_form.pk
        ord_book = Book.objects.get(pk=book_id)
        if ord_book.in_order == False:
            ord_book.in_order = True
        else:
            ord_book.in_order = False
        ord_book.save()