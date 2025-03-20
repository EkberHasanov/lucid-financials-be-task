Example curl Commands
1. Signup a new user
```bash
curl -X 'POST' \
  'http://localhost:8000/api/signup' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "wassup@user.com",
  "password": "Password!123"
}'
```

2. Login
```bash
curl -X 'POST' \
  'http://localhost:8000/api/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "wassup@user.com",
  "password": "Password!123"
}'
```
Save the returned token for subsequent requests.

3. Create a Post
```bash
curl -X 'POST' \
  'http://localhost:8000/api/posts' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer PASTE_ACTUAL_TOKEN_INSTEAD' \
  -d '{
  "text": "This is my first post!"
}'
```
4. Get All Posts
```bash
curl -X 'GET' \
  'http://localhost:8000/api/posts' \
  -H 'Authorization: Bearer PASTE_ACTUAL_TOKEN_INSTEAD'
```
5. Delete a Post
```bash
curl -X 'DELETE' \
  'http://localhost:8000/api/posts/1' \
  -H 'Authorization: Bearer PASTE_ACTUAL_TOKEN_INSTEAD'
```