---
title: "Implementing Custom Controls using TypeScript | MicrosoftDocs"
description: "How to implement a custom control using TypeScript"
manager: kvivek
ms.date: 04/20/2019
ms.service: "powerapps"
ms.author: "nabuthuk"
---

# Implement controls using TypeScript

This tutorial will walk you through creating a new custom control in Typescript. The sample control is a linear input control. The linear input control enables users to enter numeric values using a visual slider instead of directly keying in values.


## Implementing Manifest

A custom control is defined by the information in the `Manifest.xml` manifest file. For the linear input control, a property will be defined to store the numeric value of the slider input.

1. Open the `Manifest.xml` file in the code editor (Visual Studio Code). The `Manifest.xml` file defines an initial control property called `sampleProperty`.

    ```XML
    <property name="sampleProperty" display-name-key="Property_Display_Key" description-key="Property_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" /> 
    ```

2. Rename the `sampleProperty` and change the property type

    ```XML
    <property name="sliderValue" display-name-key=" sliderValue _Display_Key" description-key=" sliderValue_Desc_Key" of-type-group="numbers" usage="bound" required="true" /> 
    ```

3. The of-type-group attribute references a group of allowable numbers. Add the following type-group element as a sibling to the <property> element in the manifest. The type-group specifies the control value and can contain whole, currency, floating point, or decimal values.

    ```XML
    <type-group name="numbers"> 
      <type>Whole.None</type> 
      <type>Currency</type> 
      <type>FP</type> 
      <type>Decimal</type> 
     </type-group> 
    ```


4. Save the changes to the `ControlManifest.Input.xml` file.
5. Build the control project using the command `npm run build`.
6. The build generates an updated Typescript type declaration file under `TSLinearInputControl/generated folder`.  The `ManifestTypes.d.ts` file defines the properties that your control will have access to Typescript source code.

## Implementing control logic

Source for the custom control is implemented in the `index.ts` file. The `index.ts` file includes scaffolding for interface methods that are required by the PowerApps Component Framework. 

1. Open the `index.ts` file in code editor of your choice.
2. Update the `TSLinearInputControl` class with the following

```TypeScript
export class TSLinearInputControl implements ComponentFramework.StandardControl<IInputs, IOutputs> {
// Value of the field is stored and used inside the control 
private _value: number;
// PCF framework delegate which will be assigned to this object which would be called whenever any update happens. 
private _notifyOutputChanged: () => void;
// label element created as part of this control
private labelElement: HTMLLabelElement;
// input element that is used to create the range slider
private inputElement: HTMLInputElement;
// Reference to the control container HTMLDivElement
// This element contains all elements of our custom control example
private _container: HTMLDivElement;
// Reference to ComponentFramework Context object
 private _context: ComponentFramework.Context<IInputs>;
// Event Handler 'refreshData' reference
 private _refreshData: EventListenerOrEventListenerObject;
	
constructor() {
	}
	
public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement)
  {
     this._context = context;
     this._container = document.createElement("div");
     this._notifyOutputChanged = notifyOutputChanged;
     this._refreshData = this.refreshData.bind(this);
     // creating HTML elements for the input type range and binding it to the function which refreshes the control data
     this.inputElement = document.createElement("input");
     this.inputElement.setAttribute("type","range");
     this.inputElement.addEventListener("input",this._refreshData);
     //setting the max and min values for the control.
     this.inputElement.setAttribute("min","1");
     this.inputElement.setAttribute("max","1000");
     this.inputElement.setAttribute("class","linearslider");
     this.inputElement.setAttribute("id","linearrangeinput");
     // creating a HTML label element that shows the value that is set on the linear range control
     this.labelElement = document.createElement("label");
     this.labelElement.setAttribute("class", "TS_LinearRangeLabel");
     this.labelElement.setAttribute("id","lrclabel");
     // retrieving the latest value from the control and setting it to the HTMl elements.
     this._value = context.parameters.sliderValue.raw;
     this.inputElement.setAttribute("value",context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "0");
     this.labelElement.innerHTML = context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "0";
     // appending the HTML elements to the control's HTML container element.
     this._container.appendChild(this.inputElement);
     this._container.appendChild(this.labelElement);
     container.appendChild(this._container);
        }
	
/**
* Updates the values to the internal value variable we are storing and also updates the html label that displays the value
* @param context : The "Input Properties" containing the parameters, control metadata and interface functions
*/

public refreshData(evt: Event) : void
  {
      this._value = (this.inputElement.value as any)as number;
      this.labelElement.innerHTML = this.inputElement.value;
      this._notifyOutputChanged();
    }
		
public updateView(context: ComponentFramework.Context<IInputs>): void
 {
      // storing the latest context from the control.
    this._value = context.parameters.sliderValue.raw;
    this._context = context;
    this.inputElement.setAttribute("value",context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "");
    this.labelElement.innerHTML = context.parameters.sliderValue.formatted ? context.parameters.sliderValue.formatted : "";
        }
	
public getOutputs(): IOutputs
  {
     return {
            sliderValue : this._value
            };
        }
        
public destroy()
   {
     this.inputElement.removeEventListener("input", this._refreshData);
        }
    }
```

