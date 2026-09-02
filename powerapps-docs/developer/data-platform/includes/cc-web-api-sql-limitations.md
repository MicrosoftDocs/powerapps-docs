Dataverse provides a read-only SQL interface that supports the following T-SQL subset.

| Feature | Supported syntax |
|---|---|
| Select | `SELECT`, `SELECT DISTINCT`, `SELECT TOP N` (0–5000) |
| Joins | `INNER JOIN`, `LEFT JOIN` (multi-table) |
| Filtering | `WHERE` with `=`, `!=`, `>`, `<`, `>=`, `<=`, `LIKE`, `IN`, `NOT IN`, `IS NULL`, `IS NOT NULL`, `BETWEEN`, `AND`, `OR`, nested parentheses |
| Grouping and aggregation | `GROUP BY`, `COUNT(*)`, `SUM()`, `AVG()`, `MIN()`, `MAX()` |
| Sorting and paging | `ORDER BY [ASC\|DESC]`, `OFFSET n ROWS FETCH NEXT m ROWS ONLY` |

> [!NOTE]
> Each command must contain a single `SELECT` statement. Dataverse doesn't support commands with multiple result sets, such as `SELECT name FROM account; SELECT fullname FROM contact`.

> [!IMPORTANT]
> SQL queries must meet these requirements:
>
> - `WHERE` can only be a boolean expression tree where leaves are binary operators (`=`, `>`, `like`, etc.) with one of the arguments being a direct column reference and another being a constant.
> - `TOP` only allows an integer literal.
> - `ORDER BY` can only reference columns and doesn't allow any complex expressions.

The following statements or features aren't supported: `SELECT *`, subqueries, CTEs, `HAVING`, `UNION`, `RIGHT JOIN`, `FULL JOIN`, `CROSS JOIN`, `CASE`, `COALESCE`, window functions, string/date/math functions, and any statement other than `SELECT`, such as `DECLARE`, `INSERT`, `UPDATE`, `DELETE`, or `ALTER TABLE`. 