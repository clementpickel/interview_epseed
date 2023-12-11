BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(80) NOT NULL,
	"email"	VARCHAR(120) NOT NULL,
	"password"	VARCHAR(120) NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("email"),
	UNIQUE("username")
);
CREATE TABLE IF NOT EXISTS "note" (
	"id"	INTEGER NOT NULL,
	"title"	VARCHAR(100) NOT NULL,
	"content"	TEXT NOT NULL,
	"created_at"	DATETIME,
	"modified_at"	DATETIME,
	"user_id"	INTEGER NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "user"("id"),
	PRIMARY KEY("id")
);
INSERT INTO "user" VALUES (2,'quentin','q.pickel@outlook.fr','$2b$12$jnNTbBF3GbmwFxGY.PsAUOF9XXTCrc31aDWOZvj7YyfTPDKIdtWcK');
INSERT INTO "user" VALUES (3,'clement','clement.pickel@epitech.eu','$2b$12$0AaFD90OJQuFR3YDPar63uDON.Bq9msdnnsNbbthJoDQbWFeZRKNS');
INSERT INTO "note" VALUES (2,'New za warudo','Za warudo','2023-12-10 23:54:47','2023-12-11 00:05:54',2);
INSERT INTO "note" VALUES (3,'Epseed','Epseed est une entreprise fort sympathique','2023-12-11 00:30:42','2023-12-11 00:30:42',3);
INSERT INTO "note" VALUES (4,'Lalilulelo','The patriots','2023-12-11 00:31:24','2023-12-11 00:31:24',3);
INSERT INTO "note" VALUES (5,'Armstrong','He could break the president in two with his own bare hands','2023-12-11 00:31:56','2023-12-11 00:31:56',3);
COMMIT;
