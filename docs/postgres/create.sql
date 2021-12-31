CREATE TABLE public.dna (
	origin varchar NOT NULL,
	"sequence" varchar NOT NULL,
	CONSTRAINT dna_pk PRIMARY KEY ("sequence")
);