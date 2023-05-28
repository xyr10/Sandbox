CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Take out the trash",
    "Sort trash and take it out to the bins on the street"
);

INSERT INTO task (
    summary, 
    description
) VALUES (
    "Buy groceries",
    "One poind of beef, potatoes, groceries"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash the car",
    "Use the hose in front and the car wash stuff"
);
