---
title: "Configuring header properties in the form designer | MicrosoftDocs"
ms.custom: ""
ms.date: 08/02/2019
ms.reviewer: ""
ms.service: crm-online
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "PowerApps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Configuring header properties in the form designer

## Header density

Makers can control the density of model-driven form headers to match the needs of end-users using the form.

- **High density**  
  High density form header ensures that key information is always visible to end-users. Using high density header, the record title never truncates. Even long record titles are displayed using multiple lines. Similarly, high density header also ensures that up to four field values are directly visible in the header and never truncated or hidden.  

  To ensure that key information is always visible, the framework displays read-only field values and end-users cannot directly edit the field values in the header. Visualizations such as custom controls or web resources are also not allowed.

  When a form does not specify header density or when a new form is created, the framework defaults to high density header.

  ![High density form header](media/form-header-high-density.png)
    
- **Low density**  
  Low density form header allows end-users to directly edit the field values in the header. It also allows visualizations such as custom controls and web resources.  
  
  However, often this comes at the cost of key information being truncated or not readily visible. Low density header truncates the record title as well as field values displayed in the header. Often only one or two fields are directly visible in header and the rest overflow and are displayed in a flyout requiring an extra click.

  ![Low density form header](media/form-header-low-density.png)

### Configuring header density

  > [!NOTE]
  > Use the new form designer, the classic form designer does not provide the ability to configure the header density.

To configure the header density of a model-driven form, follow these steps.
1.	Open the form designer to [create or edit a form](create-and-edit-forms.md).
2.	Select the form header by clicking on the header in the form preview or by using the [tree view](using-tree-view-on-form.md).
3.	In the property pane, select **High density** to use high density form header or unselect it to use low density form header.
4.	In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users.

## Header flyout

The header flyout is displayed when end-users click on the chevron in the form header. It enables end-users to edit field values and also displays visualizations such as custom controls or web resources that are a part of the form header.

The behavior of the header flyout changes depending on the header density configuration.

- **Header flyout with high density header**  
  When using high density form header, the header flyout displays all header fields including the four fields that are directly displayed in the header. The framework defaults to showing the header flyout when high density header is being used. Makers can control the visibility of the header flyout when using high density header.
  
   ![Header flyout with high density header](media/form-header-flyout-high-density.png)

- **Header flyout with low density header**  
  When using low density form header, the header flyout displays only overflow fields i.e. fields that the form is unable to display directly in the header based on the width of the form. The header flyout is also automatically displayed or hidden based on the number of fields in the header and the width of the form. Makers cannot control the visibility of the header flyout when using low density header.

   ![Header flyout with low density header](media/form-header-flyout-low-density.png)

### Showing or hiding the header flyout

To show or hide the header flyout for a model-driven form, follow these steps.

  > [!NOTE]
  > Use the new form designer, the classic form designer does not provide the ability to show or hide the header flyout.
  
1.	Open the form designer to [create or edit a form](create-and-edit-forms.md).
2.	Select the form header by clicking on the header in the form preview or by using the [tree view](using-tree-view-on-form.md).
3.	In the property pane, select **High density** to use high density form header. 

  > [!NOTE]
  > The visibility of header flyout can only be controlled when using high density form header. When using low density header, the header flyout is automatically displayed or hidden based on the number of fields in the header and the width of the form.

4.	In the property pane, select **Show header flyout** to make the header flyout visible or unselect it to hide the header flyout.
5.	In the command bar, select **Save** to save the form, or select **Publish** if you want to save and make your changes visible to users.

## Form designer messages related to form headers

When editing forms using the new or classic form designers, you may see some messages related to form headers. Below you can find the details on each message and why you are seeing it.

- **We've upgraded your form to show a high density header that displays more data. You can edit this setting in the properties of the header.**  
  This message is displayed in the new form designer when a maker creates a new main form (including via the Save as action) or edits a main form that has not previously been configured for header density.  
  
  The framework defaults to high density header and this message is ensuring makers are aware of that behavior. Makers can override the framework default at any time by manually configuring the form header density as outlined earlier.

