# API Documentation

## Overview

This document describes the endpoints and schemas of the API.

## Authentication

The API uses various authentication methods including:

- Basic Authentication
- Token Authentication
- Cookie Authentication

## Endpoints

### Health Check [/api/health-check/]

#### Retrieve Health Check [GET]

Returns successful response.

+ Response 200

    [No response body]

### Recipe Endpoints

#### List Ingredients [/api/recipe/ingredients/]

Manage ingredients in the database.

+ Parameters
    + assigned_only (integer, optional) - Filter by items assigned to recipes.

+ Response 200 (application/json)

    [Array of Ingredient objects]

#### Update Ingredient [/api/recipe/ingredients/{id}/]

Manage ingredients in the database.

+ Parameters
    + id (integer, required) - A unique integer value identifying this ingredient.

+ Request Body (application/json, application/x-www-form-urlencoded, multipart/form-data)
    + Schema: IngredientRequest

+ Response 200 (application/json)

    [Updated Ingredient object]

#### Partially Update Ingredient [/api/recipe/ingredients/{id}/]

Manage ingredients in the database.

+ Parameters
    + id (integer, required) - A unique integer value identifying this ingredient.

+ Request Body (application/json, application/x-www-form-urlencoded, multipart/form-data)
    + Schema: PatchedIngredientRequest

+ Response 200 (application/json)

    [Updated Ingredient object]

#### Delete Ingredient [/api/recipe/ingredients/{id}/]

Manage ingredients in the database.

+ Parameters
    + id (integer, required) - A unique integer value identifying this ingredient.

+ Response 204

    [No response body]

...

### User Endpoints

#### Create User [/api/user/create/]

Create a new user in the system.

+ Request Body (application/json, application/x-www-form-urlencoded, multipart/form-data)
    + Schema: UserRequest

+ Response 201 (application/json)

    [Newly created User object]

...

## Schemas

### Components

#### AuthToken

Serializer for the user auth token.

+ Properties
    + email (string, required)
    + password (string, required)

#### AuthTokenRequest

Serializer for the user auth token.

+ Properties
    + email (string, required)
    + password (string, required)

...

## Security Schemes

- Basic Authentication
- Token Authentication
- Cookie Authentication
