# AirBnB Clone- RESTful API

## Improve Storage
Add `get` and `count` methods to the storage classes: `get` retrieves a single object given its class and ID, falling back to `None`; `count` takes a class name and returns the number of objects of that class.

## Status of Your API
Set up an API server with a simple endpoint that reports its status.

## Some Stats?
Add an endpoint that shows the number of records in each table.

## Not Found
Have the API server send error messages in JSON rather than HTML format.

## State
Add endpoints that allow listing, adding, modifying, and deleting `State` objects.

## City, Amenity, User, Place, Reviews
Add the same CRUD endpoints for the other data models.

## HTTP Access Control (CORS)
Add `Access-Control-Allow-Origin` headers to allow resource sharing only from the local host.

## Place - Amenity
Add CRUD endpoints for the many-to-many relationship between places and amenities.

## Security Improvements!
Always hash the users' passwords instead of storing them in plain text.

## Search
Allow searching for places based on state, city, and amenities.
