Alternate key values with the following characters `/`,`<`,`>`,`*`,`%`,`&`,`:`,`\\`,`?`,`+` aren't supported. These special characters are reserved or structurally significant in a URL path segment.  Dataverse will return an error if you send a `GET` request with these values within the parentheses of the URL. The workaround is not to retrieve a single record, but to use the alternate key values with `$filter` to retrieve a collection that contains the one record that matches the alternate key values.

For example, instead of this request that fails:

```http
GET [Organization URI]/api/data/v9.2/new_skts(new_name='M%26M')
```

Use a `$filter` query:

```http
GET [Organization URI]/api/data/v9.2/new_skts?$filter=new_name eq 'M%26M'&$select=new_name
```

If you only need to access the record, you can take the data from the first (and only) matching record in the `value` collection returned. If you need to perform some other action, like updating or deleting the record, you can use this approach to get the ID of the matching record and then refer to the record conventionally using the ID value rather than the value of alternate keys.

> [!NOTE]
> Parameter aliases (`@param`) don't work with alternate key syntax. Using a parameter alias in a key predicate returns a `400` error even for values without special characters. Use `$filter` instead.