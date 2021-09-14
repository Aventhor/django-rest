from rest_framework.routers import DefaultRouter

from store.views import GenreView, AuthorView, BookView


router = DefaultRouter()

router.register(r'genres', GenreView)
router.register(r'authors', AuthorView)
router.register(r'books', BookView)

urlpatterns = [
    *router.urls,
]
