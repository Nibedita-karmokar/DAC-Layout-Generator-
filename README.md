
# DAC Layout Generator

## Overview

DAC Layout Generator is a Python framework for automated placement and routing of common-centroid capacitor arrays used in binary-weighted and split-capacitor DACs.

This code implements the methodology presented in:

N. Karmokar, A. K. Sharma, J. Poojary, M. Madhusudan, R. Harjani, and Sachin S. Sapatnekar,
"Constructive Placement and Routing for Common-Centroid Capacitor Arrays in Binary-Weighted and Split DACs", IEEE TCAD, 2023.

The framework automatically generates common-centroid capacitor placements and routing solutions while considering matching requirements and routing constraints.

---

## Repository Structure

DAC_Layout_Generator/
	ALIGN_func.py                   # Main entry point
	Cap_Layout_Generation.py        # Placement generation
	Global_detailed_routing_main.py # Global and detailed routing
	Layout_generator.py             # Layout generation utilities
	layers.json                     # Technology information
	test.json                       # Layout boundary definition
	DAC_general.png                 # Example output

## Requirements
pip install numpy matplotlib

## Running the Tool
python ALIGN_func.py

Example input:
1 2 4 8 16

where each number represents the weight of a capacitor group in the DAC.

## Inputs

1. Capacitor Weights

Provided interactively when running the tool.

Example:

```text
Enter a list element separated by space:
1 2 4 8 16
```

These values represent the capacitor weights of the DAC and are internally converted into a unit-capacitor representation.

2. Technology Description (`layers.json`)

Contains technology-specific routing information, including:

* Metal layers
* Via definitions
* Routing directions
* Layer width and pitch
* Resistance and capacitance parameters

3. Layout Boundary (`test.json`)

Defines the layout boundary used during placement and routing.

Example:

```json
{
  "bbox": [0, 0, 2320, 3024]
}
```

---

## Methodology

The flow consists of:

1. Unit-capacitor array generation
2. Common-centroid placement generation
3. Global routing
4. Detailed routing
5. Layout visualization

The current implementation uses a spiral-based common-centroid placement strategy.

## Outputs

The framework generates:

1. Placement Information

* Unit-capacitor coordinates
* Capacitor grouping information
* Common-centroid placement structure

2. Routing Information

* Global routing assignments
* Detailed routing tracks
* Via locations

3. Layout Objects

* Capacitor terminals
* Wire segments
* Routing geometries

4. Visualization

* Generated capacitor-array layout
* Routing topology visualization
  

## Citation

If you use this code in academic work, please cite:

N. Karmokar, A. K. Sharma, J. Poojary, M. Madhusudan, R. Harjani, and Sachin S. Sapatnekar,
"Constructive Placement and Routing for Common-Centroid Capacitor Arrays in Binary-Weighted and Split DACs,"
IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2023.

