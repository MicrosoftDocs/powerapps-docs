---
title: EntityFormOptions | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 418871c0-59dc-4a7c-a8f9-9364a19f7662
---
# EntityFormOptions

Provides access to all the information about the entity forms.

## Available for 

Model-driven apps

## Properties

### createFromEntity

Designates a record that will provide default values based on mapped attribute value. The lookup object has following properties: entity type, id and name.

**Type**: [Entityreference](entityreference.md)

### entityId

Unique Id of the entity record to display the form for. 

**Type**: `string`

### entityName

Logical name of the entity to display the form for. 

**Type**: `string`

### formId

ID of the form instance to be displayed.

**Type**: `string`

### height

Height of the form window to be displayed in pixels.

**Type**: `number`

### openInNewWindow

Whether to display the form in new window.

**Type**: `boolean`

### useQuickCreateForm

Whether to open a quick create form. If you don't specify this, by default false is passed. 

**Type**: `boolean`

### width

Width of the form window to be displayed in pixels.

**Type**: `boolean`

### windowPosition

Specifies the window position on the screen.

**Type**: `number`

The windowPosition value is a number with the following possible values

|Value|Position|
|---|---|
|1|Center|
|2|Side|


## Example

```TypeScript
private onRowClick(event: Event): void {
    let rowRecordId = (event.currentTarget as HTMLTableRowElement).getAttribute(
      RowRecordId
    );
    if (rowRecordId) {
      let entityreference = this.contextObj.parameters.simpleTableGrid.records[
        rowRecordId
      ].getNamedReference();
      let entityFormOptions = {
        entityName: entityreference.entityType!,
        entityId: entityreference.id
      };
      this.contextObj.navigation.openForm(entityFormOptions);
    }
  }
```

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]