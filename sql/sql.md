# Questions
- Q1 Average Salary: CTE, Aggregates in Window functions, CASE WHEN, Date functions such as DATE_PART, INNER JOIN
- Q2 Find Quiet students in results— Subqueries, MIN, MAX, Window functions, Window Alias, INNER JOIN, ALL keyword
- Q3 Human Traffic of Stadium — LEFT JOIN with Subqueries, CTE, ROW_NUMBER
- Q4 Number of Transactions per Visit —RECURSIVE CTE, COALESCE, COUNT
- Q5 Report contiguous dates (MySQL)— Date_sub, ROW_NUMBER
- Q6 Sales by Day of the week — Pivot table, CASE WHEN
- Q7 Department Top 3 Salaries— DENSE_RANK
- Q8 Restaurant Growth — PRECEDING for moving average, OFFSET
- Q9 Shortest distance in a Plane — CROSS JOIN, SQRT, POW
- Q10 Consecutive Numbers —LAG, LEAD

## CTE - Common Table Expressions
CTE is a temporary named result set you can reference within SELECT, INSERT, UPDATE, or DELETE and can be used in a View

```sql
WITH
expression_name_1 AS
(CTE query definition 1)

[, expression_name_X AS
   (CTE query definition X)
 , etc ]

SELECT expression_A, expression_B, ...
FROM expression_name_1
```

*EXAMPLE*
"What is the average monthly cost per campaign for the company’s marketing efforts?"

```sql
-- define CTE:
WITH Cost_by_Month AS
(SELECT campaign_id AS campaign,
       TO_CHAR(created_date, 'YYYY-MM') AS month,
       SUM(cost) AS monthly_cost
FROM marketing
WHERE created_date BETWEEN NOW() - INTERVAL '3 MONTH' AND NOW()
GROUP BY 1, 2
ORDER BY 1, 2)

-- use CTE in subsequent query:
SELECT campaign, avg(monthly_cost) as "Avg Monthly Cost"
FROM Cost_by_Month
GROUP BY campaign
ORDER BY campaign
```

## SQL Aggregate Functions
- AVG()
- SUM()
- MAX(), MIN()
- COUNT()

```sql
SELECT date, city, AVG(amount) AS avg_transaction_amount_for_city
FROM transactions
GROUP BY date, city;
```