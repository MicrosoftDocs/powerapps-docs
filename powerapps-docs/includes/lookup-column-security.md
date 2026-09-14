> [!IMPORTANT]
> When a lookup column has a value set, Dataverse returns the following information in the table that contains the lookup:
>
> - The ID of the related record.
> - The string value in the related record's [primary name column](../developer/data-platform/entity-metadata.md#primary-name).
>
> Anyone who can access the record that contains the lookup column can view the primary name value, even if they don't have permission to view the related record. Don't store sensitive information in a primary name column.
