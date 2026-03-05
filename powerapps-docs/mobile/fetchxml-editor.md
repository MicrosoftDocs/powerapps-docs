---
title: FetchXML editor for Power Apps offline profiles
description: Learn how the FetchXML Editor in Power Apps helps you create advanced offline filters, optimize sync performance, and collaborate with ease using XML-based queries.
author: shwetamurkute
ms.author: smurkute
ms.reviewer: smurkute
ms.date: 03/05/2026
ms.topic: feature-guide
---

# FetchXML editor for offline profiles overview (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

By using the **FetchXML editor** in Power Apps, you can define offline data filters with Dataverse's native FetchXML query language. It provides makers advanced control beyond the visual expression builder, enabling more precise offline queries, performance optimizations for syncing large datasets, and easier maintainability of filter definitions as plain-text XML.

## Benefits of the FetchXML editor

The FetchXML editor offers several advantages over the visual expression Builder for defining offline data filters.

### Advanced filtering capabilities

The visual expression builder handles simple filters well but doesn't support complex queries or all Dataverse condition operators. The FetchXML editor removes those limitations, giving you access to the full range of FetchXML capabilities. Operators supported exclusively through FetchXML include:

- Aggregates such as `sum`, `count`, `max`, and `min`
- Hierarchical conditions such as `above`, `eq-or-above`, `under`, and `eq-or-under`

### Improved offline sync performance

FetchXML supports special attributes and query hints that optimize large queries. For example, applying `latematerialize="true"` or `hint="union"` can significantly speed up offline synchronization and help prevent timeouts when working with datasets of 100,000 or more records.

### Better maintainability

Because FetchXML filter definitions are stored as XML text, you can save them in version control, share them with your team, and review changes over time. This capability improves collaboration and provides a clear history of modifications to offline filters.

## How the FetchXML editor works

You access the FetchXML editor through the offline profile configuration experience in Power Apps. You write or paste a FetchXML query, and the editor validates it in real time before you save.

### Open an offline profile

In Power Apps ([make.powerapps.com](https://make.powerapps.com)), go to your environment's settings and open the **Offline Profiles** page. Select an existing offline profile or create a new one, and then select **Edit profile**.

### Choose a table and open its filter

In the offline profile editor, add or select the table whose data you want to filter for offline use. Under **Filter**, choose **Custom** or **Related rows**, and then select **Edit filter**. In the filter editor, scroll down and select **View/Edit FetchXML** to open the FetchXML code editor.

### Write or paste your FetchXML query

The editor displays the current filter as FetchXML. Modify this query or paste a new one. The editor automatically validates syntax and structure as you edit, checking for:

- A required `<fetch>` root element with at least one `<entity>` element
- Only supported FetchXML tags
- Proper parent-child nesting of elements
- A maximum of 500 filter clauses

If the editor detects an issue, such as a missing required element or an unsupported `<link-entity>` usage, it shows a clear error message so you can fix it before saving.

### Apply and save

After your FetchXML query is valid, select **Apply** to convert the filter, and then **Save** the offline profile. If you navigate away without saving, you lose your changes.

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
