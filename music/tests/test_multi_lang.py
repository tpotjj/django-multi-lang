from rest_framework.test import APIClient, APITestCase

from music.models import Annotation, Term


class TestTermViewSet(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email = "sunny.choi.education@gmail.com", password = make_password("CleferMusic1!"))
        term = Term.objects.create(name = "term")
        annotation  = Annotation.objects.create(parent_term = term, term = "term but in us", locale="en-US", explanation = 'some explanation for the term')
        annotation = Annotation.objects.create(parent_term = term, term = "term but in uk", locale="en-GB")

    def test_fallback_to_default_locale_when_client_defined_locale_does_not_have_annotation(self):
        client = APIClient()
        client.credentials(HTTP_ACCEPT_LANGUAGE='en-GT')
        client.force_authenticate(user=self.user)
        response = client.get('/api/v1/terms/term/')
        self.assertEquals(response.data['data']['annotations'][0]['locale'], 'en-US')

    def test_get_annotation_in_client_defined_locale_if_it_exists(self):
        client = APIClient()
        client.credentials(HTTP_ACCEPT_LANGUAGE='en-GB')
        client.force_authenticate(user=self.user)
        response = client.get('/api/v1/terms/term/')
        self.assertEquals(response.data['data']['annotations'][0]['locale'], 'en-GB')
    
    def test_fallback_to_default_locale_if_client_locale_unknown(self):
        client = APIClient()
        client.credentials(HTTP_ACCEPT_LANGUAGE='en-GT;fr-CH;de-CH')
        client.force_authenticate(user=self.user)
        response = client.get('/api/v1/terms/term/')
        # fall back on en-US since non of the languages is known
        self.assertEquals(response.data['data']['annotations'][0]['locale'], 'en-US')
