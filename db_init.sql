CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    on_offer BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO items (name, description, price, on_offer) VALUES
    ('Item 1', 'Description of item 1', 100, TRUE),
    ('Item 2', 'Description of item 2', 200, FALSE),
    ('Item 3', 'Description of item 3', 300, TRUE),
    ('Item 4', 'Description of item 4', 400, FALSE);