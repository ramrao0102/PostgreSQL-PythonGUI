--
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3
-- Dumped by pg_dump version 14.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE kineteco;
--
-- Name: kineteco; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE kineteco WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';


ALTER DATABASE kineteco OWNER TO postgres;

\connect kineteco

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: human_resources; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA human_resources;


ALTER SCHEMA human_resources OWNER TO postgres;

--
-- Name: manufacturing; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA manufacturing;


ALTER SCHEMA manufacturing OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: departments; Type: TABLE; Schema: human_resources; Owner: postgres
--

CREATE TABLE human_resources.departments (
    department_id integer NOT NULL,
    department_name character varying(100) NOT NULL,
    building character varying(100) NOT NULL
);


ALTER TABLE human_resources.departments OWNER TO postgres;

--
-- Name: employees; Type: TABLE; Schema: human_resources; Owner: postgres
--

CREATE TABLE human_resources.employees (
    employee_id integer NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    hire_date date,
    department_id integer
);


ALTER TABLE human_resources.employees OWNER TO postgres;

--
-- Name: categories; Type: TABLE; Schema: manufacturing; Owner: postgres
--

CREATE TABLE manufacturing.categories (
    category_id integer NOT NULL,
    name character varying(50) NOT NULL,
    market character varying(20) NOT NULL,
    CONSTRAINT categories_market_check CHECK ((((market)::text = 'domestic'::text) OR ((market)::text = 'industrial'::text)))
);


ALTER TABLE manufacturing.categories OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: manufacturing; Owner: postgres
--

CREATE TABLE manufacturing.products (
    product_id character varying(10) NOT NULL,
    product_name character varying(100) NOT NULL,
    power integer,
    manufacturing_cost money NOT NULL,
    category_id integer DEFAULT 4 NOT NULL
);


ALTER TABLE manufacturing.products OWNER TO postgres;

--
-- Name: product_details; Type: VIEW; Schema: manufacturing; Owner: postgres
--

CREATE VIEW manufacturing.product_details AS
 SELECT products.product_id,
    products.product_name AS products_name,
    products.manufacturing_cost,
    categories.name AS categories_name,
    categories.market
   FROM (manufacturing.products
     JOIN manufacturing.categories ON ((products.category_id = categories.category_id)));


ALTER TABLE manufacturing.product_details OWNER TO postgres;

--
-- Data for Name: departments; Type: TABLE DATA; Schema: human_resources; Owner: postgres
--

\i $$PATH$$/3340.dat

--
-- Data for Name: employees; Type: TABLE DATA; Schema: human_resources; Owner: postgres
--

\i $$PATH$$/3339.dat

--
-- Data for Name: categories; Type: TABLE DATA; Schema: manufacturing; Owner: postgres
--

\i $$PATH$$/3338.dat

--
-- Data for Name: products; Type: TABLE DATA; Schema: manufacturing; Owner: postgres
--

\i $$PATH$$/3337.dat

--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: human_resources; Owner: postgres
--

ALTER TABLE ONLY human_resources.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);


--
-- Name: departments human_resources.departments_pkey; Type: CONSTRAINT; Schema: human_resources; Owner: postgres
--

ALTER TABLE ONLY human_resources.departments
    ADD CONSTRAINT "human_resources.departments_pkey" PRIMARY KEY (department_id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: manufacturing; Owner: postgres
--

ALTER TABLE ONLY manufacturing.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: manufacturing; Owner: postgres
--

ALTER TABLE ONLY manufacturing.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- Name: fki_employees_department_id_fkey; Type: INDEX; Schema: human_resources; Owner: postgres
--

CREATE INDEX fki_employees_department_id_fkey ON human_resources.employees USING btree (department_id);


--
-- Name: products_product_id_idx; Type: INDEX; Schema: manufacturing; Owner: postgres
--

CREATE INDEX products_product_id_idx ON manufacturing.products USING btree (product_id);


--
-- Name: employees employees_department_id_fkey; Type: FK CONSTRAINT; Schema: human_resources; Owner: postgres
--

ALTER TABLE ONLY human_resources.employees
    ADD CONSTRAINT employees_department_id_fkey FOREIGN KEY (department_id) REFERENCES human_resources.departments(department_id) NOT VALID;


--
-- Name: products products_category_id_fkey; Type: FK CONSTRAINT; Schema: manufacturing; Owner: postgres
--

ALTER TABLE ONLY manufacturing.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES manufacturing.categories(category_id) ON UPDATE CASCADE;


--
-- Name: SCHEMA human_resources; Type: ACL; Schema: -; Owner: postgres
--

GRANT USAGE ON SCHEMA human_resources TO hr_manager;


--
-- PostgreSQL database dump complete
--

