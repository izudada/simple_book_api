from rest_framework import serializers

from book.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title', 'author', 'publication_date', 'isbn', 'genre', 'price', 'stock', 'qty_sold', 'qty_left')
        read_only_fields = ('id', 'qty_sold', 'qty_left') 

    def create(self, validated_data):
        return Book.objects.create(
            qty_left=validated_data.get("stock"),
            **validated_data
        )
    