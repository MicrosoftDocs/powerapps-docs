---
title: Edit table data in Excel and publish it back to Dataverse for Teams | Microsoft Docs
description: Explains how to edit table data in Dataverse for Teams.
author: matp
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/13/2021
ms.subservice: teams
ms.author: lanced
ms.reviewer: matp
---

# Edit table data in Excel and publish it back to Dataverse for Teams

By opening Dataverse for Teams table data in Microsoft Excel, you can quickly and easily view and edit the data by using the Microsoft Power Apps Office Add-in.
:::image type="content" source="../maker/data-platform/media/data-platform-cds-excel-addin/ExcelAddin.png" alt-text="Dataverse for Teams table data in Excel.":::

To install the Power Apps Excel Add-in, see [Microsoft PowerApps Office Add-in](https://appsource.microsoft.com/product/office/WA104380330?tab=Overview). For more information about how to add or remove an Office Excel Add-in, see [Add or remove add-ins in Excel](https://support.office.com/article/add-or-remove-add-ins-in-excel-0af570c4-5cf3-4fa9-9b88-403625a0b460).

## Open table data in Excel

1. Sign in to Teams, and then in the left pane, select the **Power Apps**.
1. Select the **Build** tab, and then select **See all**.
1. In the left navigation pane, select **Tables**, next to the table you want, select **…**, and then select **Edit data in Excel**.
   :::image type="content" source="media/edit-data-in-excel.png" alt-text="Edit data in Excel command.":::

1. Open the Excel worksheet that is downloaded to your browser's default download folder named similar to *crdcb_table-name (1591125669213).xlsx*.
1. In Excel, select **Enable editing** to enable the Power Apps Excel Add-in to run. The Excel Add-in runs in a pane on the right side of the Excel window.

> [!IMPORTANT]
> - If the pane displays an error message, see [Office Store Add-in download disabling](../maker/data-platform/data-platform-excel-addin.md#office-store-add-in-download-disabling).
> - If this is the first time that you've run the Power Apps Excel Add-in, you must **Trust this Add-in** to allow the Excel Add-in to run.
> - The maximum table size when editing in Excel is one million cells. If there are too many rows or columns, not all data will be read or published.

## Next steps
- [View and refresh data in Excel](../maker/data-platform/data-platform-excel-addin.md#view-and-refresh-data-in-excel)
- [Edit data in Excel](../maker/data-platform/data-platform-excel-addin.md#edit-data-in-excel)
- [Configure the add-in to adjust tables and columns](../maker/data-platform/data-platform-excel-addin.md#configure-the-add-in-to-adjust-tables-and-columns)
- [Troubleshooting](../maker/data-platform/data-platform-excel-addin.md#troubleshooting)
