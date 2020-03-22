DROP TABLE IF EXISTS chiroptere;

CREATE TABLE chiroptere(
    id_chiroptere INTEGER PRIMARY KEY autoincrement,
    name TEXT NOT NULL,
);

CREATE TABLE place(
    id_place INTEGER PRIMARY KEY autoincrement,
    name TEXT NOT NUL
);

CREATE TABLE data(
    id_place INTEGER NOT NULL,
    id_chiroptere INTEGER NOT NULL,
    nb_call INTEGER NOT NULL,
    nb_file INTEGER NOT NULL
);
/*
INSERT INTO chiroptere(name, nb_file, nb_call) VALUES
("Barbar", 0, 0),
("Eptnil", 0, 0),
("Eptser", 0, 0),
("Hypsav", 0, 0),
("Minsch", 0, 0),
("Myoalc", 0, 0),
("Myobec", 0, 0),
("Myobly", 0, 0),
("Myobra", 0, 0),
("Myocap", 0, 0),
("Myodas", 0, 0),
("Myodau", 0, 0),
("Myoema", 0, 0),
("Myomyo", 0, 0),
("Myonat", 0, 0),
("MyospA", 0, 0),
("Nyclas", 0, 0),
("Nyclei", 0, 0),
("Nycnoc", 0, 0),
("Pipkuh", 0, 0),
("Pipnat", 0, 0),
("PippiM", 0, 0),
("pippiT", 0, 0),
("Pippyg", 0, 0),
("Pleaur", 0, 0),
("Pleaus", 0, 0),
("Plemac", 0, 0),
("Rhieur", 0, 0),
("Rhifer", 0, 0),
("Rhihip", 0, 0),
("Tadten", 0, 0),
("Vesmur", 0, 0),
("ENVsp", 0, 0),
("MyoHF", 0, 0),
("MyoLF", 0, 0),
("Myosp", 0, 0),
("NlaTt", 0, 0),
("Pip35", 0, 0),
("Pip50", 0, 0),
("PipMi", 0, 0),
("Plesp", 0, 0),
("RhiHF", 0, 0),
("Rhisp", 0, 0);
*/  
