---
title: "Model-driven app timer control in PowerApps | MicrosoftDocs"
description: "Understand how you can use the timer control"
ms.custom: ""
ms.date: 06/06/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: b2b64771-083b-42f9-a3d5-2218f9d8a713
caps.latest.revision: 63
ms.author: "matp"
manager: "kvivek"
---
# Model-driven app timer control overview

 Use a timer control with forms where records need to meet a specific time-based milestone. A timer control shows people how much time is available to complete an action in the resolution of an active record or how much time has passed since the time to complete the action has passed. At a minimum, timer controls must be configured to show success or failure in completing the action. In addition, they can be configured to display warnings when the conditions are approaching failure.  
  
 A timer control can be added to a form for any entity, but they are most frequently used for the case entity, especially when linked to fields that track service level agreements. You can add multiple timer controls in the body of a form. You can’t add them to the header or footer.  
  
 Timer control **Data Source** properties use fields for the entity.  
  
-   The **Failure Time Field** uses a date-time field to set the time.  
  
-   The three condition fields use one of the **Option Set**, **Two Options**, **Status**, or **Status Reason** fields for the entity.  

To create a timer control, in the form designer select the **Insert** tab, and then on the toolbar select **Timer**. 

  > [!div class="mx-imgBorder"] 
  > ![Insert timer control](media/insert-timer-control.png)

On the Timer Control properties page, enter or select the properties that you want, and then select **OK**. 

  
<a name="BKMK_TimerControlProperties"></a>   

## Timer control properties  
 The following table describes the properties of a timer control.  
  
|Group|Name|Description|  
|-----------|----------|-----------------|  
|Name|Name|**Required**. A unique name for the control.|  
||Label|**Required**. The label to display for the timer control.|  
|Data Source|Failure Time Field|**Required**. Choose one of the date-time fields for the entity to represent when a milestone should be successfully completed.|  
||Success Condition|**Required**. Select a field for the entity to evaluate the success of the milestone, then choose which option indicates success.|  
||Warning Condition|Select a field for the entity to evaluate whether the success of the milestone is at risk so that a warning should be displayed, then choose which option indicates that a warning should be displayed.|  
||Cancel Condition|Select a field for the entity to evaluate whether the achievement of th milestone should be cancelled, then choose which option indicates that the milestone is cancelled.|  

## Next steps

[Overview of the form editor user interface](form-editor-user-interface-legacy.md)