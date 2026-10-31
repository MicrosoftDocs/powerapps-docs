---
title: "Controls Collection (Client API Reference)"
description: "Learn how to use the Controls collection in the Client API to access every control associated with a column on a model-driven app form. Explore usage tips now."
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Controls collection (Client API reference)


Use the `controls` collection to access controls associated with columns. 

When you perform actions on controls that are tied to a column, consider that the control might appear on the page more than once. Generally, you should perform the same actions for each control for the column. You can loop through the column controls collection and perform the actions on each control.

For example, to add a notification to each control bound to the `name` column, use the following code:

```JavaScript
const notification = {
    messages: ['Sample Notification on Name Controls'],
    notificationLevel: 'RECOMMENDATION',
    uniqueId: 'my_unique_id'
 };
 
formContext.getAttribute("name").controls.forEach(control =>
    control.addNotification(notification)
 );
```

Because each column can appear more than once on the page, the controls collection provides access to all controls that represent that column. If the column is represented by only one control on the page, the length of this collection is 1. 

When you use the control [getName](../controls/getName.md) method, the name of the first control matches the name of the column. The second instance of a control for that column is `<columnName>1`. The pattern `<columnName>+N` continues for each additional control added to the form for a specific column.

When a form displays a business process flow control in the header, it adds controls for each column that appears in the business process flow. These controls have a unique name like the following: `header_process_<column name>`.


## Related articles

[Columns (Client API reference)](../attributes.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