3. Rebuild the project using the command `npm run build` 
 
4. The control is compiled into the `/out/controls/TSLinearInputControl` folder. The build artifacts includes:

   - bundle.js – Bundled control source code 
   - ControlManifest.xml – Actual control manifest file that will be uploaded to Common Data Service organization.

## Adding Style to the custom control

The linear input control’s `init` method creates an input element and sets the class attribute to `linearslider`. The style for the `linearslider` class is defined in a separate `css` file. Additional control resources like `css` files can be included with the custom control to support further customizations.

1. Edit the `ControlManifest.Input.xml` file to include an additional `css` resource inside the <resources> element
 
    ```XML
      <resources> 
      <code path="index.ts" order="1"/> 
      <css path="css/TS_LinearInputControl.css" order="1"/> 
    </resources> 
     ```

2. Create a new `css` sub folder under the `TSLinearInputControl` folder. 
3. Create a new `TS_LinearInputControl.css` file inside the `css` sub folder. 
4. Add the following style content to `TS_LinearInputControl.css` file

   ```CSS
    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider {    
    margin: 1px 0;    
    background:transparent; 
   -webkit-appearance:none; 
    width:100%;padding:0; 
    height:24px; 
   -webkit-tap-highlight-color:transparent 
    } 
    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider:focus { 
     outline: none; 
     } 
    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-webkit-slider-runnable-track {    
     background: #666; 
     height:2px; 
     cursor:pointer 
     }    
     .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-webkit-slider-thumb {    
     background: #666;    
     border:0 solid #f00; 
     height:24px; 
     width:10px; 
     border-radius:48px; 
     cursor:pointer; 
     opacity:1; 
    -webkit-appearance:none; 
     margin-top:-12px 
     }     
    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-moz-range-track {    
     background: #666;    
     height:2px; 
     cursor:pointer   
     }    
     .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-moz-range-thumb {    
     background: #666;    
     border:0 solid #f00; 
     height:24px; 
     width:10px; 
     border-radius:48px; 
    cursor:pointer; 
    opacity:1; 
   -webkit-appearance:none; 
   margin-top:-12px 
   }    
   .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-ms-track {    
    background: #666;    
    height:2px; 
    cursor:pointer   
     }     
    .SampleNamespace\.TSLinearInputControl input[type=range].linearslider::-ms-thumb {    
    background: #666;    
    border:0 solid #f00; 
    height:24px; 
    width:10px; 
    border-radius:48px; 
   cursor:pointer; 
   opacity:1; 
   -webkit-appearance:none; 
    } 
   ```

5. Save the `TS_LinearInputControl.css` 
6. Rebuild the project using the command `npm run build `.
7. Inspect the build output under `./out/controls/TSLinearInputControl` and observe that the `TS_LinearInputControl.css` file is now included with the compiled build artifacts. 


### See also

[Update existing PCF controls](updating-existing-controls.md)
