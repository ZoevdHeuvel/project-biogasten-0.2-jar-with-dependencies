/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     12-1-2022 12:29:43                           */
/*==============================================================*/


drop table if exists COMPOUND;

drop table if exists GENE;

drop table if exists INPUT;

drop table if exists KEGGGENE;

drop table if exists KEGGGENE_ID;

drop table if exists MEASUREMENT;

drop table if exists OUTPUT;

drop table if exists PATHWAY;

drop table if exists PROCESBLOK;

drop table if exists PROCESBLOKPATHWAY;

/*==============================================================*/
/* Table: COMPOUND                                              */
/*==============================================================*/
create table COMPOUND
(
   COMPOUND                 varchar(255) not null,
   primary key (COMPOUND)
);

/*==============================================================*/
/* Table: GENE                                                  */
/*==============================================================*/
create table GENE
(
   CODE                 varchar(255) not null,
   primary key (CODE)
);

/*==============================================================*/
/* Table: INPUT                                                 */
/*==============================================================*/
create table INPUT
(
   PROCES_CODE           varchar(255) not null,
   COMPOUND                 varchar(255) not null,
   primary key (PROCES_CODE, COMPOUND),
   foreign key (PROCES_CODE) references PROCESBLOK (PROCES_CODE),
   foreign key (COMPOUND) references COMPOUND (COMPOUND)
);

/*==============================================================*/
/* Table: KEGGGENE                                              */
/*==============================================================*/
create table KEGGGENE
(
   KEGG_ID              varchar(255) not null,
   CODE                 varchar(255) not null,
   primary key (KEGG_ID, CODE),
   foreign key (CODE) references KEGGGENE (CODE)
);

/*==============================================================*/
/* Table: KEGGGENE_ID                                           */
/*==============================================================*/
create table KEGGGENE_ID
(
   KEGG_ID              varchar(255) not null,
   primary key (KEGG_ID)
);

/*==============================================================*/
/* Table: MEASUREMENT                                           */
/*==============================================================*/
create table MEASUREMENT
(
   PROCES_CODE           varchar(255) not null,
   CODE                 varchar(255) not null,
   MEASUREMENT          varchar(255),
   DATE                 int not null,
   primary key (PROCES_CODE, CODE, DATE),
   foreign key (PROCES_CODE) references PROCESBLOK (PROCES_CODE),
   foreign key (CODE) references GENE (CODE)
);

/*==============================================================*/
/* Table: OUTPUT                                                */
/*==============================================================*/
create table OUTPUT
(
   PROCES_CODE           varchar(255) not null,
   COMPOUND                 varchar(255) not null,
   primary key (PROCES_CODE, COMPOUND),
   foreign key (PROCES_CODE) references PROCESBLOK (PROCES_CODE),
   foreign key (COMPOUND) references COMPOUND (COMPOUND)
);

/*==============================================================*/
/* Table: PATHWAY                                               */
/*==============================================================*/
create table PATHWAY
(
   CODE                 varchar(255) not null,
   NAME                 varchar(255),
   primary key (CODE)
);

/*==============================================================*/
/* Table: PROCESBLOK                                            */
/*==============================================================*/
create table PROCESBLOK
(
   PROCES_CODE           varchar(255) not null,
   NAME                 varchar(255),
   CLASS                varchar(255),
   primary key (PROCES_CODE)
);

/*==============================================================*/
/* Table: PROCESBLOKPATHWAY                                     */
/*==============================================================*/
create table PROCESBLOKPATHWAY
(
   PROCES_CODE           varchar(255) not null,
   CODE                 varchar(255) not null,
   primary key (PROCES_CODE, CODE),
   foreign key (PROCES_CODE) references PROCESBLOK (PROCES_CODE),
   foreign key (CODE) references PATHWAY (CODE)
);