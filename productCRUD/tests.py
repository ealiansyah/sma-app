from django.test import TestCase
from unittest.mock import Mock, MagicMock
import json
from .models import Product, Product_Category
from .views import create_product, update_product, get_product, delete_product

class ProductCRUDTestCase(TestCase):

    def setUp(self):
        Product_Category.objects.create(nama_kategori="Beverage", deskripsi="Drinks and refreshments")
        Product_Category.objects.create(nama_kategori="Snacks", deskripsi="Snacks and bites")


    def test_create_get_product(self):
        """Created product has the wanted attributes"""

        name = "Lays"
        barcode_id = "thisisbarcodeid"
        snack_category = "Snacks"

        req = Mock()
        req.method = "POST"
        req.body = {
            "name": name,
            "barcode_id": barcode_id,
            "category": snack_category
        }
        req.body = json.dumps(req.body)
        res = create_product(req)

        self.assertEqual(res.status_code, 201)

        req.method = "GET"
        req.GET = {
            "name": name
        }
        res = get_product(req)
        res = json.loads(res.content)

        self.assertTrue(len(res) == 1)
        self.assertEqual(res[0]['name'], name)
        self.assertEqual(res[0]['barcode_id'], barcode_id)
        self.assertEqual(res[0]['category'], snack_category)
        
    def test_failed_create_product(self):
        """Failed to create product over missing attributes"""

        barcode_id = "thisisbarcodeid"
        snack_category = "Snacks"

        req = Mock()
        req.method = "POST"
        req.body = {
            "barcode_id": barcode_id,
            "snack_category": snack_category
        }
        req.body = json.dumps(req.body)
        res = create_product(req)

        self.assertEqual(res.status_code, 400)


    def test_update_product(self):
        """Updated field is updated accordingly"""

        name = "Lays"
        updated_name = "Chitato"
        barcode_id = "thisisbarcodeid"
        snack_category = "Snacks"

        # CREATE
        req = Mock()
        req.method = "POST"
        req.body = {
            "name": name,
            "barcode_id": barcode_id,
            "category": snack_category
        }
        req.body = json.dumps(req.body)
        res = create_product(req)

        self.assertEqual(res.status_code, 201)

        # UPDATE
        req.body = {
            "name": updated_name,
            "barcode_id": barcode_id
        }
        req.body = json.dumps(req.body)
        res = update_product(req)
        
        self.assertEqual(res.status_code, 200)

        # GET empty
        req.method = "GET"
        req.GET = {
            "name": name
        }
        res = get_product(req)
        res = json.loads(res.content)

        self.assertTrue(len(res) == 0)

        # GET one
        req.GET = {
            "name": updated_name
        }
        res = get_product(req)
        res = json.loads(res.content)

        self.assertTrue(len(res) == 1)
        self.assertEqual(res[0]['name'], updated_name)
        self.assertEqual(res[0]['barcode_id'], barcode_id)
        self.assertEqual(res[0]['category'], snack_category)
        

    def test_delete_product(self):
        """Product is deleted accordingly"""

        name = "Lays"
        barcode_id = "thisisbarcodeid"
        snack_category = "Snacks"
    
        # CREATE
        req = Mock()
        req.method = "POST"
        req.body = {
            "name": name,
            "barcode_id": barcode_id,
            "category": snack_category
        }
        req.body = json.dumps(req.body)
        res = create_product(req)

        self.assertEqual(res.status_code, 201)

        # DELETE
        req.body = {
            "barcode_id": barcode_id
        }
        req.body = json.dumps(req.body)
        res = delete_product(req)
        
        self.assertEqual(res.status_code, 200)

        # GET
        req.method = "GET"
        req.GET = {
            "name": name
        }
        res = get_product(req)
        res = json.loads(res.content)

        self.assertTrue(len(res) == 0)
