<!DOCTYPE html>
<html>

<head>
   <title>Admin Dashboard</title>
</head>

<body>
   <h1>Welcome to the Admin Dashboard</h1>
   <h2>Add New Product</h2>
   <form id="addProductForm" method="POST">
      <label for="product_name">Product Name:</label>
      <input type="text" id="product_name" name="product_name" required><br><br>

      <label for="quantity">Quantity:</label>
      <input type="number" id="quantity" name="quantity" required><br><br>

      <label for="price">Price:</label>
      <input type="number" step="0.01" id="price" name="price" required><br><br>

      <input type="submit" value="Add Product">
   </form>

   <h2>Update Quantity</h2>
   <form id="updateQuantityForm" method="POST">
      <label for="product_name">Product Name:</label>
      <input type="text" id="product_name" name="product_name" required><br><br>

      <label for="new_quantity">New Quantity:</label>
      <input type="number" id="new_quantity" name="new_quantity" required><br><br>

      <input type="submit" value="Update Quantity">
   </form>

   <script>
      // Function to handle form submission and make API requests
      async function handleSubmit(endpoint) {
         console.log("====", endpoint);
         const form = document.getElementById(endpoint + "Form"); // Get the form element
         const product_name = document.getElementById("product_name").value;
         const quantity = document.getElementById("quantity").value;
         const price = document.getElementById("price").value;

         const data = {
            product_name: product_name,
            quantity: parseInt(quantity),
            price: parseFloat(price)
         };

         console.log("====", data);
         const response = await fetch("/" + endpoint, {
            method: "POST",
            headers: {
               "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
         });

         if (response.ok) {
            alert("Success: Product " + (endpoint === "add_product" ? "added" : "quantity updated") + " successfully!");
         } else {
            const data = await response.json();
            alert("Error: " + data.error);
         }
      }

      document.getElementById("addProductForm").addEventListener("submit", function(event) {
         event.preventDefault();
         handleSubmit("add_product");
      });

      document.getElementById("updateQuantityForm").addEventListener("submit", function(event) {
         event.preventDefault();
         handleSubmit("update_quantity");
      });
   </script>
</body>

</html>