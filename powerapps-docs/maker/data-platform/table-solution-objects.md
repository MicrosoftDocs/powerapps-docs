---
title: "Tables representing solution objects | MicrosoftDocs"
description: "Learn the different ways that a table can be edited"
ms.custom: ""
ms.date: 10/20/2020
ms.reviewer: ""
ms.topic: "conceptual"
author: "Mattp123"
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Tables representing solution objects

Some standard tables in Dataverse represent the structure and instances of solution objects. If you are not familiar with solutions, go to [Solutions overview](solutions-overview.md).

For example, the [Custom API](/power-apps/developer/data-platform/custom-api) table has columns that represent the properties of an API, such as **Name** and **Binding Type**, with each row of data in the table representing a particular API instance.

:::image type="content" source="media/table-soln-objects.png" alt-text="A website built using Power Pages.":::


When viewing these tables directly in Power Apps ([make.powerapps.com](https://make.powerapps.com)), you will see a warning stating that the data in the table is read only. This ensures the instances of these objects are not changed.

To update data in such tables, you must navigate to the objects themselves in solution. In our example of Custom API, you can open a solution that contains the Custom API object or add the Custom API object to a new solution and then customize the attributes.  

### See also
[Create a table](data-platform-create-entity.md)<br/>
[Edit a table](edit-entities.md)<br/>
[Create a solution](create-solution.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]