---
title: "Grid OnSave event (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the grid OnSave event.
author: clromano
ms.author: clromano
ms.date: 09/15/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Grid OnSave event (Client API reference)

The `OnSave` event occurs before sending the updated information to the server, and when any of the following occurs:

- There's a change in the record selection.
- The user explicitly triggers a save operation using the editable grid's save button.
- The user applies a sort, filter, group, pagination, or navigation operation from the editable grid while there are pending changes.

Some important points to consider for the `OnSave` event: 

- If a user edits multiple columns of the same record in sequence, the `OnSave` event occurs only once to ensure optimal performance and form behavior compatibility.
- Editable grid and the parent form have separate save buttons. Selecting the save button in one doesn't save changes in the other.
- Editable grid doesn't save pending changes when navigation operations are performed outside of its context. If the control has unsaved data, that data might be lost. So, the `OnSave` event might not fire. For example, the `OnSave` event might not fire when navigating to a different record using a form lookup column or through the ribbon.
- Selecting the refresh button in the editable grid causes it to discard any pending changes, and the `OnSave` event isn't fired.
- Editable grid control doesn't implement an auto-save timer.
Editable grid suppresses duplicate detection rules.

[!INCLUDE [cc_book-instead-of-save](../../../../../includes/cc_book-instead-of-save.md)]

### Related articles

[Form OnSave Event](form-onsave.md)   
[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
