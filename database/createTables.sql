
CREATE OR REPLACE FUNCTION "inserirDataCadastro"()
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
    AS $$

BEGIN

    UPDATE public."GamimgTrack_user"
	SET "creationDate"=LOCALTIMESTAMP
	WHERE new.id="GamimgTrack_user".id;

    RETURN NEW;

END;
$$;
--/*
CREATE TRIGGER adicionarDataCadastroUser
AFTER INSERT 
ON "GamimgTrack_user"
FOR EACH ROW
EXECUTE PROCEDURE "inserirDataCadastro"();--*/