---
title: "Configure a web form steps for a portal | MicrosoftDocs"
description: "Instructions to create a web form step for a web form on a portal."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/04/2019
ms.author: tapanm
ms.reviewer:
---

# Define web form steps for portals

The Web Form Step provides the flow logic of the form's user experience such as steps and conditional branching. It also provided details regarding the rendering of a form and additional behavior.

> [!NOTE]
> Web Forms persists the history of the steps a user has visited in an object on a Web Form Session entity. If a Web Form's steps have been modified, previously created history data could now be stale. Anytime steps are changed, it is recommended that you delete all Web Form Session records to eliminate miss match between sequence of steps logged in history and the current sequence.

Each Web Form will be presented on the portal has one or more steps. These steps share some common properties, outlined below. Each Step contains a pointer (a lookup) to the next step, with the exception of terminal steps. Terminal steps do not have a next time, and are thus the last step of the Web Form (due to conditional branching, there can be multiple terminal steps)

![Steps to create a web form](../media/web-form-creation-steps.png "Steps to create a web form")  

| Name     | Description                                    |
|----------|------------------------------------------------|
| Name     | A title used for reference.                    |
| Web Form | The Web Form associated with the current step. |
|Type|One of the following:<br>[Load Form/Load Tab step type](load-form-step.md): displays properties of forms. <ul><li>[Load Form/Load Tab step type](load-form-step.md): displays properties of tabs.</li><li>[Conditional step type](add-conditional-step.md): displays properties for specifying expressions to be evaluated for conditional branching. </li><li>[Redirect step type](add-redirect-step.md): displays the settings appropriate for configuring a website redirection.</li></ul><br>For further details on the settings for these web form step types, please refer to their corresponding sections below.<br>**Note**: The first step cannot be of type "Condition".|
| Next Step                  | The step that will follow the current step. This will be blank for single step single form.                                                                                                            |
| Target Entity Logical Name | The logical name of the entity associated with the form.                                                                                                                                               |
| Move Previous Permitted    | Indicates whether the user is given an option to navigate to the previous step in a multiple step web form. Default is true. Uncheck to prevent the user from being able to move to the previous step. |
||

### See also

[Configure a portal](configure-portal.md)  
[Define entity](entity-forms.md)  
[Load Form/Load Tab step type](load-form-step.md)  
[Redirect step type](add-redirect-step.md)  
[Conditional step type](add-conditional-step.md)  
[Add custom JavaScript](add-custom-javascript.md)  

