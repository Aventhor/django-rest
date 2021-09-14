from django.db import models


class Book(models.Model):
    sku = models.CharField(max_length=100, verbose_name='SKU')
    name = models.CharField(max_length=256, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='book_authors',
                                  verbose_name='Автор')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genres = models.ManyToManyField('Genre', verbose_name='Жанры', blank=True, related_name='book_genres')
    publish_date = models.DateField(verbose_name='Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ('-created_at',)

