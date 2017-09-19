<properties
	pageTitle="Create a rule | Microsoft PowerApps"
	description="Step-by-step instructions for building app logic by creating rules"
	services=""
	suite="PowerApps"
	documentationCenter="na"
	authors="karthik-1"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="09/14/2017"
   ms.author="karthikb"/>

# Create a rule in PowerApps #
Create rules to automatically modify an app based on criteria that you specify. For example, show list items in red, yellow, or green based on their status, or show an approval button only for certain users (such as managers).

You can add rules to a variety of controls. In this topic, you'll add a rule to change the text color of a **Label** control if the value of a **Slider** control is greater than 70.

## Add a rule ##
1. Select a control (or add a control and leave it selected).

	For this topic, [add a label and a slider](add-configure-controls.md), set the label's **Text** property to **Slider1.Value**, and then select the slider.

1. In the right-hand panel, click or tap **Rules**, and then click or tap **New rule**.

	![Create new rule](./media/working-with-rules/new-rule.png)

	If you select a control for which one or more rules has already been defined, you can edit any of them if you click or tap it.  

## Add a condition ##
A condition is an expression that evaluates to true or false, such as whether a value is greater than 70. You can write the expression based on a template or start from scratch, and you can customize the expression based on guidance in the UI (Intellisense).

1. Click or tap **Add a condition**, and then click a template or **Custom condition**.

	For this topic, click or tap **Greater than**.

	![Add condition](./media/working-with-rules/rule-conditions.png)

1. Finish the expression to define when the rule applies.

	For this topic, use this expression:
	<br>**Value(Slider1.Value) > 70**

	**Note**: As of this writing, you must specify the property of the control used in the comparison. In future releases, PowerApps might infer common properties of the control (such as **Text** or **Value**).

## Add an action ##
Actions define what happens when the rule is applied. PowerApps can create actions automatically based on changes you make to controls.

1. Click or tap **Define actions**.

	![Define actions](./media/working-with-rules/rule-define-actions.png)

1. In the confirmation dialog box, click or tap **Let's go** so that PowerApps will capture your next change or changes as one or more actions.

1. Configure one or more controls to match your expectations when the condition is true.

	For this topic, change the color of the label.

	![Capture properties](./media/working-with-rules/rule-capture-properties.png)

1. (optional) Review your changes by clicking or tapping **Show actions**.

	![Review actions](./media/working-with-rules/rule-review-actions.png)

1. When you finish adding actions, click or tap **Done**.

1. Review the condition and actions for the rule, and then click or tap **Done** to save it.

	![Review rule](./media/working-with-rules/rule-review.png)

## Test the rule ##
1. Preview the app by pressing F5 (or by clicking the play button near the upper-right corner).

	![Open preview](./media/working-with-rules/open-preview.png)

1. Make the condition that you specified true, and then confirm that the actions work as you expect.

	For this topic, set the slider to a value that's greater than 70, and confirm that the label text changes color.

## Known limitations ##
As of this writing:

- You can't rename rules.
- You can't specify the **ThisItem** property of a form or a gallery as part of a condition.
