---
title: "React Facepile component| Microsoft Docs" 
description: "Implementing a Facepile component using React" 
ms.custom: ""
author: ghurlman
manager: kvivek
ms.date: 06/19/2019
ms.service: "powerapps"
ms.topic: "article"
ms.author: "grhurl"
ms.reviewer: nkrb
---

# Implementing the FacePile component

This sample shows how to use React to create components using PowerApps component framework.  The facepile sample component is implemented based on React and the Office UI Fabric React components. The code may not reveal the best practices for the mentioned third-party libraries.

> [!div class="mx-imgBorder"]
> ![React Facepile](../media/react-facepile.png "React Facepile")

## Available for 

Model-driven apps and canvas apps (experimental preview) 


> [!IMPORTANT]
> Although the PowerApps host applications work on top of React, the version of React you bundle will not communicate with the host version, nor is it dependent on that version. A new copy of React (or any third-party library you bundle with your component) will be loaded into the host page for every instance of that control, so be mindful of how large you are making your page(s) as you add components. We will have a solution to this issue in a future release.

## Manifest

```XML
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleControls" constructor="ReactStandardControl" version="0.0.1" display-name-key="ReactStandardControl_Display_Key" description-key="ReactStandardControl_Desc_Key" control-type="standard">
    <!-- property node identifies a specific, configurable piece of data that the control expects from CDS -->
    <property name="numberOfFaces" display-name-key="numberOfFaces" description-key="numberOfFaces" of-type="Whole.None" usage="bound" required="false" />
    <resources>
      <css path="css/ReactStandardControl.css" order="1" />
      <code path="index.ts" order="2"/>
    </resources>
  </control>
</manifest>
```

## overview

This sample provides examples on how to add dependencies for third-party libraries and Office UI Fabric, showcasing how to utilize the Office UI Fabric components for React for UI and perform bi-directional data-binding between the PowerApps component framework and the React state model.

The component sample consists of three Office UI Fabric components: a facepile, a slider, a check box, and a drop-down list. When you move the slider, the number of faces in the facepile changes. The check box components whether the faces fade in and out or simply appear or disappear, and the options in the drop-down list control the size of the faces. If there is no value set, the number of faces defaults to 3.

- When the component is loaded, the slider is set to the bound attribute value. The `context.parameters.[property_name].attributes` property contains the associated metadata.
- An event handler is passed in the React component's props; this will allow the React component to notify the host PowerApps component framework control that a value has changed. The event handler then determines if a call to the **notifyOutputEvents** method is necessary.
- Sliding the slider will cause React to update the bound value and call the passed in event handler. Inside that handler, if a call is made to the **notifyOutputEvents** method, then the control's [getOutputs](../reference/control/getoutputs.md) method will be called asynchronously and will flow to the PowerApps component framework. 
- The framework host updates the bound attribute value, and the updated value flows to the component, triggering the control’s [updateView](../reference/control/updateview.md) method. The control then rerenders the React component with the new value.


## Code

```TypeScript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
import * as React from "react";
import * as ReactDOM from "react-dom";
import { FacepileBasicExample, IFacepileBasicExampleProps } from "./Facepile";

export class ReactStandardControl
  implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  // reference to the notifyOutputChanged method
  private notifyOutputChanged: () => void;
  // reference to the container div
  private theContainer: HTMLDivElement;
  // reference to the React props, prepopulated with a bound event handler
  private props: IFacepileBasicExampleProps = {
    numberFacesChanged: this.numberFacesChanged.bind(this)
  };

  /**
   * Empty constructor.
   */
  constructor() {}

  /**
   * Used to initialize the control instance. Controls can kick off remote server calls and other initialization actions here.
   * Data-set values are not initialized here, use updateView.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to property names defined in the manifest, as well as utility functions.
   * @param notifyOutputChanged A callback method to alert the framework that the control has new outputs ready to be retrieved asynchronously.
   * @param state A piece of data that persists in one session for a single user. Can be set at any point in a controls life cycle by calling 'setControlState' in the Mode interface.
   * @param container If a control is marked control-type='starndard', it will receive an empty div element within which it can render its content.
   */
  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ) {
    this.notifyOutputChanged = notifyOutputChanged;
    this.props.numberOfFaces = context.parameters.numberOfFaces.raw || 3;
    this.theContainer = container;
  }

  /**
   * Called when any value in the property bag has changed. This includes field values, data-sets, global values such as container height and width, offline status, control metadata values such as label, visible, etc.
   * @param context The entire property bag available to control via Context Object; It contains values as set up by the customizer mapped to names defined in the manifest, as well as utility functions
   */
  public updateView(context: ComponentFramework.Context<IInputs>): void {
    if (context.updatedProperties.includes("numberOfFaces"))
      this.props.numberOfFaces = context.parameters.numberOfFaces.raw || 3;

    // Render the React component into the div container
    ReactDOM.render(
      // Create the React component
      React.createElement(
        FacepileBasicExample, // the class type of the React component found in Facepile.tsx
        this.props
      ),
      this.theContainer
    );
  }

  /**
   * Called by the React component when it detects a change in the number of faces shown
   * @param newValue The newly detected number of faces
   */
  private numberFacesChanged(newValue: number) {
    // only update if the number of faces has truly changed
    if (this.props.numberOfFaces !== newValue) {
      this.props.numberOfFaces = newValue;
      this.notifyOutputChanged();
    }
  }

  /**
   * It is called by the framework prior to a control receiving new data.
   * @returns an object based on nomenclature defined in manifest, expecting object[s] for property marked as “bound” or “output”
   */
  public getOutputs(): IOutputs {
    return {
      numberOfFaces: this.props.numberOfFaces
    };
  }

  /**
   * Called when the control is to be removed from the DOM tree. Controls should use this call for cleanup.
   * i.e. cancelling any pending remote calls, removing listeners, etc.
   */
  public destroy(): void {
    ReactDOM.unmountComponentAtNode(this.theContainer);
  }
}

```

