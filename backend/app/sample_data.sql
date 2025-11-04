-- MENU CATEGORIES
INSERT INTO menu_categories (name, sort_order)
VALUES
('Drinks', 1),
('Food', 2),
('Pastries', 3);

-- MENU ITEMS
INSERT INTO menu_items (category_id, name, description, image, is_available, is_seasonal, is_vegan, is_gluten_free, price)
VALUES
(1, 'Latte', 'Espresso with steamed milk', '', 1, 0, 0, 0, 4.50),
(1, 'Cold Brew', 'Slow-steeped 18 hours', '', 1, 0, 0, 1, 4.00),
(1, 'Chai Latte', 'Spiced tea with steamed milk', '', 1, 1, 0, 0, 4.25),
(2, 'Avocado Toast', 'Sourdough topped with avocado and chili flakes', '', 1, 0, 1, 1, 6.75),
(2, 'Breakfast Sandwich', 'Egg, cheese, and bacon on a croissant', '', 1, 0, 0, 0, 5.25),
(3, 'Blueberry Muffin', 'Freshly baked each morning', '', 1, 0, 0, 0, 3.25),
(3, 'Croissant', 'Buttery and flaky classic', '', 1, 0, 0, 0, 3.00);

-- LOCATIONS
INSERT INTO locations (name, address, city, state, postal_code, phone)
VALUES
('Downtown Cafe', '123 Main St', 'Modesto', 'CA', '95350', '(209) 555-1234'),
('Riverwalk Cafe', '42 Oak Ave', 'Turlock', 'CA', '95380', '(209) 555-5678');

-- OPENING HOURS
INSERT INTO opening_hours (location_id, day, opens_at, closes_at)
VALUES
(1, 'Monday', '7:00 AM', '5:00 PM'),
(1, 'Tuesday', '7:00 AM', '5:00 PM'),
(1, 'Wednesday', '7:00 AM', '5:00 PM'),
(1, 'Thursday', '7:00 AM', '5:00 PM'),
(1, 'Friday', '7:00 AM', '6:00 PM'),
(1, 'Saturday', '8:00 AM', '2:00 PM'),
(1, 'Sunday', 'Closed', 'Closed'),
(2, 'Monday', '7:30 AM', '4:30 PM'),
(2, 'Tuesday', '7:30 AM', '4:30 PM'),
(2, 'Wednesday', '7:30 AM', '4:30 PM'),
(2, 'Thursday', '7:30 AM', '4:30 PM'),
(2, 'Friday', '7:30 AM', '4:30 PM'),
(2, 'Saturday', '8:00 AM', '3:00 PM'),
(2, 'Sunday', 'Closed', 'Closed');
