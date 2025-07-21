<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Ecommerce FastAPI Project</title>
</head>
<body>
  <h1>🛒 Ecommerce API - FastAPI + MongoDB</h1>

  <p>This is a simple Ecommerce REST API built using <strong>FastAPI</strong> and connected to <strong>MongoDB Atlas</strong>.</p>

  <h2>🌐 Live App Link</h2>
  <p>
    <a href="https://fastapi-xylq.onrender.com" target="_blank">
      https://fastapi-xylq.onrender.com
    </a>
  </p>

  <h2>📁 Available Endpoints</h2>
  <ul>
    <li>
      <strong>Base:</strong> 
      <a href="https://fastapi-xylq.onrender.com/" target="_blank">
        / → Welcome Message
      </a>
    </li>
    <li>
      <strong>Products API:</strong> 
      <a href="https://fastapi-xylq.onrender.com/products" target="_blank">
        /products → Add/List Products
      </a>
    </li>
    <li>
      <strong>Orders API:</strong> 
      <a href="https://fastapi-xylq.onrender.com/orders" target="_blank">
        /orders → Add/List Orders
      </a>
    </li>
  </ul>

  <h2>📦 Tech Stack</h2>
  <ul>
    <li>Python</li>
    <li>FastAPI</li>
    <li>MongoDB Atlas</li>
    <li>Render (for deployment)</li>
  </ul>

  <h2>⚙️ How to Run Locally</h2>
  <ol>
    <li>Clone the repository:<br/>
      <code>git clone https://github.com/Bittu-kumar2003/fastapi.git</code>
    </li>
    <li>Install dependencies:<br/>
      <code>pip install -r requirements.txt</code>
    </li>
    <li>Set your MongoDB connection URI in a file named <code>.env</code> or directly in your code.</li>
    <li>Run the server:<br/>
      <code>uvicorn main:app --reload</code>
    </li>
  </ol>

  <h2>📄 File Structure</h2>
  <pre>
📦fastapi
 ┣ 📂routes
 ┃ ┣ 📜product_routes.py
 ┃ ┗ 📜order_routes.py
 ┣ 📂models
 ┃ ┣ 📜product_model.py
 ┃ ┗ 📜order_model.py
 ┣ 📜main.py
 ┣ 📜database.py
 ┗ 📜render.yaml
  </pre>

  <h2>📌 Deployment on Render</h2>
  <ol>
    <li>Create an account at <a href="https://render.com" target="_blank">render.com</a>.</li>
    <li>Connect your GitHub repo.</li>
    <li>Add <code>render.yaml</code> to define the build and start commands.</li>
    <li>Set environment variable <code>MONGO_URI</code> with your MongoDB Atlas URI.</li>
  </ol>

  <h2>✅ Example API Calls (with Postman)</h2>
  <p><strong>POST /products</strong> - Add a product</p>
  <pre>
{
  "name": "Laptop",
  "price": 75000,
  "description": "High-performance laptop",
  "stock": 10
}
  </pre>

  <p><strong>GET /products</strong> - List products</p>

  <p><strong>POST /orders</strong> - Add an order</p>
  <pre>
{
  "product_id": "your_product_id",
  "quantity": 2,
  "customer_name": "John Doe"
}
  </pre>

  <p><strong>GET /orders</strong> - List orders</p>

  <h2>🙌 Thanks!</h2>
  <p>Feel free to contribute or raise issues.</p>
</body>
</html>
