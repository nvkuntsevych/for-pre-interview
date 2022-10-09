# for-pre-interview
This repository contains two part: [task_1](task_1)(Data aggregation) and [task_2](task_2)(Simple TODO app).


## task_1
*task_1* is an project, which groups data from given ".csv" file.  
*task_1* consists of two files: *data.csv* and *solution.py*.  
*data.csv* file contains two columns: *country* and *person*.  
App *solution.py* reads data from *data.csv* file and groups this data by the country and 
print out all the people and their count for each country.

#### Using task_1
For using task1 you shlould do the following steps:
1. Clone this repository. It can be done by two ways:  
If you use the web URL:  
`git clone https://github.com/nvkuntsevych/for-pre-interview.git`  
If you use the SSH key:  
`git clone git@github.com:nvkuntsevych/for-pre-interview.git`  
2. Open the *task_1* directory, which is in *for-pre-interview*;  
3. Run the *solution.py* file.  

If you want to use your own *.csv* file for grouping and printing out, you should do the next things:  
1. Insert your *.csv* file into *task_1* directory. *data.csv* file must contain only two columns: *country* and *person*;  
2. Open *solution.py* file and specify name of inserted *.csv* file and path to it with *PATH_TO_FILE* variable;  
3. Run the *solution.py* file.  