Dataverse Web API supports only read-only queries. It doesn't support complex joins, subqueries, and certain SQL functions. Your SQL query must follow the supported subset:

- `WHERE` can only be a boolean expression tree where leaves are binary operators (`=`, `>`, `like`, and so on) with one of the arguments being a direct column reference and the other argument being a constant.
- `TOP` only allows an integer literal.
- `ORDERBY` can only reference columns and doesn't allow any complex expressions.