### Facepile.tsx

```TSX
import * as React from "react";
import { Checkbox } from "office-ui-fabric-react/lib/Checkbox";
import { Dropdown, IDropdownOption } from "office-ui-fabric-react/lib/Dropdown";
import { Facepile, IFacepilePersona, IFacepileProps, OverflowButtonType } from "office-ui-fabric-react/lib/Facepile";
import { PersonaSize } from "office-ui-fabric-react/lib/Persona";
import { Slider } from "office-ui-fabric-react/lib/Slider";
import { facepilePersonas } from "./FacepileExampleData";
import { setIconOptions } from "office-ui-fabric-react/lib/Styling";

// Suppress office UI fabric icon warnings.
setIconOptions({
  disableWarnings: true,
});

export interface IFacepileBasicExampleProps {
  numberOfFaces?: number;
  numberFacesChanged?: (newValue: number) => void;
}

export interface IFacepileBasicExampleState extends React.ComponentState, IFacepileBasicExampleProps {
  personaSize: PersonaSize;
  imagesFadeIn: boolean;
}

export class FacepileBasicExample extends React.Component<IFacepileBasicExampleProps, IFacepileBasicExampleState> {
  constructor(props: IFacepileBasicExampleProps) {
    super(props);

    this.state = {
      numberOfFaces: props.numberOfFaces || 3,
      imagesFadeIn: true,
      personaSize: PersonaSize.size32
    };
  }

  public componentWillReceiveProps(newProps: IFacepileBasicExampleProps): void {
    this.setState(newProps);
  }

  public render(): JSX.Element {
    const { numberOfFaces, personaSize } = this.state;
    const facepileProps: IFacepileProps = {
      personaSize,
      personas: facepilePersonas,
      overflowButtonType: OverflowButtonType.descriptive,
      maxDisplayablePersonas: this.state.numberOfFaces,
      getPersonaProps: (persona: IFacepilePersona) => {
        return {
          imageShouldFadeIn: this.state.imagesFadeIn,
        };
      },
      ariaDescription: "To move through the items use left and right arrow keys.",
    };

    return (
      <div className={"msFacepileExample"}>
        <Facepile {...facepileProps} />
        <div className={"control"}>
          <Slider
            label="Number of Personas:"
            min={1}
            max={5}
            step={1}
            showValue={true}
            value={numberOfFaces}
            onChange={this.onChangePersonaNumber}
          />
          <Dropdown
            label="Persona Size:"
            selectedKey={this.state.personaSize}
            options={[
              { key: PersonaSize.size16, text: "16px" },
              { key: PersonaSize.size24, text: "24px" },
              { key: PersonaSize.size28, text: "28px" },
              { key: PersonaSize.size32, text: "32px" },
              { key: PersonaSize.size40, text: "40px" },
            ]}
            onChange={this.onChangePersonaSize}
          />
          <Checkbox
            className={"exampleCheckbox"}
            label="Fade In"
            checked={this.state.imagesFadeIn}
            onChange={this.onChangeFadeIn}
          />
        </div>
      </div>
    );
  }

  private onChangeFadeIn = (
    ev: React.FormEvent<HTMLElement | HTMLInputElement> | undefined,
    checked?: boolean
  ): void => {
    this.setState(
      (prevState: IFacepileBasicExampleState): IFacepileBasicExampleState => {
        prevState.imagesFadeIn = checked!;
        return prevState;
      }
    );
  };

  private onChangePersonaNumber = (value: number): void => {
    this.setState(
      (prevState: IFacepileBasicExampleState): IFacepileBasicExampleState => {
        prevState.numberOfFaces = value;
        return prevState;
      }
    );
    if (this.props.numberFacesChanged) {
      this.props.numberFacesChanged(value);
    }
  };

  private onChangePersonaSize = (event: React.FormEvent<HTMLDivElement>, value?: IDropdownOption): void => {
    this.setState(
      (prevState: IFacepileBasicExampleState): IFacepileBasicExampleState => {
        prevState.personaSize = value ? (value.key as PersonaSize) : PersonaSize.size32;
        return prevState;
      }
    );
  };
}
```

