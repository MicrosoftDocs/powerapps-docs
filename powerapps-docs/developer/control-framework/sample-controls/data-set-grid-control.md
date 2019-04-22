---
title: DataSet Grid component | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 356561d0-a36b-4b93-8b76-3e1abf9414e9
---

This sample component shows how to change the user experience of interacting with the dataset. For example, you only see the home page grid on an entity homepage as a table. You can build your custom component that can display the data as per your choice. This sample shows the records as tiles instead of the regular tabular grid.

> [!div class="mx-imgBorder"]
> ![Data Set Grid component](../media/data-set-grid.png "Data Set Grid component")

## Manifest 

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace" constructor="TSDataSetGrid" version="1.0.0" display-name-key="TS_DataSetGrid_Display_Key" description-key="TSIncrementControl_Desc_Key" control-type="standard">
    <data-set name="dataSetGrid" display-name-key="DataSetGridProperty_Display_Key">
	  </data-set>
    <resources>
      <code path="index.ts" order="1" />
	    <css path="css/TS_DataSetGrid.css" order="1" />
      <resx path="strings/TSDataSetGrid.1033.resx" version="1.0.0" />
    </resources>
  </control>
</manifest>
```

## Code 

```TypeScript

import {IInputs, IOutputs} from "./generated/ManifestTypes";
// Key used to store the selected color into the context object to persist across navigations 
const PERSISTED_SELECTED_COLOR_KEY_NAME = "selectedColor";
// Key used to store the selected color into the context object to persist across navigations 
const PERSISTED_SELECTED_Label_KEY_NAME = "selectedLabel";
export class TSControlStateAPI implements ComponentFramework.StandardControl<IInputs, IOutputs> 
{
	// Flag if control view has been rendered
	private _controlViewRendered: Boolean;
	// Reference to the control container HTMLDivElement
	// This element contains all elements of our custom control example
	private _container: HTMLDivElement;
	// Div element to show the current selected color
	private _selectedColorElement: HTMLDivElement;
	// Control context object
	private _context: ComponentFramework.Context<IInputs>;
	// The color selected from the previous navigation
	private _persistedSelectedColor: string;
	// The label selected from the previous navigation
	private _persistedSelectedLabel: string;
	// Data type used to store the various information as part of the state object.
	private  _stateDictionary : ComponentFramework.Dictionary = {};
	// References to HTML Button Elements rendered on the control
	private _buttonRed: HTMLButtonElement;
	private _buttonBlue: HTMLButtonElement;
	private _buttonGreen: HTMLButtonElement;
	/**
	* Empty constructor.
	*/
	constructor()
	{
	}
	/**
	 * Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
	 * Data-set values are not initialized here, use updateView.
	 * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
	 * @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
	 * @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
	 * @param container If control is marked control-type='standard', it receives an empty div element within which it can render its content.
	 */
	public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement): void
	{
		this._controlViewRendered = false;
		this._container = document.createElement("div");
		this._context = context;
		this._container.classList.add("ControlState_Container");
		container.appendChild(this._container);
		// Check if state was persisted from the last time the control was loaded.
		if (state)
		{
			// If you are storing a collection of key value pairs as part of the state object, maintain a local copy of it so that it can be used to 
			// add, update or remove keys during the control life cycle.
			this._stateDictionary = state;
			// Retrieve persisted state and set values into variables so state can be used during control rendering.
			this._persistedSelectedColor = state[PERSISTED_SELECTED_COLOR_KEY_NAME]; 
			this._persistedSelectedLabel = state[PERSISTED_SELECTED_Label_KEY_NAME]; 
		}
		// State not persisted in control -- set variable to default values
		if (!this._persistedSelectedColor)
		{
			this._persistedSelectedColor = "transparent";
		}
		// State not persisted in control -- set variable to default values
		if (!this._persistedSelectedLabel)
		{
			this._persistedSelectedLabel = "none";
		}
	}
	/**
	 * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
	 * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
	 */
	public updateView(context: ComponentFramework.Context<IInputs>): void
	{
		if (!this._controlViewRendered)
		{
			// Render header label
			let chooseColorLabel: HTMLElement = this.renderLabelDivElement("Select a Color");
			this._container.appendChild(chooseColorLabel);
			// Render 3 color buttons
			this._buttonGreen = this.renderButtonElement("Green", "#80ff80");
			this._container.appendChild(this._buttonGreen);
			this._buttonBlue =  this.renderButtonElement("Blue", "#add8e6");
			this._container.appendChild(this._buttonBlue);
			this._buttonRed =  this.renderButtonElement("Red", "#ff8080");
			this._container.appendChild(this._buttonRed);
			// Render label for 'selected color' area
			let selectedColorLabel: HTMLElement = this.renderLabelDivElement("Selected Color");
			this._container.appendChild(selectedColorLabel);
			// Render 'selected color' display area
			this.renderSelectedColorElement();
			this.updateSelectedColorElement(this._selectedColorElement, this._persistedSelectedLabel, this._persistedSelectedColor);
			// Mark the control view as rendered so we do not re-render next time this method is invoked
			this._controlViewRendered = true;
		}
	}
	/**
	 * Creates an HTML Div Element with the provided label
	 * 
	 * @param labelText : label for the div 
	 */
	private renderLabelDivElement(labelText: string): HTMLDivElement
	{
		let div: HTMLDivElement = document.createElement("div");
		div.innerText = labelText;
		div.classList.add("ControlState_DivLabelClass");
		return div;
	}
	/**
	 * Renders a button element that the user can click to select a color
	 * 
	 * @param label : label for the button (color name)
	 * @param color : Hex code for the color
	 */
	private renderButtonElement(label: string, color: string): HTMLButtonElement
	{
		let button: HTMLButtonElement = document.createElement("button");
		button.innerHTML = label;
		button.setAttribute("value", label);
		button.setAttribute("buttonColor", color);
		button.classList.add("ControlState_ButtonClass");
		button.addEventListener("click", event => this.onButtonClick(event, this._selectedColorElement));
		return button;
	}
	/**
	 * This method updates the selected color element to reflect the last color the user selected.
	 * The label and background color will be updated to reflect the selected color.
	 * 
	 * @param selectedColorElement element to make the changes to 
	 * @param label new label for the selectedColorElement
	 * @param backgroundColor new background color for the selectedColorElement
	 */
	private updateSelectedColorElement(selectedColorElement: HTMLDivElement, label: string, backgroundColor: string)
	{
		selectedColorElement.innerText = label;
		this._selectedColorElement.style.backgroundColor = backgroundColor;
	}
	/** 
	 * Renders a div Element that will contain information regarding the last color the user selected
	 */
	private renderSelectedColorElement()
	{
		this._selectedColorElement = document.createElement("div");
		this._selectedColorElement.classList.add("ControlState_SelectedColorElement");
		this._container.appendChild(this._selectedColorElement);
	}
	/**
	 * Onclick event handler for click of a color button
	 * This method checks the button that was clicked (red / blue / green) and updates the selected color element
	 * with the selected color as the element label and background
	 * 
	 * @param event Click Event
	 * @param selectedColorElement The HTML Div Element that the results should be injected into 
	 */
	private onButtonClick(event: Event, selectedColorElement: HTMLDivElement)
	{
		if (event.srcElement)
		{
			// Get the label and the selected color attributes from the div element that was clicked
			let label:string = event.srcElement.attributes.getNamedItem("value")!.value;
			let selectedColor:string = event.srcElement!.attributes.getNamedItem("buttonColor")!.value;
			// Update the selected color div element with the results
			this.updateSelectedColorElement(selectedColorElement, label, selectedColor);
			// store the label and selected color into the local state dictionary that will be passed onto the framework.
			this._stateDictionary[PERSISTED_SELECTED_Label_KEY_NAME] = label;
			this._stateDictionary[PERSISTED_SELECTED_COLOR_KEY_NAME] = selectedColor;
			// Store the state dictionary object into the setControlState interface method to allow the 
			// selected data to persist within the user session
			// In scenarios where you don't need a collection of key value pairs but just one key value pair to be stored, just pass that object to the setControlState method.
			this._context.mode.setControlState(this._stateDictionary);
		}
	}
	/** 
	 * It is called by the framework prior to a control receiving new data. 
	 * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
	 */
	public getOutputs(): IOutputs
	{
		return {};
	}
	/** 
	 * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
	 * i.e. canceling any pending remote calls, removing listeners, etc.
	 */
	public destroy(): void
	{         
	}
}

