---
title: FetchXML editor for Power Apps offline profiles
description: Learn how the FetchXML Editor in Power Apps helps you create advanced offline filters, optimize sync performance, and collaborate with ease using XML-based queries.
author: Murugesh1985
ms.author: murugeshs
ms.reviewer: smurkute
ms.date: 03/10/2026
ms.topic: feature-guide
---

# FetchXML editor for offline profiles (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

FetchXML is Dataverse's native query language that lets makers write data filters as XML code, similar to writing a formula, but more powerful. It lets makers optimize their complex profiles for better performance and avoid sync timeouts on large tables (100K+ records).

This feature is best suited for advanced makers and developers who are comfortable working with XML and need more control than what the visual filter builder provides.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.

## Benefits of the FetchXML editor

The FetchXML editor offers several advantages over the visual expression builder for defining offline data filters.

- **Advanced filtering capabilities**: FetchXML lets you join unrelated tables. The visual expression builder handles simple filters well but doesn't support complex queries or all Dataverse condition operators. The FetchXML editor removes those limitations, giving you access to the full range of FetchXML capabilities. Operators supported exclusively through FetchXML include aggregates such as `sum`, `count`, `max`, and `min`, and hierarchical conditions such as `above`, `eq-or-above`, `under`, and `eq-or-under`.
- **Improved offline sync performance**: FetchXML supports special attributes and query hints that optimize large queries. For example, applying `latematerialize="true"` or `hint="union"` can significantly speed up offline synchronization and help prevent timeouts when working with datasets of 100,000 or more records. Applying `latematerialize="true"` optimizes query performance by narrowing down matching records before retrieving all their column data. This attribute reduces the load when syncing large tables during offline sync. Applying `hint="union"` improves performance on lookups where a record can relate to multiple entity types by querying each related entity type separately and combining the results, rather than scanning across all of them at once. For example, when syncing tasks that can be linked to either a contact or an account, `hint="union"` queries contacts and accounts independently and merges the results, instead of scanning both tables together.

  Example for `latematerialize`:

  ```xml
  <fetch latematerialize="true" count="500">
    <entity name="contact">
      <filter type="and">
        <condition attribute="statecode" operator="eq" value="0" />
      </filter>
    </entity>
  </fetch>
  ```

  Example for `hint="union"`:

  ```xml
  <fetch latematerialize="true" count="500">
    <entity name="task">
      <filter type="and">
        <condition attribute="statecode" operator="eq" value="0" />
      </filter>
      <link-entity name="contact" from="contactid" to="regardingobjectid" link-type="any" hint="union">
        <filter type="and">
          <condition attribute="statecode" operator="eq" value="0" />
        </filter>
      </link-entity>
      <link-entity name="account" from="accountid" to="regardingobjectid" link-type="any" hint="union">
        <filter type="and">
          <condition attribute="statecode" operator="eq" value="0" />
        </filter>
      </link-entity>
    </entity>
  </fetch>
  ```

- **Better maintainability**: Because FetchXML filter definitions are stored as XML text, it is easier to share and track changes.

## How the FetchXML editor works

You access the FetchXML editor through the offline profile configuration experience in Power Apps. You write or paste a FetchXML query, and the editor validates it in real time before you save.

1. In [Power Apps](https://make.powerapps.com), go to your environment's settings and open the **Offline Profiles** page. Select an existing offline profile or create a new one, and then select **Edit profile**.
1. In the offline profile editor, add or select the table whose data you want to filter for offline use.
1. Under **Filter**, choose **Custom** or **Related rows**, and then select **Edit filter**.
1. In the filter editor, scroll down and select **View/Edit FetchXML** to open the FetchXML code editor.
    :::image type="content" source="media/fetchxml-editor.png" alt-text="Screenshot showing fetchXML code editor.":::
1. Modify the existing FetchXML query or paste a new one. The editor automatically validates syntax and structure as you edit, checking for:

    - A required `<fetch>` root element with at least one `<entity>` element
    - Only supported FetchXML tags
    - Elements placed inside the correct parent elements
    - A maximum of 500 filter clauses

   If the editor detects an issue, such as a missing required element or an unsupported `<link-entity>` usage, it shows a clear error message so you can fix it before saving.

1. After your FetchXML query is valid, select **Apply** to convert the filter, and then **Save** the offline profile.

> [!IMPORTANT]
> Always select **Apply** and then **Save** after editing FetchXML. If you don't save, your changes are discarded.

After saving, the offline profile uses your custom FetchXML filter for data sync. If your query uses only features supported by the visual builder, those filters continue to display in the Expression Builder UI. If you use advanced FetchXML-only features, the visual filter UI might not render them. Use the FetchXML Editor for any future edits to that filter.

## Best practices

- Apply performance hints like `latematerialize="true"` or `hint="union"` for large datasets.
- Validate your FetchXML by using the built-in editor checks before saving.
- Save your offline profile immediately after applying FetchXML changes.
- Use only supported FetchXML constructs for offline profiles, such as `link-type="any"` or `link-type="not any"`.
- Avoid unsupported join types like `inner` or `outer` in offline filters.
- Keep filter clauses under the 500-clause limit per query.
- Don't ignore validation errors. Queries must be well-formed and complete.

## Limitations

- Queries must start with a `<fetch>` root element and include at least one `<entity>` element.
- Only supported FetchXML elements are allowed. Unknown or unsupported tags trigger validation errors.
- Elements must follow proper parent-child nesting rules.
- `<link-entity>` inside `<filter>` must use `link-type="any"` or `link-type="not any"`. Inner and outer joins aren't supported.
- FetchXML `<attribute>` tags aren't used for column selection in offline sync. Use the **Filter Columns** option instead.
- Explicit pagination attributes like `page` and `count` are ignored in offline profiles.
- Queries are limited to a maximum of 500 filter clauses.