### FacepileExampleData.ts

```TypeScript
import * as React from 'react';
import { IFacepilePersona } from 'office-ui-fabric-react/lib/Facepile';
import { PersonaInitialsColor } from 'office-ui-fabric-react/lib/Persona';
import { TestImages } from './TestImages';

export const facepilePersonas: IFacepilePersona[] = [
  {
    imageUrl: TestImages.personaFemale,
    personaName: 'Annie Lindqvist',
    data: '50%'
  },
  {
    imageUrl: TestImages.personaMale,
    personaName: 'Aaron Reid',
    data: '$1,000'
  },
  {
    personaName: 'Alex Lundberg',
    data: '75%',
    onClick: (ev?: React.MouseEvent<HTMLElement>, persona?: IFacepilePersona) => {
      if (persona)
        alert('You clicked on ' + persona.personaName + '. Extra data: ' + persona.data);
    }
  },
  {
    personaName: 'Roko Kolar',
    data: '4 hrs'
  },
  {
    imageInitials: 'CB',
    personaName: 'Christian Bergqvist',
    initialsColor: PersonaInitialsColor.green,
    data: '25%'
  },
  {
    imageUrl: TestImages.personaFemale,
    imageInitials: 'VL',
    personaName: 'Valentina Lovric',
    initialsColor: PersonaInitialsColor.lightBlue,
    data: 'Emp1234',
    onClick: (ev?: React.MouseEvent<HTMLElement>, persona?: IFacepilePersona) => {
      if (persona)
        alert('You clicked on ' + persona.personaName + '. Extra data: ' + persona.data);
    }
  },
  {
    imageUrl: TestImages.personaMale,
    imageInitials: 'MS',
    personaName: 'Maor Sharett',
    initialsColor: PersonaInitialsColor.lightGreen
  },
  {
    imageUrl: TestImages.personaFemale,
    imageInitials: 'PV',
    personaName: 'Annie Lindqvist2',
    initialsColor: PersonaInitialsColor.lightPink
  },
  {
    imageUrl: TestImages.personaMale,
    imageInitials: 'AR',
    personaName: 'Aaron Reid2',
    initialsColor: PersonaInitialsColor.magenta,
    data: 'Emp1234',
    onClick: (ev?: React.MouseEvent<HTMLElement>, persona?: IFacepilePersona) => {
      if (persona)
        alert('You clicked on ' + persona.personaName + '. Extra data: ' + persona.data);
    }
  },
  {
    imageUrl: TestImages.personaMale,
    imageInitials: 'AL',
    personaName: 'Alex Lundberg2',
    initialsColor: PersonaInitialsColor.orange
  }

  // Trimmed for display; full file in the downloadable sample code
```

### TestImages.ts

```TypeScript
const baseProductionCdnUrl = 'https://static2.sharepointonline.com/files/fabric/office-ui-fabric-react-assets/';

export const TestImages = {
  choiceGroupBarUnselected: baseProductionCdnUrl + 'choicegroup-bar-unselected.png',
  choiceGroupBarSelected: baseProductionCdnUrl + 'choicegroup-bar-selected.png',
  choiceGroupPieUnselected: baseProductionCdnUrl + 'choicegroup-pie-unselected.png',
  choiceGroupPieSelected: baseProductionCdnUrl + 'choicegroup-pie-selected.png',
  documentPreview: baseProductionCdnUrl + 'document-preview.png',
  documentPreviewTwo: baseProductionCdnUrl + 'document-preview2.png',
  documentPreviewThree: baseProductionCdnUrl + 'document-preview3.png',
  iconOne: baseProductionCdnUrl + 'icon-one.png',
  iconPpt: baseProductionCdnUrl + 'icon-ppt.png',
  personaFemale: baseProductionCdnUrl + 'persona-female.png',
  personaMale: baseProductionCdnUrl + 'persona-male.png'
};
```

## Resources

### css/ReactStandardControl.css

```css
.msFacepileExample {
  max-width: 300px;
}

.msFacepileExample .control {
  padding-top: 20px;
}

.msFacepileExample .ms-Dropdown-container,
.msFacepileExample .ms-Slider {
  margin: 10px 0 10px 0;
}

.msFacepileExample .ms-Dropdown-container .ms-Label {
  padding-top: 0;
}

.msFacepileExample .ms-Checkbox {
  padding-top: 15px;
}

.exampleCheckbox {
  margin: 10px 0;
}

.exampleLabel {
  margin: 10px 0;
}
```

### Related topics

[PowerApps component framework Manifest Schema reference](../manifest-schema-reference/index.md)<br />
[PowerApps component framework API reference](../reference/index.md)<br />
[PowerApps component framework overview](../overview.md)
