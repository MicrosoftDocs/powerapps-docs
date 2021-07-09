---
title: "Invoke custom process actions from a workflow | MicrosoftDocs"
description: "Learn how to invoke a custom process action from a workflow"
ms.custom: ""
ms.date: 04/28/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "Power Apps"
author: "Mattp123"
ms.assetid: 1fd5d39e-3dc8-4d1a-8b4b-ccaa303f4bbb
caps.latest.revision: 12
ms.author: "matp"
manager: "kvivek"
search.app: 
  - Flow
search.audienceType: 
  - flowmaker
  - enduser
---


<!-- Be sure to update publication date. -->


# Invoke custom process actions from a workflow


Workflows have numerous capabilities supporting business scenarios. Calling basic data operation actions for a row, such as create, update, and delete, from within a workflow solves quite a few business scenarios. However, if you couple the capabilities of the workflows with the power of the custom processs actions invoked directly from within a workflow, you add a whole new range of business scenarios to your application without needing to write code.  
  
Let’s look at the scenario in which a custom process action is invoked from a workflow. We’ll invoke a custom process action to request the manager’s approval when a discount for a particular opportunity exceeds 20 percent.  
  
<a name="action"></a>

## Example: Create a custom process action using the opportunity table
  
1. In [solution explorer](../model-driven-apps/advanced-navigation.md#solution-explorer), select **Processes**.  
  
2.  On the Nav bar, choose **New**. Give the process a name and choose the **Action** category.  
  
To request an approval for the discount, we’re using a custom action called **Approval Process**. We added an input parameter, **SpecialNotes**, and a **Send email** step to create a new message and send a request for the manager’s approval, as shown here.  
  
![Add a step &#45; send email.](media/enable-custom-action-approval-proces-sadd-email.png "Add a step - send email")  
  
To configure the email message, choose **Set Properties**. When the form opens, use the **Form Assistant** to add special notes and other information to the email, as highlighted on the screenshot. To add the special notes, place the cursor where you want the notes to appear in the message, and then, in the **Form Assistant**, under **Look for**, choose **Arguments** in the first drop-down list and choose **SpecialNotes** in the second drop-down list, and then choose **OK**.  
  
![Set up email.](media/enable-custom-action-approval-process-setup-email.png "Set up email")  
  
Before you can invoke the custom process action from a workflow, you have to activate it. After you have activated the action, you can view its properties by choosing **View properties**.  
  
![Activate custom action &#45; approval process.](media/enable-custom-action-approval-process-activate-action.png "Activate custom action - approval process")  
  
<a name="workflow"></a>

## Invoke a custom process action from a workflow  
  
1. In [solution explorer](../model-driven-apps/advanced-navigation.md#solution-explorer), select **Processes**.   
  
2.  On the Nav bar, choose **New**. Give the process a name and choose the **Workflow** category.  
  
We created a workflow that invokes the **Approval Process** custom action whenever the manager’s approval for a discount of more than 20 percent for an opportunity is required.  
  
![Set action properties from workflow.](media/enable-custom-action-from-workflow.png "Set action properties from workflow")  
  
You can set the custom process action’s input properties by choosing **Set Properties**. We added a name of the account related to the opportunity in the special notes. In the **Form Assistant**, under **Look for**, choose **Account** in the first drop-down list, choose **Account Name** in the second drop-down list, and then choose **OK**. The **Target** property is required and it is populated by the system. The **{Opportunity(Opportunity)}** in the **Target** property is the same opportunity that the calling workflow is running on. Alternatively, you can choose a specific opportunity for the target property by using lookup.  
  
![Set input parameters for ApprovalProcess action.](media/enable-customaction-workflow-set-properties.png "Set input parameters for ApprovalProcess action")  
  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]