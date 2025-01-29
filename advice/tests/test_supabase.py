import unittest
from app.supabase_client import get_supabase_client

class TestSupabase(unittest.TestCase):

    def setUp(self):
        self.client = get_supabase_client()

    def test_connection(self):
        """Teste si le client Supabase est bien initialisé."""
        self.assertIsNotNone(self.client)

    def test_get_data(self):
        """Teste la récupération des données depuis Supabase."""
        response = self.client.table('example_table').select("*").execute()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_insert_data(self):
        """Teste l'insertion de données dans Supabase."""
        response = self.client.table('example_table').insert({"name": "Test Item"}).execute()
        self.assertEqual(response.status_code, 201)