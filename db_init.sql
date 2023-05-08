CREATE TABLE work_orders (
    id SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL
);

CREATE TABLE modules (
    id SERIAL PRIMARY KEY,
    serial_number VARCHAR(255) NOT NULL,
    work_order_id INTEGER,
    FOREIGN KEY (work_order_id) REFERENCES work_orders (id)
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_number VARCHAR(255) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE process_routings (
    id SERIAL PRIMARY KEY,
    item_id INTEGER,
    description VARCHAR(255),
    FOREIGN KEY (item_id) REFERENCES items (id)
);
