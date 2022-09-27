# mdl_product

# Python/Django Developer Assignment

## SETUP
   ** Create virtual env and install all dependencies from 
      requirements.txt.
      
   ** Create at least 3 user by "python manage.py createsuperuser"
      (like: admin@gmail.com / vendors@gmail.com / customer@gmail.com)
      and update the role_id(admin role_id = 999, vendors role_id = 88
      , customer role_id = 3) of User model by using 
      http://localhost:8000/admin/login/?next=/admin/
      
   ** weather (title, weather_type)->([cold,1] [normal,2] [hot,3])
   
## POSTMAN 
   login(POST): http://127.0.0.1:8000/auth/api/login
   
   json-> {
            "email": "admin@gmail.com",
            "password" : "xxxxxxxx"
          }

    Then you get the access token..................

## vendors (role_id = 88)
   1. CRUD products with the quantity of the product.
    
    Create(POST): http://127.0.0.1:8000/mdl/product/create
    json -> {
                "name": "Product10",
                "price": 500.0,
                "detail_text":"Product10 Product10 Product10",
                "quantity": 2,
                "weather_type": 2
            }

    Read(GET): http://127.0.0.1:8000/mdl/product 
               http://127.0.0.1:8000/mdl/product/details/(id)   
    
    Update(PUT): http://127.0.0.1:8000/mdl/product/details/(id)   
    json-> {
                "name": "Product10",
                "price": 500.0,
                "detail_text":"Product10 Product10 Product10 Product10",
                "quantity": 2,
                "weather_type": 1

            }  

    Delete(DELETE): http://127.0.0.1:8000/mdl/product/details/(id)

    
## admin (role_id = 999)
   1. CRUD product
   
    Create(POST): http://127.0.0.1:8000/mdl/product/create
    json -> {
                "name": "Product10",
                "price": 500.0,
                "detail_text":"Product10 Product10 Product10",
                "quantity": 2,
                "weather_type": 2
            }

    Read(GET): http://127.0.0.1:8000/mdl/product 
               http://127.0.0.1:8000/mdl/product/details/(id)   
    
    Update(PUT): http://127.0.0.1:8000/mdl/product/details/(id)   
    json->  {
                "name": "Product10",
                "price": 500.0,
                "detail_text":"Product10 Product10 Product10 Product10",
                "quantity": 2,
                "weather_type": 1

            }  

    Delete(DELETE): http://127.0.0.1:8000/mdl/product/details/(id)
   2. CRUD weather
   
    Create(POST): http://127.0.0.1:8000/mdl/weather
    json->  {
                "weather_type": 1,
                "title": "Cold",
                "low_range": -186.0,
                "high_range": 5.0

            }

    Read(GET): http://127.0.0.1:8000/mdl/weather
               http://127.0.0.1:8000/mdl/weather/details/(cold/normal/hot)

    Update(PUT): http://127.0.0.1:8000/mdl/weather/details/(cold/normal/hot)
    json->  {
                <!-- "weather_type": 1,
                "title": "Cold", -->
                "low_range": -185.0,
                "high_range": 5.0

            }

    Delete(DELETE): http://127.0.0.1:8000/mdl/weather/details/(cold/normal/hot)

   3. Set temperature range(high, low) for each weather type
   
    URL(PUT): http://127.0.0.1:8000/mdl/weather/details/(cold/normal/hot)
    json->  {
                "low_range": -185.0,
                "high_range": 5.0

            }

## customer (role_id = 3)
   1. See all the products
   
    URL(GET): http://127.0.0.1:8000/mdl/product
 
   2. See product recommendations depending on the
current weather condition

    URL(GET): http://127.0.0.1:8000/mdl/home

   3. search for products using the product's name 
   
    URL(GET): http://127.0.0.1:8000/mdl/product/(product_name)
      
   4. search for products using the weather type
    
    URL(GET): http://127.0.0.1:8000/mdl/product/weather/(cold/normal/hot)
