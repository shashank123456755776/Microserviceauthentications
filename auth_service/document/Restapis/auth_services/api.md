

Here’s an example of an API documentation (`api.md`) for your provided endpoints:

---

# API Documentation

## Base URL

`http://<your-server-url>/`

---

## Endpoints

### 1. **Register User**

- **URL:** `/register/`
- **Method:** `POST`
- **Description:** This endpoint registers a new user.
- **Request Body:**

```json
{
  "username": "string",
  "password": "string",
  "role": "string",  // Example: 'admin', 'user'
}
```

- **Response:**

    - **Status Code:** `201 Created`
    - **Body:**

    ```json
    {
      "message": "User registered successfully",
      "uuid": "user-uuid",
      "api_key": "user-api-key"
    }
    ```

    - **Status Code:** `400 Bad Request`
    - **Body:**

    ```json
    {
      "username": ["This field is required."],
      "password": ["This field is required."]
    }
    ```

### 2. **Login User**

- **URL:** `/login/`
- **Method:** `POST`
- **Description:** This endpoint logs in a user using their credentials (username and password).
- **Request Body:**

```json
{
  "username": "string",
  "password": "string"
}
```

- **Response:**

    - **Status Code:** `200 OK`
    - **Body:**

    ```json
    {
      "uuid": "user-uuid",
      "refresh": "refresh-token",
      "access": "access-token",
      "role": "user-role",
      "api_key": "user-api-key",
      "status": 200
    }
    ```

    - **Status Code:** `401 Unauthorized`
    - **Body:**

    ```json
    {
      "error": "Invalid credentials"
    }
    ```

    - **Status Code:** `400 Bad Request`
    - **Body:**

    ```json
    {
      "username": ["This field is required."],
      "password": ["This field is required."]
    }
    ```

### 3. **Login via API Key**

- **URL:** `/login/api-key/`
- **Method:** `GET`
- **Description:** This endpoint logs in a user via an API key.
- **Headers:**

    - `X-API-KEY`: The API key for authentication.

- **Response:**

    - **Status Code:** `200 OK`
    - **Body:**

    ```json
    {
      "refresh": "refresh-token",
      "access": "access-token",
      "username": "user-username",
      "role": "user-role",
      "uuid": "user-uuid",
      "api_key": "user-api-key"
    }
    ```

    - **Status Code:** `400 Bad Request`
    - **Body:**

    ```json
    {
      "error": "X-API-KEY header missing"
    }
    ```

    - **Status Code:** `401 Unauthorized`
    - **Body:**

    ```json
    {
      "error": "Invalid API key"
    }
    ```

---

## Error Codes

- **400 Bad Request:** The request was invalid or missing necessary data.
- **401 Unauthorized:** Invalid login credentials or API key.
- **404 Not Found:** The endpoint does not exist.
- **500 Internal Server Error:** There was an issue with the server processing the request.

---

## Notes

- For the `RegisterView`, the user must provide the username, password, and role for registration.
- The `LoginView` allows users to authenticate via their username and password.
- The `ApiKeyLoginView` enables login using an API key provided in the `X-API-KEY` header.

---

This should provide a clear documentation for your API. You can further modify it based on the specifics of your system or environment.