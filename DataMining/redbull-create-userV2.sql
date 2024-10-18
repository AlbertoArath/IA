

1. Crear el usuario

create user f1 identified by Oracle_12345;
grant dwrole to f1;
alter user f1 quota unlimited on data;
grant create session to f1;
grant create table to f1;
begin
ords.enable_schema(p_enabled => true,
  p_schema => 'f1',
  p_url_mapping_type => 'BASE_PATH',
  p_url_mapping_pattern => 'f1',
  p_auto_rest_auth => true);
commit;
end;

/

2. Crear las tablas

CREATE TABLE F1.RACES
   (	"RACEID" NUMBER(38,0),
	"YEAR" NUMBER(38,0),
	"ROUND" NUMBER(38,0),
	"NAME" VARCHAR2(255),
	"F1DATE" DATE,
	"TIME" VARCHAR2(255),
	"URL" VARCHAR2(500),
	"SCORE" NUMBER,
	"DNF_COUNT" NUMBER,
	"DNF_DUE_TO_ACCIDENT_COUNT" NUMBER,
	"WEATHER" VARCHAR2(500),
	"WEATHER_WET" VARCHAR2(1),
	"CIRCUITREF" VARCHAR2(100),
	"YEAR_C" VARCHAR2(4),
	"RACE_COUNT" NUMBER,
	"NAME_YEAR" VARCHAR2(100),
	"OVERTAKEN_POSITIONS_TOTAL" NUMBER
   );
   
   
   