- **This form isn't using high density header, access the setting in the header properties. High density header helps display more data.**  
  This message is displayed in the new form designer when a maker opens a main form for editing that is configured to use low density header.      
  
  It is aimed at increasing awareness amongst makers about the high density header and its benefits.

- **Field moved to header flyout: The header supports displaying up to four read-only field values. The field *[field display name]* will now only be available from the flyout.**  
  This message is displayed in the new form designer when a form is using high density header with the header flyout visible.  
  
  High density header displays read-only values of the first four fields in the header. When makers add a field in the header in the top four positions it causes an existing field that was being directly displayed in the header to be pushed out and visible only in the header flyout.      
  
  This message is informing the maker of the change and confirming if they would like to proceed with the action.

- **Header field limit exceeded: The header supports displaying up to four read-only field values. Remove unused fields to add more.**  
  This message is displayed in the new form designer when a form is using high density header with the header flyout hidden.  
  
  High density header displays read-only values of up to four fields in the header. Since the header flyout is hidden end-users will be unable to see any additional fields.  
  
  This message is informing the maker that they already have four fields in the header and preventing them from accidentally adding additional fields in the header that end-users will not be able to see.

- **Header does not display custom components: The header supports displaying up to four read-only field values. Remove the custom component from the field before adding it to the header.**  
  This message is displayed in the new form designer when a form is using high density header with the header flyout hidden.  
  
  High density header displays read-only values of fields in the header. Since the header flyout is hidden end-users will be unable to see any custom components associated with the fields in the header.  
  
  This message is informing the maker that they are trying to add a field with an associated custom component to the header and that they need to remove the custom component before adding the field to the header since end-users will not be able to see the custom component in the header.

- **Header displays read-only field values: The header supports displaying up to four read-only field values. To provide editability to the end user, add the field to a section in the form.**  
  This message is displayed in the new form designer when a form is using high density header with the header flyout hidden.  
  
  High density header displays read-only values of fields in the header. Since the header flyout is hidden end-users will be unable to edit field values.  
  
  This message is informing the maker that any fields added to the header will be read-only and that any fields they want end-users to edit should also be added to a section in the form.

- **Header field values are not editable: Moving a field from the body to the header will display as a read-only value. To maintain editability, copy the field to the header.**  
  This message is displayed in the new form designer only for forms using high density header with the header flyout hidden.  
  
  High density header displays read-only values of fields in the header. Since the header flyout is hidden end-users will be unable to edit field values.  
  
  This message is informing the maker that they are trying to move a field from the form body to the form header and doing so will make it read-only. It gives them the choice of moving the field to the header or adding a copy of the field to the header. Moving the field to the header will mean that the field will no longer be available in the original location on the form body for end-users to edit. Adding a copy of the field to the header will leave the field in the original location as-is ensuring that end-users can continue to edit it via the form body.

- **Form headers now default to high density to display more data. Use the new form designer to edit header density.**  
  This message is displayed in the classic form designer when a maker opens a main form for editing and it is configured to use low density header.  
  
  It is aimed at increasing awareness amongst makers about the high density header and its benefits and that makers should use the new form designer to configure header density.  

- **This form is using high density header. For the best authoring experience with this form, use the new form designer.**  
  This message is displayed in the classic form designer when a maker opens a main form for editing and it is configured to use high density header.  
  
  The classic form designer does not provide a WYSIWYG authoring experience. It also does not detect and prevent or warn makers about the implications of changes they make to the form header. For example: When editing a form that is using high density header with the header flyout hidden, the classic form designer will not prevent makers from adding more than four fields to the header even though these field will not be available to end-users.  
  
  This message is informing the maker that when editing a form that is using high density header they should use the new form designer to ensure they are aware of the impact of their changes to form header.
