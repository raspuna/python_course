USE `world`;

-- #1
SELECT name, language, percentage  FROM countries JOIN languages ON countries.id = country_id 
	WHERE language = 'Slovene' ORDER BY percentage DESC;

-- #2
SELECT countries.name, count(cities.id) FROM countries JOIN cities ON countries.id = country_id 
	GROUP BY countries.name ORDER BY count(cities.id) DESC;
    
-- #3
SELECT cities.name, cities.population FROM cities JOIN countries ON countries.id = country_id 
	WHERE countries.name = 'Mexico' AND cities.population > 500000 ORDER BY population DESC;

-- #4
SELECT countries.name, language, languages.percentage FROM languages JOIN countries ON countries.id = country_id
	WHERE languages.percentage > 89 ORDER BY languages.percentage DESC;

-- #5
SELECT countries.name, countries.surface_area FROM countries 
	WHERE surface_area < 501 AND population > 100000;
    
-- #6
SELECT name, government_form, capital, life_expectancy FROM countries
	WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy  > 75;

-- #7
SELECT countries.name, cities.name, cities.district, cities.population FROM cities JOIN countries ON countries.id = country_id
	WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

-- #8
SELECT region, count(countries.id) FROM countries GROUP BY region ORDER BY count(countries.id) DESC;
    
    