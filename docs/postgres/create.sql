-- public.dna definition

-- Drop table

-- DROP TABLE public.dna;

CREATE TABLE public.dna (
	origin varchar NOT NULL,
	"sequence" varchar NOT NULL,
	id serial4 NOT NULL,
	CONSTRAINT dna_pk PRIMARY KEY (id),
	CONSTRAINT dna_un UNIQUE (sequence)
);