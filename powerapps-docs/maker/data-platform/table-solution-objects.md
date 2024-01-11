---
title: "View and edit tables representing solution objects | MicrosoftDocs"
description: "Learn about tables in Dataverse that represent the structure and instances of solution objects."
ms.custom: ""
ms.date: 05/18/2022
ms.reviewer: "matp"
ms.topic: "conceptual"
author: "si-matthews"
ms.subservice: dataverse-maker
ms.author: "simatthe"
search.audienceType: 
  - maker
---
# View and edit tables representing solution objects

Some standard tables in Dataverse represent the structure and instances of solution objects. If you aren't familiar with solutions, go to [Solutions overview](solutions-overview.md).

For example, the **Custom API** table has columns that represent the properties of an API, such as **Name** and **Binding Type**, with each row of data in the table representing a particular API instance. For more information about Custom API table, go to [Custom API table columns](../../developer/data-platform/custom-api-tables.md#custom-api-table-columns)

:::image type="content" source="media/table-soln-objects.png" alt-text="custom API table in Dataverse":::

When viewing these tables in Power Apps ([make.powerapps.com](https://make.powerapps.com)), you'll see a warning stating that the data in the table is read only. This ensures the instances of these objects aren't changed.

To update data in such tables, you must navigate to the respective objects in the solution. In our example of custom API, you can open a solution that contains the custom API object or add the custom API object to a new solution and then customize the data as required.

:::image type="content" source="media/edit-table-soln-objects.png" alt-text="Customize fields.":::  

### See also
[Create a table](data-platform-create-entity.md)<br/>
[Edit a table](edit-entities.md)<br/>
[Create a solution](create-solution.md)<br/>
[Create and use custom APIs](../../developer/data-platform/custom-api.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
