# Vendor Management System API Documentation

Welcome to the Vendor Management System API documentation. This document provides instructions on setting up and using the API endpoints for managing vendors, purchase orders, and performance metrics.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/SanyujaShelke/Vendor-Management-System.git
    cd vendor_management_system
    ```

2. Activate the virtual environment:

    ```bash
    source myenv/bin/activate  # For Unix/Mac
    .\myenv\Scripts\activate     # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for accessing the Django admin):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ``` 

## API Endpoints

### Vendor Management

- **List/Create Vendors**

  - Endpoint: `POST /api/vendors/`
  - Description: Create a new vendor.
  - Request Body:
    ```json
    {
      "name": "Vendor Name",
      "contact_details": "Contact Information",
      "address": "Vendor Address",
      "vendor_code": "Unique Vendor Code"
    }
    ```
  - Example Response:
    ```json
    {
      "id": 1,
      "name": "Vendor Name",
      "contact_details": "Contact Information",
      "address": "Vendor Address",
      "vendor_code": "Unique Vendor Code",
      "on_time_delivery_rate": 0.0,
      "quality_rating_avg": 0.0,
      "average_response_time": 0.0,
      "fulfillment_rate": 0.0
    }
    ```

- **Retrieve/Update/Delete Vendor**

  - Endpoint: `GET /api/vendors/{vendor_id}/`
  - Description: Retrieve details of a specific vendor.
  - Endpoint: `PUT /api/vendors/{vendor_id}/`
  - Description: Update details of a specific vendor.
  - Endpoint: `DELETE /api/vendors/{vendor_id}/`
  - Description: Delete a specific vendor.

### Purchase Order Tracking

- **List/Create Purchase Orders**

  - Endpoint: `POST /api/purchase_orders/`
  - Description: Create a new purchase order.
  - Request Body:
    ```json
    {
      "vendor": "Vendor ID",
      "po_number": "PO Number",
      "order_date": "Order Date",
      "delivery_date": "Delivery Date",
      "items": "Items Details",
      "quantity": "Total Quantity",
      "status": "Status"
    }
    ```
  - Example Response:
    ```json
    {
      "id": 1,
      "vendor": 1,
      "po_number": "PO Number",
      "order_date": "Order Date",
      "delivery_date": "Delivery Date",
      "items": "Items Details",
      "quantity": "Total Quantity",
      "status": "Status",
      "quality_rating": null,
      "issue_date": "Issue Date",
      "acknowledgment_date": null
    }
    ```

- **Retrieve/Update/Delete Purchase Order**

  - Endpoint: `GET /api/purchase_orders/{po_id}/`
  - Description: Retrieve details of a specific purchase order.
  - Endpoint: `PUT /api/purchase_orders/{po_id}/`
  - Description: Update details of a specific purchase order.
  - Endpoint: `DELETE /api/purchase_orders/{po_id}/`
  - Description: Delete a specific purchase order.

### Vendor Performance Evaluation

- **Retrieve Vendor Performance Metrics**

  - Endpoint: `GET /api/vendors/{vendor_id}/performance/`
  - Description: Retrieve performance metrics for a specific vendor.

## Authentication

API endpoints are secured with token-based authentication. To access authenticated endpoints, include the token in the request header:

