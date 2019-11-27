---
title: " Table component| Microsoft Docs" 
description: "Implementing a table component" 
ms.custom: ""
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "article"
ms.author: "nabuthuk" 
author: Nkrb
---

# Implementing table component

This sample component renders a table with two columns. The left column shows the name of the API method or property, and the right column shows the value returned by the API. You can open this component on the different type of devices or modify your language or user settings to see the values adjust correctly in the table.

> [!div class="mx-imgBorder"]
> ![Table component](../media/table-control.png "Table component")

## Available for 

Model-driven apps

> ![!NOTE]
> When you debug the table component using the command `npm start`, the component is not rendered in the test harness. This is because the component uses the `context.utils.getEntityMetadata`  method which is not supported by the PowerApps CLI tooling yet.

## Manifest

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest>
	<control namespace="SampleNamespace" constructor="TSTableControl" version="1.0.0" display-name-key="TS_TableControl_Display_Key" description-key="TS_TableControl_Desc_Key" control-type="standard">
		<property name="stringProperty" display-name-key="stringProperty_Display_Key" description-key="stringProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
		<resources>
			<code path="index.ts" order="1" />
			<css path="css/TS_TableControl.css" order="2" />
		</resources>
	</control>
</manifest>
```

## Code

```TypeScript
export class TSTableControl
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // Flag to track if control is in full screen mode or not
  private _isFullScreen: boolean;
  // reference to HTMLTableElement rendered by control
  private _tableElement: HTMLTableElement;
  // reference to 'Set Full Screen' HTMLButtonElement
  private _setFullScreenButton: HTMLButtonElement;
  // reference to 'Lookup Objects' HTMLButtonElement
  private _lookupObjectsButton: HTMLButtonElement;
  // reference to 'Lookup Result Div' HTMLDivElement
  // Used to display information about the item selected by the lookup
  private _lookupObjectsResultDiv: HTMLDivElement;
  // reference to the control container HTMLDivElement
  // This element contains all elements of our custom control example
  private _container: HTMLDivElement;
  // reference to ComponentFramework Context object
  private _context: ComponentFramework.Context<IInputs>;
  // Flag if control view has been rendered
  private _controlViewRendered: Boolean;
  // Label displayed in lookup result div
  // NOTE: See localization sample control for information on how to localize strings into multiple languages
  private LOOKUP_OBJECTS_RESULT_DIV_STRING: string =
    "Item selected by lookupObjects method:";
  // Prefix for label displayed
  // NOTE: See localization sample control for information on how to localize strings into multiple languages
  private BUTTON_LABEL_CLICK_STRING: string = "Click to invoke:";
  // Name of entity to use for metadata retrieve example (this entity needs to exist in your org)
  private ENTITY_LOGICAL_NAME_FOR_METADATA_EXAMPLE = "account";
  /**
   * Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
   * Data-set values are not initialized here, use updateView.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
   * @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
   * @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
   * @param container If control is marked control-type='standard', it receives an empty div element within which it can render its content.
   */
  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ) {
    this._isFullScreen = false;
    this._controlViewRendered = false;
    this._context = context;
    this._container = document.createElement("div");
    this._container.classList.add("TSTable_Container");
    container.appendChild(this._container);
  }
  /**
   * Creates an HTMLButtonElement with the provided label
   * Attaches the provided method to the "onclick" event of the button element
   * @param buttonLabel : Label to set on button element
   * @param onClickHandler : event handler to attach to button's "onclick" event
   * @param entityName : entityName to store in the button's attribute
   */
  private createHTMLButtonElement(
    buttonLabel: string,
    onClickHandler: (event?: any) => void,
    entityName: string | null
  ): HTMLButtonElement {
    let button: HTMLButtonElement = document.createElement("button");
    button.innerHTML = buttonLabel;
    if (entityName != null) {
      button.setAttribute("entityName", entityName);
    }
    button.classList.add("SampleControlHtmlTable_ButtonClass");
    button.addEventListener("click", onClickHandler);
    return button;
  }
  /**
   * Returns the label to display on the 'set full screen' button
   * @param isFullScreenVal : True if control is currently in 'full screen' mode
   */
  private getSetFullScreenButtonLabel(isFullScreenVal: boolean): string {
    return (
      this.BUTTON_LABEL_CLICK_STRING +
      " setFullScreen(" +
      String(isFullScreenVal) +
      ")"
    );
  }
  /**
   * Event handler for 'Set Full Screen' button
   *
   * This method will transition the control to full screen state if it is currently in non-full screen state, or transition
   * the control out of full screen state if it is currently in full screen state
   *
   * It will also update the label on the 'Set Full Screen' button, and update the interal _isFullScreen state variable
   * to maintain the control's updated state
   *
   * @param event : OnClick Event
   */
  private onSetFullScreenButtonClick(event: Event): void {
    this._context.mode.setFullScreen(!this._isFullScreen);
    this._setFullScreenButton.innerHTML = this.getSetFullScreenButtonLabel(
      this._isFullScreen
    );
    this._isFullScreen = !this._isFullScreen;
  }
  /**
   * Event handler for 'lookup objects' button
   *
   * This method invokes the lookup dialog for the entity name specified by the buttons attribute
   * Once the user selects an item in the lookup, the selected item is passed back to our callback method.
   * Our callback method retrieves the id, name, entity type fields from the selected item and injects the
   * values into a resultDiv on the control to showcase the selected values.
   *
   * @param event : OnClick Event
   */
  private onLookupObjectsButtonClick(event: Event): void {
    // Get the entity name for the button
    let entityName: string = event.srcElement!.getAttribute("entityName")!;
    var lookUpOptions: any = {
      // Note: lookup can support multiple entity types with the below syntax
      // entityTypes: ["account", "contact"]
      entityTypes: [entityName]
    };
    var lookUpPromise: any = this._context.utils.lookupObjects(lookUpOptions);
    lookUpPromise.then(
      // Callback method - invoked after user has selected an item from the lookup dialog
      // Data parameter is the item selected in the lookup dialog
      (data: any) => {
        if (data && data[0] && this._lookupObjectsResultDiv) {
          let id: string = data[0].id;
          let name: string = data[0].name;
          let entityType: string = data[0].entityType;
          let resultHTML: string = this.LOOKUP_OBJECTS_RESULT_DIV_STRING;
          resultHTML += "<br/>";
          resultHTML += "Entity ID: ";
          resultHTML += id;
          resultHTML += "<br/>";
          resultHTML += "Entity Name: ";
          resultHTML += name;
          resultHTML += "<br/>";
          resultHTML += "Entity Type: ";
          resultHTML += entityType;
          this._lookupObjectsResultDiv.innerHTML = resultHTML;
        }
      },
      (error: any) => {
        // Error handling code here
      }
    );
  }
  /**
   * Generates HTML Button that invokes the lookup dialog and appends to custom control container
   * Generates HTML Div that displays the result of the call to the lookup dialog
   * @param entityName : name of entity that should be used by the lookup dialog
   */
  private GenerateLookupObjectElements(entityName: string): void {
    this._lookupObjectsButton = this.createHTMLButtonElement(
      this.BUTTON_LABEL_CLICK_STRING + " lookupObjects(" + entityName + ")",
      this.onLookupObjectsButtonClick.bind(this),
      entityName
    );
    this._container.appendChild(this._lookupObjectsButton);
    this._lookupObjectsResultDiv = document.createElement("div");
    this._lookupObjectsResultDiv.setAttribute(
      "class",
      "lookupObjectsResultDiv"
    );
    let resultDivString: string = this.LOOKUP_OBJECTS_RESULT_DIV_STRING;
    resultDivString += "<br />";
    resultDivString += "none";
    this._lookupObjectsResultDiv.innerHTML = resultDivString;
    this._container.appendChild(this._lookupObjectsResultDiv);
  }
  /**
   * Creates an HTML Table that showcases examples of basic methods available to the custom control
   * The left column of the table shows the method name or property that is being used
   * The right column of the table shows the result of that method name or property
   */
  private createHTMLTableElement(): HTMLTableElement {
    // Create HTML Table Element
    let tableElement: HTMLTableElement = document.createElement("table");
    tableElement.setAttribute("class", "SampleControlHtmlTable_HtmlTable");
    // Create header row for table
    let key: string = "Example Method";
    let value: string = "Result";
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, true));
    // Example use of getFormFactor() method
    // Open the control on different form factors to see the value change
    key = "getFormFactor()";
    value = String(this._context.client.getFormFactor());
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example use of getClient() method
    // Open the control on different clients (phone / tablet/ web) to see the value change
    key = "getClient()";
    value = String(this._context.client.getClient());
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of userName property
    // Log in with a different user to see the user name change
    key = "userName";
    value = String(this._context.userSettings.userName);
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of isRTL property
    // Update your language to an RTL language (for example: Hebrew) to see this value change
    key = "User Language isRTL";
    value = String(this._context.userSettings.isRTL);
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of numberFormattingInfo and formatCurrency
    // Retrieve the currencyDecimalDigits and currencySymbol from the numberFormattingInfo object to retrieve the
    // preferences set in the current users 'User Settings'
    // Pass these values as parameters into the formatting.formatCurrency utility method to format the number per the users preferences
    key = "formatting formatCurrency";
    let numberFormattingInfo: ComponentFramework.UserSettingApi.NumberFormattingInfo = this
      ._context.userSettings.numberFormattingInfo;
    let percision: number = numberFormattingInfo.currencyDecimalDigits;
    let currencySymbol: string = numberFormattingInfo.currencySymbol;
    value = this._context.formatting.formatCurrency(
      100500,
      percision,
      currencySymbol
    );
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of formatDateLong
    // Pass a JavaScript Data object set to the current time into formatDateLong method to format the data
    // per the users preferences in 'User Settings'
    key = "formatting formatDateLong";
    value = this._context.formatting.formatDateLong(new Date());
    tableElement.appendChild(this.createHTMLTableRowElement(key, value, false));
    // Example of getEntityMetadata
    // Retrieve the Entity Metadata for the entityName parameter. In the callback method, retrieve the primaryNameAttribute, logicalName,
    // and isCustomEntity attributes and inject the results into the Example HTML Table
    this._context.utils
      .getEntityMetadata(this.ENTITY_LOGICAL_NAME_FOR_METADATA_EXAMPLE)
      .then(
        entityMetadata => {
          // Generate the HTML Elements used for the lookup control example
          this.GenerateLookupObjectElements(
            this.ENTITY_LOGICAL_NAME_FOR_METADATA_EXAMPLE
          );
        },
        error => {
          // Error handling code here
        }
      );
    return tableElement;
  }
  /**
   * Helper method to create an HTML Table Row Element
   *
   * @param key : string value to show in left column cell
   * @param value : string value to show in right column cell
   * @param isHeaderRow : true if method should generate a header row
   */
  private createHTMLTableRowElement(
    key: string,
    value: string,
    isHeaderRow: boolean
  ): HTMLTableRowElement {
    let keyCell: HTMLTableCellElement = this.createHTMLTableCellElement(
      key,
      "SampleControlHtmlTable_HtmlCell_Key",
      isHeaderRow
    );
    let valueCell: HTMLTableCellElement = this.createHTMLTableCellElement(
      value,
      "SampleControlHtmlTable_HtmlCell_Value",
      isHeaderRow
    );
    let rowElement: HTMLTableRowElement = document.createElement("tr");
    rowElement.setAttribute("class", "SampleControlHtmlTable_HtmlRow");
    rowElement.appendChild(keyCell);
    rowElement.appendChild(valueCell);
    return rowElement;
  }
  /**
   * Helper method to create an HTML Table Cell Element
   *
   * @param cellValue : string value to inject in the cell
   * @param className : class name for the cell
   * @param isHeaderRow : true if method should generate a header row cell
   */
  private createHTMLTableCellElement(
    cellValue: string,
    className: string,
    isHeaderRow: boolean
  ): HTMLTableCellElement {
    let cellElement: HTMLTableCellElement;
    if (isHeaderRow) {
      cellElement = document.createElement("th");
      cellElement.setAttribute(
        "class",
        "SampleControlHtmlTable_HtmlHeaderCell " + className
      );
    } else {
      cellElement = document.createElement("td");
      cellElement.setAttribute(
        "class",
        "SampleControlHtmlTable_HtmlCell " + className
      );
    }
    let textElement: Text = document.createTextNode(cellValue);
    cellElement.appendChild(textElement);
    return cellElement;
  }
  /**
   * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
   */
  public updateView(context: ComponentFramework.Context<IInputs>): void {
    if (!this._controlViewRendered) {
      // Render and add HTMLTable to the custom control container element
      let tableElement: HTMLTableElement = this.createHTMLTableElement();
      this._container.appendChild(tableElement);
      // Render and add set full screen button to the custom control container element
      this._setFullScreenButton = this.createHTMLButtonElement(
        this.getSetFullScreenButtonLabel(!this._isFullScreen),
        this.onSetFullScreenButtonClick.bind(this),
        null
      );
      this._container.appendChild(this._setFullScreenButton);
      this._controlViewRendered = true;
    }
  }
  /**
   * It is called by the framework prior to a control receiving new data.
   * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
   */
  public getOutputs(): IOutputs {
    // no-op: method not leveraged by this example custom control
    return {};
  }
  /**
   * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
   * i.e. canceling any pending remote calls, removing listeners, etc.
   */
  public destroy() {}
}
```

## Resources

```css
.SampleNamespace\.TSTableControl {
  font-family: "SegoeUI-Semibold", "Segoe UI Semibold", "Segoe UI Regular",
    "Segoe UI";
}
.SampleNamespace\.TSTableControl .TSTable_Container {
  overflow-x: auto;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlRow {
  background-color: #ffffff;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlHeaderCell {
  text-align: center;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlCell,
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlHeaderCell {
  border: 1px solid black;
  padding-left: 3px;
  padding-right: 3px;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlHeaderCell {
  font-weight: bold;
  font-size: 16px;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlCell_Key {
  color: #1160b7;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_HtmlCell_Value {
  color: #1160b7;
  text-align: center;
}
.SampleNamespace\.TSTableControl .SampleControlHtmlTable_ButtonClass {
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  cursor: pointer;
  color: #1160b7;
  background-color: #ffffff;
  border: 1px solid black;
  padding: 5px;
  text-align: center;
  min-width: 300px;
  margin-top: 10px;
  margin-bottom: 5px;
  display: block;
}
.SampleNamespace\.TSTableControl .lookupObjectsResultDiv {
  color: #1160b7;
}
```

This sample provides examples on how to use methods from the `IClient, IUserSettings, IUtility, IFormatting interfaces`.

This component also showcases two utility functions, `setFullScreen` and `lookupObjects`. These functions are invoked by clicking the button rendered as part of the code component. The `setFullScreen` button toggles the component in and out of full screen mode. The `lookupObjects` button opens a lookup dialog, and then inject the selected record as text into div.

In this sample, we render an HTML button and attach a JavaScript `onClick` event handler `onLookupObjectsButtonClick` to the button. On click of this button, we invoke `context.utils.lookupObjects()` method and pass as a parameter an array of entity names. 

This method returns a JavaScript Promise object, representing the completion or failure of the call to the lookup dialog. If the promise is resolved successfully, the lookup object which the user selected is passed as a parameter into the callback method and can be referenced as data.id, data.name, data.entityType.

The callback method injects this information as HTML into a div rendered on the code component to showcase the selected results to the user. If the promise is rejected, the error callback method is invoked where your component can handle the error scenario accordingly.

### Related topics

[Download sample components](https://go.microsoft.com/fwlink/?linkid=2088525)<br/>
[How to use the sample components](use-sample-components.md)<br/>
[PowerApps component framework API reference](../reference/index.md)<br/>
[PowerApps component framework manifest schema reference](../manifest-schema-reference/index.md)