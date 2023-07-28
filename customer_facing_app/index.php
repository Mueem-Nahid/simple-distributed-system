<!DOCTYPE html>
<html>

<head>
   <title>Customer-Facing Web App</title>
</head>

<body>
   <h1>Welcome to Our E-commerce Store</h1>

   <h2>Products for Sale:</h2>

   <?php
   // Fetch data from the Flask web framework API
   $api_url = 'http://web_framework:5003/'; // Replace 'web_framework' with the actual service name in Docker Compose
   $data = file_get_contents($api_url);
   $products = json_decode($data, true);

   // Display products in a table
   echo '<table border="1">';
   echo '<tr><th>Product Name</th><th>Quantity</th><th>Price</th></tr>';
   foreach ($products['products'] as $product) {
      echo '<tr>';
      echo '<td>' . $product['name'] . '</td>';
      echo '<td>' . $product['qty'] . '</td>';
      echo '<td>' . $product['price'] . '</td>';
      echo '</tr>';
   }
   echo '</table>';
   ?>

</body>

</html>