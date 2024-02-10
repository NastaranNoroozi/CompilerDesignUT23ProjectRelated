Fifth Homework
***************************
# CompilerDesignUT23ProjectRelated
This section is dedicated to the tasks related to the project and since our group had 3 tasks for 2 persons, it only includes HW5.

# Code Analysis Comparison - OpenUnderstand vs. Understand

This project involves the analysis of a Java codebase using two different tools: OpenUnderstand and the original Understand tool. Below, we provide details on how to use both tools and compare the results.

## OpenUnderstand

### Overview

OpenUnderstand is a custom library used for code analysis. The analysis script (`test_run.py`) uses OpenUnderstand to open an database and retrieve information about classes in the codebase.

### Usage

1. Clone the OpenUnderstand repository:
   ```bash
   git clone https://github.com/m-zakeri/OpenUnderstand.git
   cd OpenUnderstand
   git fetch
   git checkout -b dev origin/dev
   ```

2. Make things costumize in config.ini, test_openunderstand.py and test_run.py

### Result

[![mypicforhw5p1.png](https://i.postimg.cc/52ZZwXbx/mypicforhw5p1.png)](https://postimg.cc/pmJGvXm7)

[![NNOpen-Understand-Screenshot.png](https://i.postimg.cc/DZk3Cg2b/NNOpen-Understand-Screenshot.png)](https://postimg.cc/FfZ6z0k9)

## Original Understand Tool

### Overview

The original Understand tool is a commercial code analysis tool. The analysis script (`api.py`) uses the Understand Python API to analyze the Java code and print information about the classes.

### Usage

1. Install the Understand tool from [SciTools website](https://scitools.com/download/all-products/).

2. Run the analysis script in test Directory:
   ```bash
   python api.py
   ```
### Result

[![mypicforhw5p2.jpg](https://i.postimg.cc/rF7WcTqd/mypicforhw5p2.jpg)](https://postimg.cc/sv919tQy)

[![mypicforhw5p3.png](https://i.postimg.cc/Gpd4hhVp/mypicforhw5p3.png)](https://postimg.cc/rDZVfc86)

### SymbolTables

In order to preview the tables on mac I used RazorSQL and nothing special is needed to download this app, you just need to learn to work with it.

[![NNSymbol-Tables.png](https://i.postimg.cc/KY9TXJq4/NNSymbol-Tables.png)](https://postimg.cc/5HCyLqMM)


   ## Comparison

While both tools aim to analyze the codebase, there are differences in the reported classes.
   
