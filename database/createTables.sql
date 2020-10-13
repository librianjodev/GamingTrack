CREATE SEQUENCE IF NOT EXISTS public."id_user"
    INCREMENT 1;

CREATE TABLE IF NOT EXISTS public."User"
(
    id integer NOT NULL DEFAULT nextval('id_user'),
    nome text,
    photo bytea,
    email text NOT NULL,
    password text NOT NULL,
    login text NOT NULL,
    "creationDate" timestamp with time zone,
    "lastLogin" timestamp with time zone,
    "permissionLevel" integer,
    PRIMARY KEY (id)
);

CREATE OR REPLACE FUNCTION "inserirDataCadastro"()
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
    AS $$

BEGIN

    UPDATE public."user"
	SET "creationDate"=LOCALTIMESTAMP
	WHERE new.id="user".id;

    RETURN NEW;

END;
$$;
--/*
CREATE TRIGGER adicionarDataCadastroUser
AFTER INSERT 
ON "user"
FOR EACH ROW
EXECUTE PROCEDURE "inserirDataCadastro"();--*/