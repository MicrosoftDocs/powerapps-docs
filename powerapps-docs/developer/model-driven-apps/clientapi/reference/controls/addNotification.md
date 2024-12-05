---
title: "addNotification (Client API reference) in model-driven apps"
description: Displays an error or recommendation notification for a control, and lets you specify to execute based on the notification.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addNotification (Client API reference)

Displays an error or recommendation notification for a control, and lets you specify actions to execute based on the notification. When you specify an error type of notification, a red "X" icon appears next to the control. When you specify a recommendation type of notification, an "i" icon appears next to the control. On Dynamics 365 mobile clients, tapping on the icon will display the message, and let you perform the configured action by clicking the **Apply** button or dismiss the message. 

## Control types supported

All

## Syntax

`formContext.getControl(arg).addNotification(notification);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`notification`|Object|Yes|The notification to add. See [`notification` parameter](#notification-parameter)|

## `notification` parameter

The `notification` parameter accepts an object with the following properties

|Name|Type|Required|Description|
|---|---|---|---|
|`actions`|Array of objects|No|See [`actions` property](#actions-property)|
|`messages`|Array of Strings|Yes|The message to display in the notification. In the current release, only the first message specified in this array will be displayed. The string that you specify here appears as bold text in the notification, and is typically used for title or subject of the notification. You should limit your message to 50 characters for optimal user experience.|
|`notificationLevel`|String|Yes|Defines the type of notification. Valid values are `ERROR` or `RECOMMENDATION`.|
|`uniqueId`|String|Yes|The ID to use to clear this notification when using the [clearNotification method](clearNotification.md).|

### `actions` property

The `actions` property contains an array of objects with the following properties:

|Name|Type|Required|Description|
|---|---|---|---|
|`message`|String|No|The body message of the notification to be displayed to the user. Limit your message to 100 characters for optimal user experience.|
|`actions`|Array of functions|No|The corresponding actions for the message.|

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Boolean

**Description**: Indicates whether the method succeeded.


## Remarks

In web client the **addNotification** method displays a notification with the messages you specified and two standard buttons: **Apply** and **Dismiss**. Clicking **Apply** executes the action you define; clicking **Dismiss** closes the notification message.

In Unified Interface:

- There is no **Dismiss** button.
- The **Apply** button only appears when the notification level is set to **RECOMMENDATION**, not **ERROR**.

## Example

The following sample code displays a notification on the **Account Name** column of the account form to set the **Ticker Symbol** if the **Account Name** column contains "Microsoft", and the ticker symbol is not already set to "MSFT". Clicking **Apply** in the notification will set the **Ticker Symbol** column to "MSFT".

```JavaScript
function addTickerSymbolRecommendation(executionContext) {
    var formContext = executionContext.getFormContext();
    var myControl = formContext.getControl('name');
    var accountName = formContext.data.entity.attributes.get('name');
    var tickerSymbol = formContext.data.entity.attributes.get('tickersymbol');

    if (accountName.getValue() == 'Microsoft' && tickerSymbol.getValue() != 'MSFT') {
        var actionCollection = {
            message: 'Set the Ticker Symbol to MSFT?',
            actions: null
        };

        actionCollection.actions = [function () {
            tickerSymbol.setValue('MSFT');
            myControl.clearNotification('my_unique_id');
        }];

        myControl.addNotification({
            messages: ['Set Ticker Symbol'],
            notificationLevel: 'RECOMMENDATION',
            uniqueId: 'my_unique_id',
            actions: [actionCollection]
        });
    }
    else
        console.log("Notification not set");
}
```

This how the notification appears in model-driven apps:

> [!div class="mx-imgBorder"]
> ![Example add notification.](../../../media/clientapi_addnotification.png "Example add notification")

### Related articles

[clearNotification](clearNotification.md)   
[setNotification](setNotification.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