```

## Resources

```css
.SampleNamespace\.TSDataSetGrid .DataSetControl_main-container {
    overflow-y: auto;
}

.SampleNamespace\.TSDataSetGrid .DataSetControl_grid-container {
    background-color: transparent;
    border: solid thin lightgray;
    padding: 10px;
    display: inline-block;
    overflow: auto;
}

.SampleNamespace\.TSDataSetGrid .DataSetControl_grid-item {
    margin: 5px;
    width: 200px;
    height: 200px;
    background-color: rgb(59, 121, 183);
    color: white;
    border: solid thin black;
    padding: 5px;
    text-align: center;
    float: left;
}

.SampleNamespace\.TSDataSetGrid .DataSetControl_grid-text-label {
    font-size: 12px;
    white-space: normal;
    margin: 2px;
    display: block;
    color: lightgray;
}

.SampleNamespace\.TSDataSetGrid .DataSetControl_grid-text-value {
    font-size: 12px;
    white-space: normal;
    margin: 1px;
    display: block;
    color: white;
    font-weight: bold;
}

.SampleNamespace\.TSDataSetGrid button.DataSetControl_LoadMoreButton_Style {
    background-color:#e5e5e5;
    font-size:1.5rem;
    font-weight:bold;
    height:3.5rem;
    text-align:center;
    width:100%;
    border:none
}

