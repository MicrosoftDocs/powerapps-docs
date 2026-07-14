---
title: "Perform operations using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Microsoft Dataverse Web API provides a RESTful web service interface that you can use to interact with data in Dataverse using a wide variety of programming languages. Read about the operations that can be performed using the Web API"
ms.date: 03/09/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Perform operations by using the Web API

The Web API provides a RESTful web service interface that you can use to interact with data in Microsoft Dataverse by using a wide variety of programming languages and libraries. Use the following resources to learn how to compose requests, query data, manage table rows, and execute operations in batch—all using standard HTTP methods.

> [!TIP]
> New to the Dataverse Web API? Start by reviewing [Web API types and operations](web-api-types-operations.md) to understand the OData service documents that define the entities, functions, and actions available to you.

> [!NOTE]
> The information in this section also applies to Dynamics 365 Customer Engagement (on-premises) users.

## In this section

|Article|Description|
|---------|-------------|
|[Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)|Learn how to set the appropriate HTTP headers and handle errors when interacting with the Web API.|
|[Query data](query/overview.md)|Learn to compose queries using OData to retrieve data from entity collections in Dataverse.|
|[Create a table row](create-entity-web-api.md)|Send a `POST` request to create table rows, including related rows in a single deep insert operation.|
|[Retrieve a table row](retrieve-entity-using-web-api.md)|Use a `GET` request to retrieve a specific record by its unique identifier, including specific properties and related records.|
|[Update and delete table rows](update-delete-entities-using-web-api.md)|Perform update, delete, and upsert operations on table rows, including operations on individual columns.|
|[Associate and disassociate table rows](associate-disassociate-entities-using-web-api.md)|Create and remove relationships between records using the navigation properties defined in the table metadata.|
|[Merge table rows](merge-entity-using-web-api.md)|Combine two duplicate records into one using the `Merge` action for accounts, contacts, leads, and incidents.|
|[Use functions](use-web-api-functions.md)|Use reusable functions with `GET` requests to retrieve data or evaluate values in queries without side effects.|
|[Use actions](use-web-api-actions.md)|Use reusable operations with `POST` requests to perform actions that have side effects, including custom actions.|
|[Execute batch operations](execute-batch-operations-using-web-api.md)|Group multiple operations into a single HTTP request, optionally within a change set to ensure they succeed or fail as a unit.|
|[Impersonate another user](impersonate-another-user-web-api.md)|Execute business logic on behalf of another user, applying that user's role and object-based security.|
|[Perform conditional operations](perform-conditional-operations-using-web-api.md)|Use ETags to perform conditional retrievals, optimistic concurrency control, and limited upsert operations.|
|[Detect duplicate data](manage-duplicate-detection-create-update.md)|Use the `MSCRM.SuppressDuplicateDetection` header to detect and prevent creation of duplicate records.|
|[Troubleshoot Dataverse client errors](/troubleshoot/power-platform/dataverse/dataverse-web-api-and-sdk/web-api-client-errors)|Identify and resolve common client errors encountered when using the Dataverse Web API.|

## Next steps

- [Authenticate to Dataverse with the Web API](authenticate-web-api.md) — Set up authentication before making your first request.
- [Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md) — Start building requests with the correct headers and error handling.
- [Web API types, functions and actions](web-api-types-operations.md) — Explore the OData service documents that define available operations.

### See also

[Use the Dataverse Web API](overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
