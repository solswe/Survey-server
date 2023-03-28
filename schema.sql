CREATE TABLE surveyform (
    id serial primary key,
    ts TIMESTAMP not null,
    topGenre VARCHAR(30) not null,
    secGenre VARCHAR(30) not null,
    allTimeTitle VARCHAR(30) not null,
    allTimeGenre VARCHAR(30),
    allTimeRate VARCHAR(10),
    tasteTitle VARCHAR(30) not null,
    tasteGenre VARCHAR(30),
    tasteRate VARCHAR(10),
    recTitle VARCHAR(30) not null,
    recGenre VARCHAR(30),
    recRate VARCHAR(10),
    subscribe VARCHAR(10),
    services VARCHAR(500)
);
