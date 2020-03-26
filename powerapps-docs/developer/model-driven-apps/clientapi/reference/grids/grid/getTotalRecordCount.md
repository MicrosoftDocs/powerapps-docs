---
title: "getTotalRecordCount (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8305f0cb-9959-4429-a721-a864ade4cd35
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getTotalRecordCount (Client API reference)



[!INCLUDE[./includes/getTotalRecordCount-description.md](./includes/getTotalRecordCount-description.md)]

- When the Dynamics 365 for Outlook client isn’t connected to the server, this number is limited to those records that the user has selected to take offline.
- For Dynamics 365 mobile clients, this method will return the number of records in the subgrid.

## Grid types supported

Read-only and editable grids

## Syntax

`var filteredRecordCount = gridContext.getGrid().getTotalRecordCount();`

## Return Value

**Type**: Number

**Description**: Total number of records that match the filter criteria of the view.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

See [Collections (Client API reference)](../../collections.md) for information on the methods available to access data in a collection.

