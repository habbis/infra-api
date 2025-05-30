DROP TABLE IF EXISTS host2hostgroup;
CREATE TABLE host2hostgroup  (
        id SERIAL  NOT NULL PRIMARY KEY ,
        id_hosts INT,
        id_hostgroup INT
) ;

DROP TABLE IF EXISTS hostgroup;
CREATE TABLE hostgroup  (
        id SERIAL NOT NULL PRIMARY KEY ,
        name VARCHAR(255) ,
        updated TIMESTAMP WITH TIME ZONE DEFAULT now(),
        UNIQUE (name)
) ;


DROP TABLE IF EXISTS host_vars;
CREATE TABLE host_vars  (
        id SERIAL NOT NULL PRIMARY KEY,
        id_hosts INT,
        keyname VARCHAR(255) NOT NULL ,
        value TEXT NOT NULL,
        updated TIMESTAMP WITH TIME ZONE DEFAULT now()
) ;

DROP TABLE IF EXISTS hosts;
CREATE TABLE hosts  (
        id SERIAL NOT NULL PRIMARY KEY,
        FQDN VARCHAR(255) NOT NULL ,
        env VARCHAR(255) NOT NULL ,
        updated TIMESTAMP WITH TIME ZONE DEFAULT now(),
        UNIQUE (FQDN)
) ;

DROP TABLE IF EXISTS reserved_ip;
CREATE TABLE reserved_ip   (
        id SERIAL NOT NULL PRIMARY KEY ,
        name VARCHAR(255) NOT NULL,
        id_hosts INT NOT NULL ,
        ip inet NOT NULL ,
        updated TIMESTAMP WITH TIME ZONE DEFAULT now(),
        UNIQUE (ip)
) ;

DROP TABLE IF EXISTS interfaces;
CREATE TABLE interfaces  (
        id SERIAL NOT NULL PRIMARY KEY ,
        name VARCHAR(255) NOT NULL ,
        ip INET NOT NULL ,
        id_hosts INT NOT NULL ,
        id_vlan INT NOT NULL ,
        id_reserved_ip INT NOT NULL ,
        updated TIMESTAMP WITH TIME ZONE DEFAULT now(),
        UNIQUE (ip)
) ;

DROP TABLE IF EXISTS vlan;
CREATE TABLE vlan  (
        id SERIAL NOT NULL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        vlan_id INT NOT NULL,
        prefix CIDR NOT NULL,
        updated TIMESTAMP WITH TIME ZONE DEFAULT now(),
        UNIQUE (name,prefix)
) ;