.SampleNamespace\.TSDataSetGrid button.DataSetControl_LoadMoreButton_Hidden_Style {
    display: none;
}

.SampleNamespace\.TSDataSetGrid .DataSetControl_grid-norecords {
    display: flex;
    align-items: center;
    justify-content: center;
  }
```

```XML
<?xml version="1.0" encoding="utf-8"?>
<root>
<xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="PCF_DataSetControl_LoadMore_ButtonLabel" xml:space="preserve">
    <value>Load More</value>
    <comment>Label for TSTableGrid's Load More Paging Button</comment>
  </data>
  <data name="PCF_DataSetControl_No_Record_Found" xml:space="preserve">
    <value>No records found.</value>
    <comment>No records found if no records</comment>
  </data>
</root>
```

In this sample, we have the input parameter defined in component manifest file with the data-set tag. This is the input property that gets bound to the component.  
 
This component has two important containers that are added onto the main div which is added onto the div that is passed onto the component.  The first container holds the tiles that show the record data from the view and the second container is for the `Load More button` that shows when there are records that need more area that can fit in one page. 
 
Both the containers are generated and refreshed whenever the [updateView](../reference/control/updateview.md) method is called. For the first container, we generate the tiles based on the information in the columns and the number of records. This ensures we display a tile for each record along with its information on it.  
 
If there exists a following page for the records, the load more button is displayed i.e., the second container is visible and is hidden if there are no more pages in the result set.  
 
On the click of load more button, we load the next page of records and append it to the existing result set and the logic to hide or show the button remains same as earlier as shown in the code. This is taken care by the ***onLoadMoreButtonClick*** method which is bound to the button.
 
The ***toggleLoadMoreButtonWhenNeeded*** function takes the input as the data set and checks, whether the data set, has next page, and if the button is hidden or visible and respectively hides or shows the button.  
 
The ***onRowClick*** function attaches the context of the record using its GUID value and invokes the [openForm](../reference/navigation/openform.md) method of the `NavigationAPI` to open that respective record. This method is bound to each tile that gets generated as part of the ***createGridBody*** method.
 
The ***getSortedColumnsOnView*** method returns the list of columns based on the defined order on the view.

### Related topics

[PowerApps component framework API Reference](../index.md)<br/>
[PowerApps component framework Manifest Schema Reference](../manifest-schema-reference/index.md)