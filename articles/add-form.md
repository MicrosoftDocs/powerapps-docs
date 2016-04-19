<properties
    pageTitle="Show, edit, or add a record from a table | Microsoft PowerApps"
    description="Use a form to show, edit, or add a record from a table in your data source."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="sarafankit"
    manager="erikre"
    editor=""
    tags=""/>
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="04/13/2016"
    ms.author="ankitsar"/>

# Show, edit, or add a record from a table #
To show all fields in a record, add and configure a [**DisplayForm**](./controls/control-form-detail.md) control. To edit any field in a record (or to add a record) and save your changes back to a data source, add and configure an [**Edit Form**](./controls/control-form-detail.md) control.

**Prerequisites**

- Create an app, or add a screen to an app.
- Learn how to [configure a control](./add-configure-controls.md) in PowerApps.
- A [connection](./add-data-connection.md) to **FlooringEstimates** table from [this Excel file](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx), which contains sample data for this tutorial.

## Add a form, and show data ##
1. Add a [**Drop down**](./controls/control-drop-down.md) control, name it **ChooseProduct**, and set its **Items** property to this value:

	**FlooringEstimates.Name**

	The list shows names of flooring products from the data source.

1. Add a **Display form** or an **Edit form**, move it below **ChooseProduct**, and resize the form to cover most of the screen.

    ![Add a form](./media/add-form/add-a-form.png)

1.  Set the **DataSource** property of the form to **FlooringEstimates** and the **Item** property of the form to this formula:

	**First(Filter(FlooringEstimates,Name=ChooseProduct.Selected.Value))**

    This formula specifies that the form will show the record that the user selects in **ChooseProduct**.

## Show or hide fields on the form ##
1. If the **Options** pane isn't open, make sure that the form is still selected, and select **Options** near the lower-right corner.

	![Open Options pane](./media/add-form/open-options.png)

	The **Form** customization tab of the **Options** pane appears.

    ![Form options](./media/add-form/form-options.png)

1. In the **Options** pane, select show field option for all the fields

	![Show fields on form](./media/add-form/show-fields.png)

## Set the card type for a field##
1. In the **Options** pane, select the card selector for **Price**.

    ![Expand Card Selector](./media/add-form/card-selector.png)

1. Select the **View text** option.

    ![View text Card](./media/add-form/select-text-card.png)

## Arrange cards on the form##
1. Select **Category**, and then drag the field's title bar above **Image**.

    ![Select a card](./media/add-form/select-card.png)

    ![Drop a card](./media/add-form/card-on-top.png)

## Submit changes for an Edit form##
1. Add a button to the bottom of the form, and set its **Text** property to **Save**

	![Add a save button](./media/add-form/add-a-save-button.png)  

1.  On the **Formula Bar**, set the **OnSelect** property of the **Save** button to [submit the form](./functions/function-form.md") to save the changes to the record:

	```
	SubmitForm(Form1);
	```

## Next steps ##
- Learn more about [working with Forms](./working-with-forms.md)
- Learn more about [formulas](./working-with-formulas.md) in PowerApps
