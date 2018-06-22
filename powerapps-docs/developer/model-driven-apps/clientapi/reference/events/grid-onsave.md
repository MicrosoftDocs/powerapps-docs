---
title: "Grid OnSave Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Grid OnSave Event (Client API reference)



The `OnSave` event occurs before sending the updated information to the server, and when any of the following occurs: 
- There is a change in the record selection.
- The user explicitly triggers a save operation using the editable grid’s save button.
- The user applies a sort, filter, group, pagination, or navigation operation from the editable grid while there are pending changes.

Some important points to consider for the `OnSave` event: 
- If a user edits multiple columns of the same record in sequence, the OnSave event will only be fired once to ensure optimal performance and form behavior compatibility.
- Editable grid and the parent form have separate save buttons. Clicking the save button in one will not save changes in the other.
- Editable grid does not save pending changes when navigation operations are performed outside of its context. If the control has unsaved data, that data may be lost. Consequently, the `OnSave` event may not fire. For example, this could happen when navigating to a different record using a form lookup field or through the ribbon.
- Pressing the refresh button in the editable grid causes it to discard any pending changes, and the `OnSave` event won't be fired.
- Editable grid control does not implement an auto-save timer.
Editable grid suppresses duplicate detection rules.

### Related topic
[Form OnSave Event](form-onsave.md)



