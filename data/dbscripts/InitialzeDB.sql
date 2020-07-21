2	B	22
1	WFH	474
1	SPY	272
1	AAPL	90.4377
1	HACK	233
2	HACK	22
2	TSLA	22
2	GOOGL	22
2	QQQ	22
2	F	22

CREATE SCHEMA Users;

CREATE TABLE Users.user (
    user_id int,
    pw_hash varchar(255),
    email varchar(255),
    join_ts TIMESTAMP,
    created_ts TIMESTAMP,
    modified_ts TIMESTAMP
);

CREATE TABLE Users.net_worth (
    user_id int,
    net_worth numeric,
    net_worth_ts TIMESTAMP,
    created_ts TIMESTAMP,
    modified_ts TIMESTAMP
);

CREATE TABLE Users.portfolio (
    user_id int,
    portfolio_id int,
    symbol varchar(6),
    quantity numeric,
    created_ts TIMESTAMP,
    modified_ts TIMESTAMP
);

CREATE SCHEMA Stocks;


CREATE TABLE Stocks.price (
    symbol varchar(5),
    price numeric,
    price_ts TIMESTAMP,
    after_hours boolean,
    source varchar(255),
    created_ts TIMESTAMP,
    modified_ts TIMESTAMP
);
