---
title: Add custom JavaScript to a list
description: Learn how to add custom JavaScript to a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 04/04/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# Add custom JavaScript to a list

The Options tab on the form contains a text area where you can enter custom [!INCLUDE[pn-javascript](../../../includes/pn-javascript.md)]. If your page includes jQuery library, you can use that here as well. The script block will be added at the bottom of the webpage just before the page’s closing form tag.

![Custom JavaScript example.](../media/custom-javascript-example.png "Custom JavaScript example")  

The list gets its data asynchronously, and when it's complete it will trigger an event `loaded` that your custom [!INCLUDE[pn-javascript](../../../includes/pn-javascript.md)] can listen for and do something with items in the grid. The following code is a trivial example:
```
$(document).ready(function (){
$(".entitylist.entity-grid").on("loaded", function () {
$(this).children(".view-grid").find("tr").each(function (){
// do something with each row
$(this).css("background-color", "yellow");
});
});
}); 
```

Find a particular attribute field and get its value to possibly modify the rendering of the value. The following code gets each table cell that contains the value of the `accountnumber` attribute. Replace `accountnumber` with an attribute appropriate for your table and view.
```
$(document).ready(function (){
   $(".entitylist.entity-grid").on("loaded", function () {
      $(this).children(".view-grid").find("td[data-attribute='accountnumber']").each(function (i, e){
         var value = $(this).data(value);
         // now that you have the value you can do something to the value
      });
   });
});
```

### See also

- [Microsoft Learn: Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
