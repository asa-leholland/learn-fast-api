
INSERT INTO items (item_number, description) VALUES
('1234', 'Manufacturing part 1'),
('5432', 'Manufacturing part 2'),
('5864', 'Manufacturing part 3'),
('8468', 'Manufacturing part 4'),
('87946', 'Manufacturing part 5'),
('7843', 'Manufacturing part 6'),
('1253', 'Manufacturing part 7'),
('0006', 'Manufacturing part 8'),
('4785', 'Manufacturing part 9'),
('4555', 'Manufacturing part 10');

INSERT INTO work_orders (quantity) VALUES
(5),
(7),
(10);

INSERT INTO modules (serial_number, work_order_id) VALUES
('TXIRABC1234', 1),
('TXIRDEF5678', 1),
('TXIRGHI9012', 1),
('TXIRGHI9011', 1),
('TXIRGHI9014', 1),

('TXIRJKL3123', 2),
('TXIRMNO7456', 2),
('TXIRPQR1789', 2),
('TXIRJKL3485', 2),
('TXIRMNO7687', 2),
('TXIRPQR1128', 2),
('TXIRPQR1778', 2),

('TXIRSTU5644', 3),
('TXIRVWX9658', 3),
('TXIRYZA3789', 3),
('TXIRBCD7558', 3),
('TXIRSTU5348', 3),
('TXIRVWX9912', 3),
('TXIRYZA3885', 3),
('TXIRBCD7772', 3),
('TXIRSTU5981', 3),
('TXIRVWX9697', 3);


INSERT INTO process_routings (description) VALUES
 ( 'Analyzer'),
 ('Excitation Module'),
 ('Texas Red'),
  ( 'Green'),
  ('Vacuum System');
