
INSERT INTO "items" ("id", "item_number", "description") VALUES
(1,	'3939',	'Analyzer Subassembly'),
(2,	'5772',	'Texas Red Excitation Module'),
(3,	'5782',	'Green Excitation Module'),
(4,	'3778',	'Vacuum System Module'),
(5,	'5492',	'Camera Module');

INSERT INTO "modules" ("id", "serial_number", "work_order_id") VALUES
(1,	'TXIRABC1234',	1),
(2,	'TXIRDEF5678',	1),
(3,	'TXIRGHI9012',	1),
(4,	'TXIRGHI9011',	1),
(5,	'TXIRGHI9014',	1),
(6,	'TXIRJKL3123',	2),
(7,	'TXIRMNO7456',	2),
(8,	'TXIRPQR1789',	2),
(9,	'TXIRJKL3485',	2),
(10,	'TXIRMNO7687',	2),
(11,	'TXIRPQR1128',	2),
(12,	'TXIRPQR1778',	2),
(13,	'TXIRSTU5644',	3),
(14,	'TXIRVWX9658',	3),
(15,	'TXIRYZA3789',	3),
(16,	'TXIRBCD7558',	3),
(17,	'TXIRSTU5348',	3),
(18,	'TXIRVWX9912',	3),
(19,	'TXIRYZA3885',	3),
(20,	'TXIRBCD7772',	3),
(21,	'TXIRSTU5981',	3),
(22,	'TXIRVWX9697',	3);

INSERT INTO "process_routings" ("id", "item_id", "description") VALUES
(2,	2,	'Texas Red Excitation Subassembly'),
(3,	3,	'Green Excitation Subassembly'),
(4,	5,	'Camera Subassembly'),
(5,	4,	'Vacuum System Subassembly'),
(1,	1,	'Complete Analyzer');

INSERT INTO "work_orders" ("id", "quantity") VALUES
(1,	5),
(2,	7),
(3,	10);
