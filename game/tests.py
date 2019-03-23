from django.test import TestCase
from .models import GameGenre, Reviews, GameE
vent
from .forms import ResourceForm, MeetingForm
from datetime import datetime
from django.urls import reverse

### Class tests ###
# test Game class
class GameTest(TestCase):
    def test_stringOutput(self):
        games=Games(gamegenres='Gamer member party')
        self.assertEqual(str(games), games.games)
    def test_tablename(self):
        self.assertEqual(str(Games._meta.db_table), 'games')

# test Review class
class ReviewTest(TestCase):
    def test_stringOutput(self):
        review=Review(reviewname='review')
        self.assertEqual(str(review), review.reviewname)
    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')
    
# test GameEvent class
class GameEventTest(TestCase):
    def test_stringOutput(self):
        gameevent=GameEvent(gameeventtitle='game event title')
        self.assertEqual(str(event), gameevent.gameeventtitle)
    def test_tablename(self):
        self.assertEqual(str(GameEvent._meta.db_table), 'gameevent')


### View tests ###
# testing index view
class TestIndexView(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'game/index.html')

# testing details view
class TestResourceView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/reviews')
        self.assertEqual(response.status_code, 200)
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('reviews'))
        self.assertTemplateUsed(response, 'game/reviews.html')

# testing game genre view
class TestGameGenreView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/game/games')
        self.assertEqual(response.status_code, 200)
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('games'))
        self.assertTemplateUsed(response, 'game/games.html')


### Form tests ###
# testing add review form
class New_Review_Form_Test(TestCase):
    def test_resourceForm_is_valid(self):
        form = ReviewForm(data={'reviewname': "Pokemon Snap Review", 'reviewtype': "review", 'resourceurl': "http://www.google.com", 'dateentered': "2019-01-30", 'user':"sarah", 'reviewdescription':"Events that Gamer members may be interested in" })
        self.assertTrue(form.is_valid())
