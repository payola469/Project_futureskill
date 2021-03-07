# Inventory System API Specifications

### HTML Pages

---

> Home page

- Method: `GET`
- Path: `/`
- Response: home page html

---

### API

---

> Add new card

- Method: `POST`

- Path: `/card/new`

- Request:

  - Header
    - Content-Type: `multipart/form-data`
  - Body

  ```json
  {
    "cardName": "string"
  }
  ```

- Response:

  - Home page

---

> Add item to card

- Method: `POST`

- Path: `/item/new`

- Request:

  - Header
    - Content-Type: `multipart/form-data`
  - Body

  ```json
  {
    "card_id": "string",
    "name": "string"
  }
  ```

- Response:


---

> Check / Uncheck item in card

- Method: `POST`

- Path: `/item/check`

- Request

  - Header:
    - Content-Type: `multipart/form-data`
  - Body

  ```json
  {
    "item_id": "string",
    "status": "boolean"
  }
  ```

- Response:
