# API Documentation

## Introduction
This document provides the API documentation for the API endpoints.

## Authentication
This API uses various authentication methods, including basic authentication, cookie-based authentication, and token-based authentication.

### Basic Authentication
For endpoints requiring basic authentication, use HTTP basic authentication with the username and password provided.

### Cookie-based Authentication
For endpoints requiring cookie-based authentication, include the session token in the cookie named "Session".

### Token-based Authentication
For endpoints requiring token-based authentication, include the authentication token in the Authorization header with the prefix "Token".

## Endpoints

### Retrieve Schema
- **Description**: Retrieves the OpenAPI 3 schema for this API in the selected format.
- **Method**: GET
- **URL**: `/api/schema/`
- **Parameters**:
  - `format` (query parameter, required): Format of the schema. Allowed values: json, yaml.
  - `lang` (query parameter, optional): Language code for the schema.
- **Tags**: schema
- **Security**:
  - cookieAuth
  - basicAuth

### Create User
- **Description**: Creates a new user in the system.
- **Method**: POST
- **URL**: `/api/user/create/`
- **Tags**: user
- **Request Body**:
  - Content-Type: application/json, application/x-www-form-urlencoded, multipart/form-data
  - Schema: User
- **Security**:
  - cookieAuth
  - basicAuth

### Retrieve Authenticated User
- **Description**: Retrieves the authenticated user's information.
- **Method**: GET
- **URL**: `/api/user/me/`
- **Tags**: user
- **Security**: tokenAuth

### Update Authenticated User
- **Description**: Updates the authenticated user's information.
- **Method**: PUT
- **URL**: `/api/user/me/`
- **Tags**: user
- **Request Body**:
  - Content-Type: application/json, application/x-www-form-urlencoded, multipart/form-data
  - Schema: User
- **Security**: tokenAuth

### Partially Update Authenticated User
- **Description**: Partially updates the authenticated user's information.
- **Method**: PATCH
- **URL**: `/api/user/me/`
- **Tags**: user
- **Request Body**:
  - Content-Type: application/json, application/x-www-form-urlencoded, multipart/form-data
  - Schema: PatchedUser
- **Security**: tokenAuth

### Create User Auth Token
- **Description**: Creates a new authentication token for the user.
- **Method**: POST
- **URL**: `/api/user/token/`
- **Tags**: user
- **Request Body**:
  - Content-Type: application/json, application/x-www-form-urlencoded, multipart/form-data
  - Schema: AuthToken
- **Security**:
  - cookieAuth
  - basicAuth

## Schemas
- **AuthToken**:
  - Type: object
  - Description: Serializer for the user auth token.
  - Properties:
    - email (string, format: email, required)
    - password (string, required)
- **PatchedUser**:
  - Type: object
  - Description: Serializer for the user object.
  - Properties:
    - email (string, format: email, maxLength: 255)
    - password (string, writeOnly: true, maxLength: 128, minLength: 5)
    - name (string, maxLength: 255)
- **User**:
  - Type: object
  - Description: Serializer for the user object.
  - Properties:
    - email (string, format: email, maxLength: 255, required)
    - password (string, writeOnly: true, maxLength: 128, minLength: 5, required)
    - name (string, maxLength: 255, required)
