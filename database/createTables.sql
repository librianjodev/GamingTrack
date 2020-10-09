CREATE SEQUENCE public."id_user"
    INCREMENT 1;

CREATE TABLE IF NOT EXISTS public."user"
(
    id integer NOT NULL DEFAULT nextval('id_user'),
    nome text,
    photo bytea,
    email text NOT NULL,
    password text NOT NULL,
    login text NOT NULL,
    "creationDate" timestamp with time zone DEFAULT (LOCALTIMESTAMP),
    "lastLogin" timestamp with time zone,
    "permissionLevel" integer,
    PRIMARY KEY (id)
);